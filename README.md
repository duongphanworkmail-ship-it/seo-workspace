# SEO Workspace — Claude Code

Workspace tự động hóa SEO website dùng Claude Code làm nền tảng. Gồm 11 skill độc lập, 4 file tiêu chuẩn tham chiếu, Python helpers tích hợp SerpAPI, và workflow pipeline end-to-end.

## Cấu trúc

```
seo-workspace/
├── CLAUDE.md                          # Hướng dẫn workspace & index skill
├── skills/                            # 11 skill SEO
│   ├── keyword-research.md
│   ├── topical-map-builder.md         # Xây bản đồ chủ đề 3 cấp
│   ├── topic-cluster-planner.md       # Thiết kế Pillar + Cluster + Internal Links
│   ├── serp-analysis.md
│   ├── competitor-analysis.md
│   ├── content-brief-generator.md
│   ├── on-page-optimizer.md
│   ├── technical-seo-audit.md
│   ├── rank-tracker.md
│   ├── seo-report-generator.md
│   └── algorithm-update-monitor.md
├── standards/                         # Tài liệu tiêu chuẩn tham chiếu
│   ├── content-seo-standards.md       # Tiêu chuẩn bài viết chuẩn SEO
│   ├── technical-seo-checklist.md     # Checklist kỹ thuật 🔴/🟡/🟢
│   ├── on-page-seo-standards.md       # Checklist on-page 9 bước
│   ├── topical-authority-standards.md # Tiêu chuẩn Topical Authority & Cluster
│   └── serpapi-integration.md         # Hướng dẫn tích hợp SerpAPI
├── scripts/
│   ├── serpapi_helpers.py             # Python helpers gọi SerpAPI
│   └── requirements.txt
├── workflows/
│   └── full-seo-pipeline.md           # Pipeline end-to-end
├── output/                            # Kết quả phân tích
│   └── keyword-research-phong-hop-truc-tuyen.md
├── .env.example                       # Template cấu hình API key
└── .gitignore
```

## Cài đặt

```bash
# Cài Python dependencies cho SerpAPI
pip install -r scripts/requirements.txt

# Cấu hình API key
cp .env.example .env
# Điền SERPAPI_KEY vào .env (lấy tại serpapi.com/manage-api-key)
```

## Cách sử dụng Skill

Mở Claude Code trong thư mục này, sau đó gọi skill bằng ngôn ngữ tự nhiên:

```
Chạy keyword-research cho "phần mềm họp trực tuyến"
Chạy topical-map-builder cho niche: SaaS cộng tác
Chạy serp-analysis cho "Zoom vs Google Meet"
```

## Tích hợp SerpAPI (tiết kiệm token)

```bash
# Fetch data thực tế trước khi gọi skill
python scripts/serpapi_helpers.py serp    "keyword"           --save
python scripts/serpapi_helpers.py keyword "seed keyword"      --save
python scripts/serpapi_helpers.py rank    domain.com kw1 kw2  --save
python scripts/serpapi_helpers.py algorithm "niche" kw1 kw2   --save
```

## Skills theo nhóm

### Lớp 1: Nghiên cứu
- `keyword-research` — Tìm & phân nhóm từ khóa theo intent
- `topical-map-builder` — Bản đồ chủ đề 3 cấp + Topical Coverage Score
- `topic-cluster-planner` — Pillar + Cluster + Internal Linking Map
- `serp-analysis` — Phân tích top 10 SERP + SERP features
- `competitor-analysis` — Content gap + phân tích đối thủ

### Lớp 2: Tối ưu
- `content-brief-generator` — Brief chuẩn SEO cho writer/AI
- `on-page-optimizer` — Audit on-page 9 bước + quick wins
- `technical-seo-audit` — Phát hiện lỗi kỹ thuật crawl/indexing

### Lớp 3: Theo dõi & Báo cáo
- `rank-tracker` — Theo dõi biến động thứ hạng
- `seo-report-generator` — Tổng hợp báo cáo SEO định kỳ
- `algorithm-update-monitor` — Phân tích tác động Google algorithm updates

## Kết quả phân tích mẫu

- [`output/keyword-research-phong-hop-truc-tuyen.md`](output/keyword-research-phong-hop-truc-tuyen.md) — Phân tích 42 từ khóa cho niche phần mềm họp trực tuyến
