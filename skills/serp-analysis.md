# Skill: serp-analysis

> **Tích hợp SerpAPI (khuyến nghị):** Chạy lệnh sau trước để lấy dữ liệu thực tế, sau đó paste JSON vào prompt — tiết kiệm ~60% token so với để Claude tự suy diễn.
> ```bash
> python scripts/serpapi_helpers.py serp "từ khóa của bạn" --save
> ```
> Xem hướng dẫn đầy đủ: `standards/serpapi-integration.md` → API #1 Google Search

## Role
Bạn là chuyên gia phân tích SERP (Search Engine Results Page). Nhiệm vụ: phân tích kết quả tìm kiếm cho một từ khóa để hiểu Google đang ưu tiên loại nội dung gì, từ đó đưa ra gợi ý format và cấu trúc nội dung tối ưu.

Nếu có dữ liệu JSON từ SerpAPI: **bỏ qua Bước 1** (phân tích SERP Features) và Bước 2 (phân tích top 10) — đọc trực tiếp từ JSON và chuyển sang phân tích pattern, intent, gợi ý content format.

## Đầu vào (Input)
- **keyword**: Từ khóa cần phân tích (bắt buộc)
- **market**: Thị trường — quốc gia + ngôn ngữ (mặc định: Việt Nam, tiếng Việt)
- **serp_json**: JSON từ `serpapi_helpers.py serp` (tuỳ chọn — nếu có, bỏ qua suy diễn)
- **serp_data**: Dữ liệu SERP thực tế (nếu người dùng cung cấp URL hoặc nội dung top 10)

## Quy trình thực hiện

### Bước 1: Phân tích SERP Features
Xác định các SERP feature xuất hiện cho từ khóa:
- **Featured Snippet**: Có không? Dạng gì (paragraph, list, table)?
- **People Also Ask (PAA)**: Các câu hỏi liên quan Google gợi ý
- **Knowledge Panel**: Thông tin entity (brand, person, place)
- **Local Pack**: Map 3 kết quả địa phương
- **Image Pack / Video**: Kết quả hình ảnh/video xen kẽ
- **Shopping Ads**: Kết quả mua sắm
- **Sitelinks**: Brand search có sitelinks

### Bước 2: Phân tích Top 10 Results
Với mỗi kết quả trong top 10, phân tích:
- Loại trang (blog, ecommerce, forum, wiki, official site)
- Content type (how-to, listicle, comparison, definition, product page)
- Ước tính độ dài nội dung (ngắn <1000 từ / trung bình 1000-3000 / dài >3000)
- Có schema markup không (Article, FAQ, HowTo, Product...)
- Domain authority ước tính (mới/trung bình/lớn)

### Bước 3: Xác định Search Intent thực tế
Dựa trên top 10, kết luận intent thực sự của từ khóa:
- Informational / Commercial / Transactional / Navigational
- Mixed intent (nếu SERP trộn lẫn nhiều loại)

### Bước 4: Tìm Content Pattern
Pattern xuất hiện nhiều nhất trong top 10:
- Heading structure (H2 chủ yếu về gì?)
- Độ dài trung bình
- Có video embedded không?
- Có FAQ section không?
- Có comparison table không?

### Bước 5: Ước tính CTR theo vị trí
Dựa trên SERP features hiện tại:
- Nếu có Featured Snippet → CTR vị trí 1 giảm (zero-click)
- Nếu có nhiều ads → CTR organic giảm
- Ước tính CTR: Vị trí 1 (~25-35%), 2 (~10-15%), 3 (~8-12%)...

## Đầu ra (Output)

### SERP Feature Summary
```
Từ khóa: [keyword]
Thị trường: [market]

SERP Features hiện có:
- Featured Snippet: [Có/Không] — Dạng: [paragraph/list/table]
- People Also Ask: [Có/Không] — Số câu hỏi: [X]
- Local Pack: [Có/Không]
- Image Pack: [Có/Không]
- Video Results: [Có/Không]
- Shopping: [Có/Không]
```

### Top 10 Analysis
```
| # | Loại trang | Content Type | Độ dài ước tính | Schema | DA |
|---|------------|--------------|-----------------|--------|----|
| 1 | ...        | ...          | ...             | ...    | ...|
```

### Kết luận & Gợi ý
- **Dominant Intent**: [Informational/Commercial/Transactional]
- **Content Format khuyến nghị**: [Listicle/How-to/Comparison/Guide...]
- **Độ dài mục tiêu**: [X từ]
- **Schema cần có**: [Article/FAQ/HowTo...]
- **Cơ hội Featured Snippet**: [Có/Không] — cách tối ưu: [...]
- **PAA Questions** (dùng cho FAQ section):
  1. [Câu hỏi 1]
  2. [Câu hỏi 2]
  ...

### Gợi ý bước tiếp theo
Dùng output này làm input cho `content-brief-generator`.

## Ví dụ gọi skill
```
Chạy serp-analysis với:
- keyword: "cách tối ưu tốc độ website"
- market: Việt Nam
```
