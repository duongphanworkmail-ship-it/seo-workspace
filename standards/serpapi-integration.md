# Hướng dẫn Tích hợp SerpAPI

Tài liệu này hướng dẫn cách tích hợp SerpAPI vào các skill SEO để lấy dữ liệu thực tế thay vì phụ thuộc vào suy diễn của Claude — giúp kết quả chính xác hơn và tiết kiệm token đáng kể.

**Tổng quan tiết kiệm token:**

| Không có API | Có API |
|-------------|--------|
| Claude brainstorm từ training data (cũ, không chắc chắn) | Claude nhận JSON thực tế → chỉ phân tích |
| Cần nhiều token để reason về dữ liệu giả định | Ít token hơn — dữ liệu đã có sẵn |
| Kết quả có thể lỗi thời | Kết quả real-time |

---

## 1. Cài đặt & Cấu hình

### Cài thư viện

```bash
pip install google-search-results python-dotenv
```

> `google-search-results` là SDK chính thức của SerpAPI.

### Lưu API Key

Tạo file `.env` trong thư mục gốc workspace:

```
SERPAPI_KEY=your_api_key_here
```

> Lấy API key miễn phí (100 searches/month) tại: serpapi.com/manage-api-key

### Cấu trúc scripts

```
seo-workspace/
├── scripts/
│   └── serpapi_helpers.py   ← Tất cả helper functions
├── .env                      ← API key (KHÔNG commit lên git)
└── ...
```

---

## 2. API #1: Google Search API

**Skill sử dụng:** `serp-analysis`, `rank-tracker`, `competitor-analysis`

**Endpoint:** `https://serpapi.com/search?engine=google`

**Tại sao tiết kiệm token nhiều nhất:** Thay vì Claude đoán top 10 SERP, API trả về toàn bộ kết quả thực tế gồm: organic results, People Also Ask, Related Searches, Featured Snippet, Local Pack, Shopping — Claude chỉ cần tóm tắt và phân tích.

### Dữ liệu trả về (JSON)

```json
{
  "organic_results": [
    {
      "position": 1,
      "title": "...",
      "link": "https://...",
      "snippet": "...",
      "displayed_link": "...",
      "date": "..."
    }
  ],
  "people_also_ask": [
    { "question": "...", "snippet": "...", "link": "..." }
  ],
  "related_searches": [
    { "query": "..." }
  ],
  "featured_snippet": {
    "title": "...",
    "snippet": "...",
    "link": "..."
  },
  "local_results": { ... },
  "knowledge_graph": { ... },
  "ads": [ ... ]
}
```

### Code mẫu

```python
from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_serp(keyword: str, market: str = "vn", lang: str = "vi", num: int = 10) -> dict:
    """
    Fetch SERP data cho một keyword.
    Dùng cho: serp-analysis, rank-tracker, competitor-analysis
    """
    params = {
        "engine": "google",
        "q": keyword,
        "gl": market,       # vn = Việt Nam, us = USA
        "hl": lang,         # vi = tiếng Việt
        "num": num,
        "device": "desktop",
        "api_key": os.getenv("SERPAPI_KEY")
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    # Trích xuất data cần thiết, bỏ metadata thừa
    return {
        "keyword": keyword,
        "organic_results": results.get("organic_results", []),
        "people_also_ask": results.get("people_also_ask", []),
        "related_searches": results.get("related_searches", []),
        "featured_snippet": results.get("answer_box") or results.get("featured_snippet"),
        "local_results": results.get("local_results"),
        "has_shopping": bool(results.get("shopping_results")),
        "has_video": bool(results.get("inline_videos")),
        "has_news": bool(results.get("news_results")),
        "total_results": results.get("search_information", {}).get("total_results")
    }
```

### Cách dùng với skill

```python
# Cách 1: Gọi trực tiếp và paste output vào skill
data = fetch_serp("SEO kỹ thuật là gì")
# Paste `data` vào prompt: "Chạy serp-analysis với dữ liệu sau: {data}"

# Cách 2: Check rank của một domain
def check_ranking(keyword: str, domain: str, market: str = "vn") -> dict:
    """
    Kiểm tra vị trí ranking của domain cho keyword.
    Dùng cho: rank-tracker
    """
    data = fetch_serp(keyword, market=market, num=20)
    position = None
    ranking_url = None

    for result in data["organic_results"]:
        if domain in result.get("link", ""):
            position = result["position"]
            ranking_url = result["link"]
            break

    return {
        "keyword": keyword,
        "domain": domain,
        "position": position,          # None nếu không có trong top 20
        "ranking_url": ranking_url,
        "top_competitor": data["organic_results"][0]["link"] if data["organic_results"] else None
    }
```

### Dùng cho competitor-analysis

