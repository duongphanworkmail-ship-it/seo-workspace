# SEO Workspace — Claude Code

Workspace tự động hóa SEO website. Gồm 11 skill độc lập, có thể chạy riêng lẻ hoặc kết hợp thành pipeline hoàn chỉnh.

## Cách sử dụng skill

Gọi tên skill và cung cấp đầu vào theo format quy định trong file skill tương ứng.

Ví dụ:
- "Chạy keyword-research cho chủ đề: digital marketing, thị trường Việt Nam"
- "Chạy topical-map-builder cho niche: sức khỏe và dinh dưỡng"
- "Chạy topic-cluster-planner cho pillar: SEO kỹ thuật"

---

## Danh sách Skill

### Lớp 1: Nghiên cứu (Research)

| # | Skill | File | Mô tả ngắn |
|---|-------|------|------------|
| 1 | `keyword-research` | skills/keyword-research.md | Tìm & phân nhóm từ khóa theo intent |
| 2 | `topical-map-builder` | skills/topical-map-builder.md | Xây bản đồ chủ đề 3 cấp + coverage score |
| 3 | `topic-cluster-planner` | skills/topic-cluster-planner.md | Thiết kế pillar + cluster + internal linking |
| 4 | `serp-analysis` | skills/serp-analysis.md | Phân tích top 10 SERP, SERP features |
| 5 | `competitor-analysis` | skills/competitor-analysis.md | Tìm content gap, phân tích đối thủ |

### Lớp 2: Tối ưu (Optimization)

| # | Skill | File | Mô tả ngắn |
|---|-------|------|------------|
| 6 | `content-brief-generator` | skills/content-brief-generator.md | Tạo content brief chuẩn SEO cho writer/AI |
| 7 | `on-page-optimizer` | skills/on-page-optimizer.md | Audit & tối ưu on-page cho URL cụ thể |
| 8 | `technical-seo-audit` | skills/technical-seo-audit.md | Phát hiện lỗi kỹ thuật crawl/indexing |

### Lớp 3: Theo dõi & Báo cáo (Monitoring & Reporting)

| # | Skill | File | Mô tả ngắn |
|---|-------|------|------------|
| 9 | `rank-tracker` | skills/rank-tracker.md | Theo dõi biến động thứ hạng từ khóa |
| 10 | `seo-report-generator` | skills/seo-report-generator.md | Tổng hợp báo cáo SEO định kỳ |
| 11 | `algorithm-update-monitor` | skills/algorithm-update-monitor.md | Theo dõi tác động Google algorithm |

---

## Pipeline tích hợp

Xem chi tiết tại: `workflows/full-seo-pipeline.md`

```
keyword-research
    └── topical-map-builder ◄── competitor-analysis
            └── topic-cluster-planner
                    ├── serp-analysis
                    └── content-brief-generator
                                └── [Publish]
                                        └── on-page-optimizer
                                                └── rank-tracker
                                                        └── seo-report-generator
```

---

## Tài liệu Tiêu chuẩn (Standards)

Các file tiêu chuẩn dùng làm nguồn tham chiếu cho skill. Khi gọi một skill, Claude sẽ tự động áp dụng tiêu chuẩn tương ứng.

| File | Dùng cho Skill | Nội dung |
|------|---------------|----------|
| `standards/content-seo-standards.md` | content-brief-generator, on-page-optimizer | Tiêu chuẩn bài viết chuẩn SEO: metadata, heading, keyword, E-E-A-T, checklist pre/post-publish |
| `standards/technical-seo-checklist.md` | technical-seo-audit | Checklist kỹ thuật đầy đủ 🔴/🟡/🟢, CWV targets, scoring matrix |
| `standards/on-page-seo-standards.md` | on-page-optimizer, content-brief-generator | Checklist on-page 9 bước, scoring matrix, quick wins |
| `standards/topical-authority-standards.md` | topical-map-builder, topic-cluster-planner | Cấu trúc 3 cấp, tiêu chí pillar/cluster, anchor text, URL structure, cannibalization prevention |
| `standards/serpapi-integration.md` | serp-analysis, keyword-research, topical-map-builder, rank-tracker, algorithm-update-monitor | Hướng dẫn tích hợp SerpAPI — fetch dữ liệu thực tế để tiết kiệm token |

---

## Tích hợp SerpAPI (tiết kiệm token)

Cài đặt một lần:
```bash
cd "D:\Claude Code\seo-workspace"
pip install -r scripts/requirements.txt
cp .env.example .env   # sau đó điền SERPAPI_KEY vào .env
```

Lệnh nhanh trước khi gọi skill:
```bash
python scripts/serpapi_helpers.py serp    "keyword"         --save  # → serp-analysis
python scripts/serpapi_helpers.py keyword "seed keyword"    --save  # → keyword-research
python scripts/serpapi_helpers.py rank    domain.com kw1 kw2 --save # → rank-tracker
python scripts/serpapi_helpers.py algorithm "niche" kw1 kw2 --save  # → algorithm-update-monitor
```

---

## Thứ tự ưu tiên dùng cho dự án mới

1. `keyword-research` → 2. `topical-map-builder` → 3. `topic-cluster-planner` → 4. `content-brief-generator` → 5. `on-page-optimizer` → 6. `technical-seo-audit` → 7. `rank-tracker` → 8. `seo-report-generator`
