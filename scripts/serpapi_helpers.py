"""
SerpAPI Helpers — SEO Workspace
Chạy: python scripts/serpapi_helpers.py --help
Yêu cầu: pip install google-search-results python-dotenv
API Key: thêm SERPAPI_KEY=... vào file .env
"""

import os
import json
import time
import argparse
from dotenv import load_dotenv

load_dotenv()

try:
    from serpapi import GoogleSearch
except ImportError:
    print("Thiếu thư viện: pip install google-search-results")
    raise


# ─────────────────────────────────────────────
# Core helpers
# ─────────────────────────────────────────────

def _api_key() -> str:
    key = os.getenv("SERPAPI_KEY")
    if not key:
        raise EnvironmentError("Thiếu SERPAPI_KEY trong file .env")
    return key


def _search(params: dict) -> dict:
    params["api_key"] = _api_key()
    result = GoogleSearch(params).get_dict()
    time.sleep(0.5)  # tránh rate limit khi bulk
    return result


def _save(data: dict, filename: str) -> None:
    path = os.path.join("output", filename)
    os.makedirs("output", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Đã lưu: {path}")


# ─────────────────────────────────────────────
# API #1: Google Search
# Dùng cho: serp-analysis, rank-tracker, competitor-analysis
# ─────────────────────────────────────────────

def fetch_serp(keyword: str, market: str = "vn", lang: str = "vi", num: int = 10) -> dict:
    """Fetch SERP data thực tế cho keyword."""
    result = _search({
        "engine": "google",
        "q": keyword,
        "gl": market,
        "hl": lang,
        "num": num,
        "device": "desktop",
    })

    # Compact organic results — chỉ giữ field cần thiết
    organic = [
        {
            "position": r.get("position"),
            "title": r.get("title", ""),
            "url": r.get("link", ""),
            "domain": r.get("displayed_link", ""),
            "snippet": (r.get("snippet") or "")[:200],
            "date": r.get("date", ""),
        }
        for r in result.get("organic_results", [])
    ]

    return {
        "keyword": keyword,
        "market": market,
        "total_results": result.get("search_information", {}).get("total_results"),
        "organic_results": organic,
        "people_also_ask": [
            q.get("question") for q in result.get("people_also_ask", [])
        ],
        "related_searches": [
            r.get("query") for r in result.get("related_searches", [])
        ],
        "featured_snippet": result.get("answer_box") or result.get("featured_snippet"),
        "has_local_pack": bool(result.get("local_results")),
        "has_shopping": bool(result.get("shopping_results")),
        "has_video": bool(result.get("inline_videos")),
        "has_news": bool(result.get("news_results")),
    }


def check_ranking(keyword: str, domain: str, market: str = "vn", top_n: int = 20) -> dict:
    """Kiểm tra vị trí ranking của domain cho keyword. Dùng cho rank-tracker."""
    result = _search({
        "engine": "google",
        "q": keyword,
        "gl": market,
        "num": top_n,
        "device": "desktop",
    })

    position = None
    ranking_url = None
    for r in result.get("organic_results", []):
        if domain.lower() in r.get("link", "").lower():
            position = r["position"]
            ranking_url = r["link"]
            break

    return {
        "keyword": keyword,
        "domain": domain,
        "position": position,
        "ranking_url": ranking_url,
        "in_top_n": top_n,
        "top_result": result.get("organic_results", [{}])[0].get("link"),
    }


def get_competitor_pages(competitor_domain: str, limit: int = 20) -> list:
    """Lấy trang đã index của đối thủ qua site: query. Dùng cho competitor-analysis."""
    result = _search({
        "engine": "google",
        "q": f"site:{competitor_domain}",
        "num": limit,
    })
    return [
        {
            "url": r.get("link"),
            "title": r.get("title"),
            "snippet": (r.get("snippet") or "")[:150],
        }
        for r in result.get("organic_results", [])
    ]


# ─────────────────────────────────────────────
# API #2: Google Autocomplete
# Dùng cho: keyword-research, topical-map-builder
# ─────────────────────────────────────────────

def expand_keywords(seed_keyword: str, market: str = "vn", lang: str = "vi") -> list:
    """Mở rộng từ khóa qua Google Autocomplete. Dùng cho keyword-research."""
    result = _search({
        "engine": "google_autocomplete",
        "q": seed_keyword,
        "gl": market,
        "hl": lang,
    })
    return [
        {"keyword": s.get("value", ""), "relevance": s.get("relevance", 0)}
        for s in result.get("suggestions", [])
        if s.get("value", "").strip().lower() != seed_keyword.strip().lower()
    ]


def bulk_expand_keywords(main_topics: list, market: str = "vn") -> dict:
    """
    Mở rộng nhiều main topics cùng lúc.
    Dùng cho: topical-map-builder để tự động khám phá sub-topics.
    """
    all_keywords: dict = {}
    for topic in main_topics:
        print(f"  Expanding: {topic}")
        suggestions = expand_keywords(topic, market=market)
        variations: list = []
        for prefix in [f"{topic} là gì", f"cách {topic}", f"{topic} tốt nhất"]:
            variations += expand_keywords(prefix, market=market)
        # Merge + dedup by keyword value
        seen: set = set()
        merged = []
        for item in suggestions + variations:
            kw = item["keyword"]
            if kw not in seen:
                seen.add(kw)
                merged.append(item)
        all_keywords[topic] = sorted(merged, key=lambda x: x["relevance"], reverse=True)
    return all_keywords


# ─────────────────────────────────────────────
# API #3: Google Trends
# Dùng cho: keyword-research, algorithm-update-monitor
# ─────────────────────────────────────────────

def get_keyword_trends(keywords: list, date_range: str = "today 12-m",
                       market: str = "VN") -> dict:
    """
    Trend data cho 1-5 keywords theo thời gian.
    Dùng cho: keyword-research — so sánh xu hướng các từ khóa.

    date_range options: "now 7-d", "today 1-m", "today 12-m", "today 5-y"
    """
    result = _search({
        "engine": "google_trends",
        "q": ",".join(keywords[:5]),
        "data_type": "TIMESERIES",
        "date": date_range,
        "geo": market,
    })
    timeline = result.get("interest_over_time", {}).get("timeline_data", [])
    if not timeline:
        return {"keywords": keywords, "data": []}

    return {
        "keywords": keywords,
        "period": date_range,
        "data": [
            {
                "date": point.get("date"),
                "values": {
                    keywords[i]: v.get("extracted_value", 0)
                    for i, v in enumerate(point.get("values", []))
                    if i < len(keywords)
                },
            }
            for point in timeline
        ],
    }


def get_related_queries(keyword: str, market: str = "VN") -> dict:
    """
    Related queries (top + rising) cho keyword.
    Dùng cho: topical-map-builder — rising queries = cơ hội SEO chưa cạnh tranh cao.
    """
    result = _search({
        "engine": "google_trends",
        "q": keyword,
        "data_type": "RELATED_QUERIES",
        "geo": market,
    })
    related = result.get("related_queries", {})
    return {
        "keyword": keyword,
        "top_queries": [
            {"query": q.get("query"), "value": q.get("extracted_value")}
            for q in related.get("top", [])
        ],
        "rising_queries": [
            {"query": q.get("query"), "change": q.get("extracted_value")}
            for q in related.get("rising", [])
        ],
    }


def detect_traffic_anomaly(keyword: str, market: str = "VN") -> dict:
    """
    Phát hiện biến động traffic bất thường theo trend.
    Dùng cho: algorithm-update-monitor — so sánh 6 tháng gần nhất vs 6 tháng trước.
    """
    result = _search({
        "engine": "google_trends",
        "q": keyword,
        "data_type": "TIMESERIES",
        "date": "today 12-m",
        "geo": market,
    })
    timeline = result.get("interest_over_time", {}).get("timeline_data", [])
    if not timeline:
        return {"keyword": keyword, "error": "No trend data"}

    mid = len(timeline) // 2
    recent = [p["values"][0]["extracted_value"] for p in timeline[mid:] if p.get("values")]
    older = [p["values"][0]["extracted_value"] for p in timeline[:mid] if p.get("values")]

    recent_avg = sum(recent) / max(len(recent), 1)
    older_avg = sum(older) / max(len(older), 1)
    change_pct = ((recent_avg - older_avg) / max(older_avg, 1)) * 100

    return {
        "keyword": keyword,
        "recent_6m_avg": round(recent_avg, 1),
        "older_6m_avg": round(older_avg, 1),
        "change_percent": round(change_pct, 1),
        "trend": "tăng" if change_pct > 10 else "giảm" if change_pct < -10 else "ổn định",
    }


# ─────────────────────────────────────────────
# API #4: Google Local
# Dùng cho: serp-analysis (local intent)
# ─────────────────────────────────────────────

def fetch_local_pack(keyword: str, location: str = "Ho Chi Minh City, Vietnam",
                     lang: str = "vi") -> list:
    """Lấy Local Pack (3 kết quả bản đồ). Dùng cho serp-analysis local intent."""
    result = _search({
        "engine": "google_local",
        "q": keyword,
        "location": location,
        "hl": lang,
    })
    return [
        {
            "name": r.get("title"),
            "rating": r.get("rating"),
            "reviews": r.get("reviews"),
            "address": r.get("address"),
            "type": r.get("type"),
            "hours": r.get("hours"),
        }
        for r in result.get("local_results", [])
    ]


# ─────────────────────────────────────────────
# API #5: Google News
# Dùng cho: algorithm-update-monitor
# ─────────────────────────────────────────────

def fetch_algorithm_update_news() -> list:
    """Lấy tin tức Google algorithm updates gần nhất. Dùng cho algorithm-update-monitor."""
    result = _search({
        "engine": "google",
        "q": (
            "Google algorithm update "
            "site:searchengineland.com OR site:seroundtable.com "
            "OR site:developers.google.com/search/blog"
        ),
        "tbm": "nws",
        "tbs": "qdr:m",   # 1 tháng gần nhất
        "num": 15,
    })
    return [
        {
            "title": r.get("title"),
            "link": r.get("link"),
            "date": r.get("date"),
            "source": r.get("source"),
            "snippet": (r.get("snippet") or "")[:200],
        }
        for r in result.get("news_results", [])
    ]


# ─────────────────────────────────────────────
# Workflow functions — chuẩn bị data cho từng skill
# ─────────────────────────────────────────────

def prepare_keyword_research(seed_keyword: str, market: str = "vn") -> dict:
    """
    Thu thập đủ data để chạy skill keyword-research với Claude.
    Giảm từ ~5-8 lượt hỏi xuống còn 1 lượt.
    """
    print(f"\n[keyword-research] Đang thu thập data cho: {seed_keyword}")

    print("  → Autocomplete suggestions...")
    suggestions = expand_keywords(seed_keyword, market=market)

    print("  → Keyword variations...")
    variations: list = []
    for prefix in [f"{seed_keyword} là gì", f"cách {seed_keyword}", f"{seed_keyword} tốt nhất"]:
        variations += expand_keywords(prefix, market=market)

    print("  → Trend data...")
    top_kws = [s["keyword"] for s in suggestions[:4]]
    trends = get_keyword_trends([seed_keyword] + top_kws, market=market.upper()) if top_kws else {}

    print("  → Related queries...")
    rising_data = get_related_queries(seed_keyword, market=market.upper())

    return {
        "seed_keyword": seed_keyword,
        "autocomplete_suggestions": suggestions,
        "keyword_variations": variations[:20],
        "trends_12m": trends,
        "rising_queries": rising_data["rising_queries"][:10],
        "top_queries": rising_data["top_queries"][:10],
    }


def prepare_serp_analysis(keyword: str, market: str = "vn") -> dict:
    """
    Thu thập SERP data đầy đủ để chạy skill serp-analysis với Claude.
    """
    print(f"\n[serp-analysis] Đang fetch SERP cho: {keyword}")
    return fetch_serp(keyword, market=market)


def prepare_rank_tracker(keywords: list, domain: str, market: str = "vn") -> list:
    """
    Kiểm tra ranking cho danh sách keywords.
    Dùng cho: rank-tracker
    """
    print(f"\n[rank-tracker] Checking {len(keywords)} keywords for: {domain}")
    results = []
    for kw in keywords:
        print(f"  → {kw}")
        results.append(check_ranking(kw, domain, market=market))
    return results


def prepare_algorithm_monitor(keywords: list, domain_niche: str, market: str = "VN") -> dict:
    """
    Thu thập data để chạy skill algorithm-update-monitor.
    """
    print(f"\n[algorithm-update-monitor] Phân tích biến động traffic...")

    print("  → Trend anomalies...")
    anomalies = [detect_traffic_anomaly(kw, market=market) for kw in keywords[:5]]

    print("  → Algorithm update news...")
    news = fetch_algorithm_update_news()

    return {
        "domain_niche": domain_niche,
        "keyword_trend_anomalies": anomalies,
        "recent_google_updates": news[:10],
    }


# ─────────────────────────────────────────────
# CLI — chạy từ terminal
# ─────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="SerpAPI Helpers — Thu thập data cho SEO workspace skills"
    )
    subparsers = parser.add_subparsers(dest="command")

    # serp
    p_serp = subparsers.add_parser("serp", help="Fetch SERP data cho keyword")
    p_serp.add_argument("keyword", help="Từ khóa cần phân tích")
    p_serp.add_argument("--market", default="vn", help="Mã quốc gia (vn, us, ...)")
    p_serp.add_argument("--save", action="store_true", help="Lưu kết quả ra file JSON")

    # keyword
    p_kw = subparsers.add_parser("keyword", help="Chuẩn bị data cho keyword-research")
    p_kw.add_argument("seed", help="Seed keyword")
    p_kw.add_argument("--market", default="vn")
    p_kw.add_argument("--save", action="store_true")

    # rank
    p_rank = subparsers.add_parser("rank", help="Check ranking cho domain")
    p_rank.add_argument("domain", help="Domain cần check (vd: example.com)")
    p_rank.add_argument("keywords", nargs="+", help="Danh sách từ khóa")
    p_rank.add_argument("--market", default="vn")
    p_rank.add_argument("--save", action="store_true")

    # algorithm
    p_algo = subparsers.add_parser("algorithm", help="Phân tích algorithm update impact")
    p_algo.add_argument("niche", help="Niche/domain mô tả")
    p_algo.add_argument("keywords", nargs="+", help="Từ khóa đại diện để check trend")
    p_algo.add_argument("--market", default="VN")
    p_algo.add_argument("--save", action="store_true")

    args = parser.parse_args()

    if args.command == "serp":
        result = prepare_serp_analysis(args.keyword, market=args.market)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if args.save:
            _save(result, f"serp_{args.keyword.replace(' ', '_')}.json")

    elif args.command == "keyword":
        result = prepare_keyword_research(args.seed, market=args.market)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if args.save:
            _save(result, f"keyword_{args.seed.replace(' ', '_')}.json")

    elif args.command == "rank":
        result = prepare_rank_tracker(args.keywords, args.domain, market=args.market)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if args.save:
            _save(result, f"rank_{args.domain}.json")

    elif args.command == "algorithm":
        result = prepare_algorithm_monitor(args.keywords, args.niche, market=args.market)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if args.save:
            _save(result, f"algorithm_{args.niche.replace(' ', '_')}.json")

    else:
        parser.print_help()