```python
def get_competitor_pages(competitor_domain: str, limit: int = 20) -> list:
    """
    Lấy các trang đã index của đối thủ.
    Dùng cho: competitor-analysis
    """
    params = {
        "engine": "google",
        "q": f"site:{competitor_domain}",
        "num": limit,
        "api_key": os.getenv("SERPAPI_KEY")
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return [
        {"url": r["link"], "title": r["title"], "snippet": r.get("snippet", "")}
        for r in results.get("organic_results", [])
    ]
```

---

## 3. API #2: Google Autocomplete API

**Skill sử dụng:** `keyword-research`, `topical-map-builder`

**Endpoint:** `https://serpapi.com/search?engine=google_autocomplete`

**Tại sao tiết kiệm token:** Thay thế bước Claude tự sinh từ khóa gợi ý (tốn nhiều token, kém chính xác). Autocomplete trả về từ khóa người dùng thực sự đang gõ + relevance score.

### Dữ liệu trả về

```json
{
  "suggestions": [
    { "value": "seo kỹ thuật là gì", "relevance": 600 },
    { "value": "seo kỹ thuật gồm những gì", "relevance": 550 },
    { "value": "seo kỹ thuật khác gì với seo nội dung", "relevance": 500 }
  ]
}
```

### Code mẫu

```python
def expand_keywords(seed_keyword: str, market: str = "vn", lang: str = "vi") -> list:
    """
    Mở rộng từ khóa từ seed keyword dùng Google Autocomplete.
    Dùng cho: keyword-research, topical-map-builder
    """
    params = {
        "engine": "google_autocomplete",
        "q": seed_keyword,
        "gl": market,
        "hl": lang,
        "api_key": os.getenv("SERPAPI_KEY")
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    suggestions = results.get("suggestions", [])
    return [
        {
            "keyword": s["value"],
            "relevance": s.get("relevance", 0)
        }
        for s in suggestions
        if s["value"] != seed_keyword  # bỏ seed keyword khỏi list
    ]


def bulk_expand_keywords(seed_keywords: list, market: str = "vn") -> dict:
    """
    Mở rộng nhiều seed keywords cùng lúc.
    Dùng cho: topical-map-builder (expand sub-topics)
    """
    all_keywords = {}
    for seed in seed_keywords:
        suggestions = expand_keywords(seed, market=market)
        all_keywords[seed] = suggestions
        # Thêm variations: "[seed] là gì", "cách [seed]", "[seed] tốt nhất"
        for prefix in [f"{seed} là gì", f"cách {seed}", f"{seed} hiệu quả"]:
            extra = expand_keywords(prefix, market=market)
            all_keywords[seed].extend(extra)

    return all_keywords
```

### Cách dùng với skill

```python
# keyword-research: expand từ 1 seed keyword
seeds = expand_keywords("SEO website")
# Output: [{"keyword": "seo website là gì", "relevance": 600}, ...]
# Paste vào prompt: "Chạy keyword-research với danh sách từ khóa sau: {seeds}"

# topical-map-builder: expand nhiều main topics
main_topics = ["SEO kỹ thuật", "SEO nội dung", "SEO off-page", "SEO local"]
subtopics = bulk_expand_keywords(main_topics)
# Paste vào prompt: "Chạy topical-map-builder, dùng sub-topics sau thay vì tự sinh: {subtopics}"
```

---

## 4. API #3: Google Trends API

**Skill sử dụng:** `keyword-research`, `algorithm-update-monitor`

**Endpoint:** `https://serpapi.com/search?engine=google_trends`

**Tại sao tiết kiệm token:** Cung cấp số liệu trend thực tế (0-100), related queries rising — thay vì Claude phỏng đoán "từ khóa X có thể đang trending".

### Code mẫu

