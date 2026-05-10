# Workflow: Full SEO Pipeline

Workflow end-to-end cho dự án SEO mới hoặc tái cấu trúc website hiện có. Chạy theo thứ tự từ Nghiên cứu → Tối ưu → Theo dõi.

---

## Tổng quan Pipeline

```
[DỰ ÁN MỚI / NICHE MỚI]
         │
         ▼
    ┌─────────────────────┐
    │  GIAI ĐOẠN 1        │
    │  NGHIÊN CỨU         │
    └─────────────────────┘
         │
         ▼
① keyword-research
   INPUT: seed keyword, market, niche
   OUTPUT: bảng từ khóa phân nhóm theo intent
         │
         ├──────────────────► ⑤ competitor-analysis
         │                       INPUT: URL đối thủ
         ▼                       OUTPUT: content gap list
② topical-map-builder ◄──────────────────────┘
   INPUT: seed topic + content gaps từ competitor-analysis
   OUTPUT: topical-map.md + coverage-score + gaps
         │
         ▼
③ topic-cluster-planner
   INPUT: topical-map.md, pillar topic, domain
   OUTPUT: cluster-map + internal-link-plan.csv + url-structure
         │
         │
    ┌─────────────────────┐
    │  GIAI ĐOẠN 2        │
    │  TỐI ƯU             │
    └─────────────────────┘
         │
         ├──────────────────────────────────────┐
         ▼                                      ▼
④ serp-analysis                   ⑧ technical-seo-audit
   INPUT: từ khóa target             INPUT: domain
   OUTPUT: content format gợi ý      OUTPUT: lỗi kỹ thuật ưu tiên
         │
         ▼
⑥ content-brief-generator
   INPUT: keyword + serp-analysis + cluster-map
   OUTPUT: content brief (.md)
         │
         ▼
   [VIẾT NỘI DUNG / PUBLISH]
         │
         ▼
⑦ on-page-optimizer
   INPUT: URL + keyword + internal-link-plan
   OUTPUT: audit checklist + quick wins
         │
         │
    ┌─────────────────────┐
    │  GIAI ĐOẠN 3        │
    │  THEO DÕI & BÁO CÁO │
    └─────────────────────┘
         │
         ▼
⑨ rank-tracker
   INPUT: keyword list + ranking data
   OUTPUT: ranking report + alerts
         │
         ├──────────► ⑪ algorithm-update-monitor
         │               (khi có traffic drop đột ngột)
         ▼
⑩ seo-report-generator
   INPUT: rank-tracker + technical-audit + traffic data
   OUTPUT: báo cáo SEO tuần/tháng
```

---

## Hướng dẫn từng giai đoạn

### Giai đoạn 1: Nghiên cứu (Tuần 1-2)

**Bước 1.1 — keyword-research**
```
Mục tiêu: Xác định từ khóa tiềm năng cho niche
Thời gian: 2-4 giờ
Output cần lưu: bảng từ khóa + intent + cluster groups
```

**Bước 1.2 — competitor-analysis** (song song với 1.1)
```
Mục tiêu: Tìm content gaps đối thủ chưa phủ
Thời gian: 2-3 giờ
Output cần lưu: danh sách content gaps theo ưu tiên
```

**Bước 1.3 — topical-map-builder**
```
Mục tiêu: Xây bản đồ chủ đề 3 cấp
Input từ: 1.1 (keyword clusters) + 1.2 (content gaps)
Thời gian: 3-5 giờ
Output cần lưu: topical-map.md + coverage-score
```

**Bước 1.4 — topic-cluster-planner** (cho từng Main Topic)
```
Mục tiêu: Thiết kế pillar + cluster + internal links
Input từ: 1.3 (topical map)
Thời gian: 2-3 giờ/cluster
Output cần lưu: cluster-map.md + internal-link-plan.csv
Lặp lại cho mỗi Main Topic trong topical map
```

---

### Giai đoạn 2: Tối ưu (Liên tục)

**Bước 2.1 — technical-seo-audit** (ngay khi bắt đầu)
```
Mục tiêu: Fix lỗi kỹ thuật trước khi tạo nội dung mới
Thời gian: 3-5 giờ
Lặp lại: Hàng tháng hoặc sau mỗi deployment lớn
```

**Chu trình tạo nội dung (lặp cho mỗi Cluster Page):**

```
serp-analysis (30 phút)
      ↓
content-brief-generator (1 giờ)
      ↓
[Viết nội dung] (2-8 giờ tùy độ dài)
      ↓
on-page-optimizer (30 phút - audit trước publish)
      ↓
[Publish]
      ↓
on-page-optimizer (30 phút - re-check sau publish)
```

---

### Giai đoạn 3: Theo dõi & Báo cáo (Liên tục)

**Weekly:**
- rank-tracker: theo dõi biến động hàng tuần
- Nếu có drop đột ngột → algorithm-update-monitor

**Monthly:**
- seo-report-generator: tổng hợp báo cáo tháng
- technical-seo-audit: re-check lỗi kỹ thuật
- Cập nhật topical-map với nội dung mới đã publish (coverage score mới)

**Quarterly:**
- Đánh giá lại topical map: có chủ đề mới cần phủ không?
- Cập nhật cluster cho các Main Topic
- Full competitor-analysis để tìm gaps mới

---

## Thời gian dự kiến cho dự án mới

| Giai đoạn | Thời gian |
|-----------|-----------|
| Nghiên cứu (1 niche, 3-5 clusters) | 2-3 tuần |
| Technical audit + fix | 1-2 tuần |
| Content production (10 bài đầu) | 3-4 tuần |
| Bắt đầu thấy kết quả ranking | Tháng 3-6 |
| Full topical authority | Tháng 6-12 |

---

## Tips & Best Practices

1. **Luôn chạy topical-map-builder trước** khi viết bất kỳ nội dung nào — tránh viết bài rời rạc không có cấu trúc.

2. **Xây Pillar Page trước Cluster Pages** — Pillar Page là "neo" của toàn bộ cluster, cần có trước để cluster pages có chỗ link về.

3. **Internal links ngay từ bài đầu** — Dùng internal-link-plan.csv để thêm internal links vào mỗi bài ngay khi publish, không để sau.

4. **Topical Coverage Score mục tiêu: >70%** trước khi đẩy mạnh link building — Google cần thấy site có chiều sâu trước khi trust domain.

5. **Cập nhật nội dung cũ trước khi viết mới** — Nếu coverage score đã >60%, ưu tiên refresh bài cũ hơn viết bài mới.

6. **Dùng rank-tracker để quyết định ưu tiên** — Từ khóa ở vị trí 4-10 là "low-hanging fruit", push lên top 3 dễ hơn nhiều so với từ khóa ở vị trí 20+.
