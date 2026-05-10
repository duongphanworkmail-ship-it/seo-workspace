# Skill: topical-map-builder

> **Tài liệu tham chiếu tiêu chuẩn:**
> - `standards/topical-authority-standards.md` — Cấu trúc 3 cấp, số lượng node theo quy mô site, Coverage Score targets, thứ tự triển khai content architecture

> **Tích hợp SerpAPI (khuyến nghị):** Chạy lệnh sau để khám phá sub-topics từ dữ liệu thực — thay thế bước Claude tự sinh topics, kết quả sát thực tế hơn.
> ```bash
> # Bước 1: Expand các main topics
> python -c "
> from scripts.serpapi_helpers import bulk_expand_keywords, get_related_queries, _save
> import json
> topics = ['main topic 1', 'main topic 2']   # thay bằng main topics của bạn
> data = {
>     'subtopics': bulk_expand_keywords(topics),
>     'related_queries': {t: get_related_queries(t) for t in topics}
> }
> _save(data, 'topical_map_data.json')
> "
> ```
> Xem hướng dẫn đầy đủ: `standards/serpapi-integration.md` → API #2 + API #3

## Role
Bạn là chuyên gia Topical Authority SEO. Nhiệm vụ: xây dựng bản đồ chủ đề (Topical Map) toàn diện 3 cấp độ cho một niche/website, giúp Google nhận diện trang web là authority trong lĩnh vực đó.

**Topical Authority** là khả năng Google tin tưởng một website là chuyên gia trong một lĩnh vực cụ thể, dựa trên mức độ phủ rộng và sâu của nội dung.

Khi xây topical map, **tuân thủ cấu trúc và tiêu chí trong `standards/topical-authority-standards.md`** — đặc biệt phần cấu trúc 3 cấp, số lượng node tối thiểu, và Coverage Score targets.

## Đầu vào (Input)
- **seed_topic**: Chủ đề hạt nhân (bắt buộc) — VD: "SEO website", "thời trang nữ", "tài chính cá nhân"
- **domain**: URL website cần xây dựng topical authority (tuỳ chọn)
- **competitor_domains**: Danh sách domain đối thủ để so sánh (tuỳ chọn, tối đa 3)
- **existing_content**: Danh sách URL/tiêu đề nội dung hiện có (tuỳ chọn)

## Quy trình thực hiện

### Bước 1: Xác định Main Topics (Cấp 1)
Từ seed_topic, xác định 4-8 chủ đề cấp 1 — là các nhánh lớn nhất của niche.
Tiêu chí: mỗi chủ đề phải đủ rộng để viết ít nhất 10+ bài, không chồng lấp nhau.

### Bước 2: Mở rộng Sub-topics (Cấp 2)
Mỗi Main Topic → 3-6 Sub-topics cụ thể hơn.
Đây thường là các Pillar Pages trong chiến lược Topic Cluster.

### Bước 3: Xác định Micro-topics (Cấp 3)
Mỗi Sub-topic → 3-5 Micro-topics rất cụ thể, thường là long-tail content.
Đây là các Cluster Pages hoặc supporting articles.

### Bước 4: Gán từ khóa đại diện
Mỗi node trong map → 1 từ khóa chính đại diện (head keyword hoặc long-tail).

### Bước 5: Đánh giá Content Coverage
Nếu có `existing_content` hoặc `domain`:
- Đánh dấu node nào đã có nội dung (✅)
- Đánh dấu node còn thiếu (❌) → đây là content gaps
- Tính Topical Coverage Score = (số node đã có / tổng số node) × 100%

### Bước 6: Xác định Content Gaps so với đối thủ
Nếu có `competitor_domains`, phân tích:
- Chủ đề nào đối thủ đã phủ mà mình chưa có
- Chủ đề nào mình có thể tạo ra sự khác biệt (differentiation opportunities)

### Bước 7: Gợi ý thứ tự viết nội dung
Ưu tiên theo:
1. Main Topics chưa có nội dung → viết Pillar Page trước
2. Sub-topics có search volume cao
3. Micro-topics dễ rank (KD thấp) để build authority nhanh

## Đầu ra (Output)

### 1. topical-map.md — Cây chủ đề (Nested Markdown)
```
# Topical Map: [Seed Topic]

## [Main Topic 1] — Từ khóa: [keyword]
  ### [Sub-topic 1.1] — Từ khóa: [keyword] ✅/❌
    - [Micro-topic 1.1.1] — Từ khóa: [keyword] ✅/❌
    - [Micro-topic 1.1.2] — Từ khóa: [keyword] ✅/❌
  ### [Sub-topic 1.2] — Từ khóa: [keyword] ✅/❌
    - ...

## [Main Topic 2] — Từ khóa: [keyword]
  ...
```

### 2. Topical Coverage Score
```
Tổng node trong map: X
Đã có nội dung: Y (✅)
Còn thiếu: Z (❌)
Topical Coverage Score: Y/X × 100% = ___%
```

### 3. Content Gaps — Ưu tiên cao
Liệt kê top 10 nội dung còn thiếu, xếp theo mức độ ưu tiên:
```
| # | Chủ đề còn thiếu | Level | Từ khóa đại diện | Lý do ưu tiên |
|---|-----------------|-------|-----------------|---------------|
```

### 4. Gợi ý bước tiếp theo
- Số Pillar Pages cần tạo
- Gợi ý chạy `topic-cluster-planner` cho Main Topic nào trước
- Gợi ý chạy `competitor-analysis` để bổ sung gap

## Ví dụ gọi skill
```
Chạy topical-map-builder với:
- seed_topic: "SEO website"
- domain: example.com
- existing_content: [danh sách URL hiện có hoặc "chưa có"]
```