```python
def get_keyword_trends(keywords: list, date_range: str = "today 12-m",
                        market: str = "VN") -> dict:
    """
    Lấy trend data cho 1-5 keywords.
    Dùng cho: keyword-research (so sánh volume trend giữa các từ khóa)

    date_range options:
        "now 1-H"     = 1 giờ gần nhất
        "now 7-d"     = 7 ngày gần nhất
        "today 1-m"   = 1 tháng gần nhất
        "today 12-m"  = 12 tháng gần nhất (default)
        "today 5-y"   = 5 năm gần nhất
    """
    params = {
        "engine": "google_trends",
        "q": ",".join(keywords[:5]),   # tối đa 5 keywords
        "data_type": "TIMESERIES",
        "date": date_range,
        "geo": market,
        "api_key": os.getenv("SERPAPI_KEY")
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("interest_over_time", {})


def get_related_queries(keyword: str, market: str = "VN") -> dict:
    """
    Lấy related queries (top + rising) cho một keyword.
    Dùng cho: topical-map-builder (tìm subtopics đang nổi)
    Rising queries = cơ hội SEO — chưa cạnh tranh cao nhưng đang tăng.
    """
    params = {
        "engine": "google_trends",
        "q": keyword,
        "data_type": "RELATED_QUERIES",
        "geo": market,
        "api_key": os.getenv("SERPAPI_KEY")
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    related = results.get("related_queries", {})
    return {
        "top_queries": related.get("top", []),      # Phổ biến nhất
        "rising_queries": related.get("rising", []) # Đang tăng mạnh → cơ hội
    }


def detect_traffic_anomaly(keyword: str, market: str = "VN") -> dict:
    """
    Phát hiện biến động traffic bất thường (dùng cho algorithm-update-monitor).
    So sánh 3 tháng gần nhất vs 3 tháng trước đó.
    """
    params = {
        "engine": "google_trends",
        "q": keyword,
        "data_type": "TIMESERIES",
        "date": "today 12-m",
        "geo": market,
        "api_key": os.getenv("SERPAPI_KEY")
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    timeline = results.get("interest_over_time", {}).get("timeline_data", [])
    if not timeline:
        return {"error": "No data"}

    # So sánh nửa cuối vs nửa đầu
    mid = len(timeline) // 2
    recent_avg = sum(p["values"][0]["extracted_value"] for p in timeline[mid:]) / max(len(timeline[mid:]), 1)
    older_avg = sum(p["values"][0]["extracted_value"] for p in timeline[:mid]) / max(mid, 1)
    change_pct = ((recent_avg - older_avg) / max(older_avg, 1)) * 100

    return {
        "keyword": keyword,
        "recent_avg_interest": round(recent_avg, 1),
        "older_avg_interest": round(older_avg, 1),
        "change_percent": round(change_pct, 1),
        "trend": "tăng" if change_pct > 10 else "giảm" if change_pct < -10 else "ổn định"
    }
```

---

## 5. API #4: Google Local API

**Skill sử dụng:** `serp-analysis` (khi keyword có local intent)

**Endpoint:** `https://serpapi.com/search?engine=google_local`

### Code mẫu

```python
def fetch_local_pack(keyword: str, location: str = "Ho Chi Minh City, Vietnam") -> list:
    """
    Lấy Local Pack results (3 kết quả bản đồ).
    Dùng cho: serp-analysis khi keyword có local intent.
    """
    params = {
        "engine": "google_local",
        "q": keyword,
        "location": location,
        "hl": "vi",
        "api_key": os.getenv("SERPAPI_KEY")
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    return [
        {
            "name": r.get("title"),
            "rating": r.get("rating"),
            "reviews": r.get("reviews"),
            "address": r.get("address"),
            "hours": r.get("hours"),
            "type": r.get("type")
        }
        for r in results.get("local_results", [])
    ]
```

---

## 6. API #5: Google News API

**Skill sử dụng:** `algorithm-update-monitor`

**Endpoint:** `https://serpapi.com/search?engine=google_news`

### Code mẫu

```python
def fetch_algorithm_update_news(days_back: int = 30) -> list:
    """
    Lấy tin tức về Google algorithm updates gần đây.
    Dùng cho: algorithm-update-monitor
    """
    from datetime import datetime, timedelta

    params = {
        "engine": "google",
        "q": "Google algorithm update site:searchengineland.com OR site:seroundtable.com OR site:developers.google.com",
        "tbm": "nws",      # news search
        "tbs": f"qdr:m",   # trong 1 tháng gần nhất
        "num": 20,
        "api_key": os.getenv("SERPAPI_KEY")
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    return [
        {
            "title": r.get("title"),
            "link": r.get("link"),
            "date": r.get("date"),
            "source": r.get("source"),
            "snippet": r.get("snippet")
        }
        for r in results.get("news_results", [])
    ]
```

---

## 7. Workflow tổng hợp — Chạy trước khi gọi skill

Đây là script chạy trước để thu thập đủ dữ liệu, sau đó paste vào skill một lần duy nhất:

### Workflow A: Chuẩn bị cho `keyword-research`

```python
def prepare_keyword_research(seed_keyword: str, market: str = "vn") -> dict:
    """
    Thu thập đủ data để chạy keyword-research với Claude.
    Giảm từ ~5-8 lượt hỏi xuống còn 1 lượt.
    """
    print(f"Đang thu thập data cho: {seed_keyword}")

    # 1. Autocomplete suggestions
    suggestions = expand_keywords(seed_keyword, market=market)

    # 2. Thêm variations phổ biến
    variations = []
    for prefix in [f"{seed_keyword} là gì", f"cách {seed_keyword}", f"{seed_keyword} tốt nhất"]:
        variations += expand_keywords(prefix, market=market)

    # 3. Trend data
    top_keywords = [s["keyword"] for s in suggestions[:5]]
    if top_keywords:
        trends = get_keyword_trends([seed_keyword] + top_keywords[:4], market=market.upper())
    else:
        trends = {}

    # 4. Related rising queries
    rising = get_related_queries(seed_keyword, market=market.upper())

    return {
        "seed_keyword": seed_keyword,
        "autocomplete_suggestions": suggestions,
        "keyword_variations": variations[:20],
        "trends": trends,
        "rising_queries": rising["rising_queries"][:10],
        "top_queries": rising["top_queries"][:10]
    }
```

### Workflow B: Chuẩn bị cho `serp-analysis`

```python
def prepare_serp_analysis(keyword: str, market: str = "vn") -> dict:
    """
    Thu thập SERP data đầy đủ để chạy serp-analysis với Claude.
    """
    print(f"Đang fetch SERP cho: {keyword}")

    serp_data = fetch_serp(keyword, market=market)

    # Rút gọn organic results để tiết kiệm token
    compact_results = [
        {
            "position": r["position"],
            "title": r.get("title", ""),
            "url": r.get("link", ""),
            "snippet": r.get("snippet", "")[:200],   # cắt ngắn snippet
            "domain": r.get("displayed_link", "")
        }
        for r in serp_data["organic_results"]
    ]

    return {
        "keyword": keyword,
        "top_10": compact_results,
        "people_also_ask": [q["question"] for q in serp_data.get("people_also_ask", [])],
        "related_searches": [r["query"] for r in serp_data.get("related_searches", [])],
        "has_featured_snippet": bool(serp_data.get("featured_snippet")),
        "has_local_pack": bool(serp_data.get("local_results")),
        "has_shopping": serp_data.get("has_shopping", False),
        "has_video": serp_data.get("has_video", False),
        "has_news": serp_data.get("has_news", False)
    }
```

### Workflow C: Chuẩn bị cho `rank-tracker` (nhiều keywords)

```python
def prepare_rank_tracker(keywords: list, domain: str, market: str = "vn") -> list:
    """
    Kiểm tra ranking cho danh sách keywords.
    """
    results = []
    for kw in keywords:
        print(f"Checking rank: {kw}")
        rank_data = check_ranking(kw, domain, market=market)
        results.append(rank_data)

    return results
```

---

## 8. Cách dùng với Claude Code

### Bước 1: Chạy script Python thu thập data

```bash
cd "D:\Claude Code\seo-workspace"
python scripts/serpapi_helpers.py
```

Hoặc import vào Python script của bạn:

```python
from scripts.serpapi_helpers import prepare_serp_analysis, prepare_keyword_research

# Thu thập data
data = prepare_serp_analysis("SEO kỹ thuật là gì")
```

### Bước 2: Paste output vào Claude Code

```
Chạy serp-analysis với dữ liệu SerpAPI sau:

[paste JSON output từ script]

Phân tích và đưa ra SERP report + gợi ý content format.
```

### Bước 3: Claude chỉ phân tích, không phải suy diễn

Claude nhận dữ liệu thực → chỉ cần tóm tắt, phân tích intent, đưa ra kết luận → **ít token hơn 50-70%** so với Claude tự suy diễn từ đầu.

---

## 9. Lưu ý quan trọng

### Tiết kiệm credits SerpAPI
- **Cached searches miễn phí** — SerpAPI cache kết quả 1 giờ. Cùng query trong 1 giờ không tốn credit.
- Dùng `num=10` thay vì `num=100` khi chỉ cần top 10.
- Dùng `Google Light Search API` (`engine=google_light`) cho quick checks — rẻ hơn.

### Bảo mật API Key
- Không commit `.env` lên git → thêm `.env` vào `.gitignore`
- Không hardcode API key trong source code

### Rate limits
- Free tier: 100 searches/tháng
- Paid plans: từ $50/tháng cho 5.000 searches
- Implement sleep giữa các calls khi bulk fetch:
  ```python
  import time
  time.sleep(1)  # 1 giây giữa các calls
  ```

---

## 10. Mapping API → Skill (tóm tắt nhanh)

| Skill | API cần dùng | Function |
|-------|-------------|---------|
| `keyword-research` | Autocomplete + Trends | `prepare_keyword_research()` |
| `serp-analysis` | Google Search | `prepare_serp_analysis()` |
| `topical-map-builder` | Autocomplete + Trends (related queries) | `bulk_expand_keywords()` + `get_related_queries()` |
| `competitor-analysis` | Google Search (`site:`) | `get_competitor_pages()` |
| `rank-tracker` | Google Search | `prepare_rank_tracker()` |
| `algorithm-update-monitor` | Trends + Google News | `detect_traffic_anomaly()` + `fetch_algorithm_update_news()` |
