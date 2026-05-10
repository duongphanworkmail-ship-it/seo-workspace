# Tiêu chuẩn Topical Authority & Content Architecture

Tài liệu tham chiếu cho: `topical-map-builder`, `topic-cluster-planner`

---

## 1. Topical Authority là gì?

Topical Authority là mức độ Google tin tưởng website của bạn là chuyên gia trong một lĩnh vực cụ thể. Website có Topical Authority cao sẽ:
- Rank nhanh hơn cho từ khóa mới trong niche
- Duy trì thứ hạng ổn định hơn qua các Core Updates
- Được Google ưu tiên cho Featured Snippets và Knowledge Panel

**Cách Google đánh giá Topical Authority:**
1. Mức độ phủ rộng: Bao nhiêu % sub-topics trong niche đã được đề cập?
2. Mức độ phủ sâu: Nội dung có expert-level không?
3. Consistency: Có focus vào niche không hay viết lan man?
4. Internal linking: Các trang có kết nối với nhau theo chủ đề không?

---

## 2. Tiêu chuẩn Topical Map

### Cấu trúc 3 cấp bắt buộc
```
Seed Topic (Niche)
├── Main Topic 1 (Cấp 1 — Pillar)
│   ├── Sub-topic 1.1 (Cấp 2 — Cluster)
│   │   ├── Micro-topic 1.1.1 (Cấp 3 — Supporting)
│   │   └── Micro-topic 1.1.2
│   └── Sub-topic 1.2
│       └── ...
├── Main Topic 2
│   └── ...
```

### Số lượng tối thiểu theo quy mô site

| Quy mô | Main Topics | Sub-topics/Main | Micro-topics/Sub |
|--------|-------------|-----------------|------------------|
| Site nhỏ (mới) | 3–5 | 3–5 | 2–4 |
| Site trung bình | 5–8 | 4–6 | 3–5 |
| Site lớn (authority) | 8–15 | 5–10 | 4–8 |

### Tiêu chí chất lượng của mỗi node trong map
- [ ] Mỗi node đại diện cho **1 search intent cụ thể** (không overlap)
- [ ] Mỗi node có **1 từ khóa chính** đại diện
- [ ] Node cấp 1 đủ rộng để có 5+ trang con
- [ ] Node cấp 3 đủ cụ thể để viết 1 bài hoàn chỉnh

### Topical Coverage Score Targets
| Giai đoạn | Coverage Score | Mô tả |
|-----------|---------------|-------|
| Mới bắt đầu | 0–20% | Tập trung build core topics |
| Đang phát triển | 20–50% | Google bắt đầu nhận diện authority |
| Established | 50–70% | Rank nhanh hơn cho từ khóa mới |
| Authority | 70%+ | Full topical authority, Google trust cao |

> **Mục tiêu ngắn hạn (3–6 tháng):** Đạt 50% coverage cho ít nhất 2 Main Topics
> **Mục tiêu dài hạn (12 tháng):** Đạt 70%+ coverage toàn bộ topical map

---

## 3. Tiêu chuẩn Topic Cluster

### Cấu trúc cluster chuẩn

```
[PILLAR PAGE] — Head keyword (broad)
    ↑ ↑ ↑ ↑ ↑  (nhận link từ tất cả cluster)
    │ │ │ │ │
    ▼ ▼ ▼ ▼ ▼  (link về pillar + cross-link nhau)
[C1] [C2] [C3] [C4] [C5]  — Cluster Pages (specific)
```

### Số lượng trang trong 1 cluster
| Quy mô cluster | Pillar | Cluster Pages | Tổng trang |
|----------------|--------|---------------|------------|
| Mini cluster | 1 | 3–5 | 4–6 |
| Standard cluster | 1 | 6–10 | 7–11 |
| Mega cluster | 1 | 10–20 | 11–21 |

### Tiêu chí Pillar Page
- [ ] Target **head keyword** (broad, 1–2 từ) với search volume cao
- [ ] Phủ **tổng quan** toàn bộ chủ đề — không đi quá sâu vào từng aspect
- [ ] Độ dài: **3.000–5.000 từ** (đủ để phủ rộng)
- [ ] Link tới **tất cả Cluster Pages** trong cluster (anchor text mô tả)
- [ ] Nhận internal links từ tất cả Cluster Pages (bắt buộc)
- [ ] URL: ngắn, cấp cao (`/pillar-slug/`)

### Tiêu chí Cluster Pages
- [ ] Target **long-tail keyword** (3–5 từ), specific hơn Pillar
- [ ] Phủ **sâu** 1 aspect cụ thể của Pillar Topic
- [ ] Độ dài: **1.500–2.500 từ**
- [ ] **Bắt buộc có** 1 link về Pillar Page với anchor text chứa head keyword
- [ ] Cross-link tới 2–3 Cluster Pages liên quan (semantic)
- [ ] URL: dưới Pillar (`/pillar-slug/cluster-slug/`)

---

## 4. Tiêu chuẩn Internal Linking trong Cluster

### Quy tắc link equity flow
```
Cluster Page 1 ──────► Pillar Page (link juice chảy lên)
Cluster Page 2 ──────► Pillar Page
Cluster Page 3 ──────► Pillar Page
Pillar Page ──────────► Cluster 1, 2, 3 (phân phối xuống)
Cluster 1 ────────────► Cluster 2 (semantic cross-link)
```

### Anchor text standards
| Loại anchor | Tỷ lệ khuyến nghị | Ví dụ |
|------------|-------------------|-------|
| Exact match keyword | 10–20% | "SEO kỹ thuật" |
| Partial match | 30–40% | "kỹ thuật tối ưu SEO" |
| Branded | 10–20% | "tại Example.com" |
| Natural/contextual | 30–40% | "tìm hiểu thêm về tốc độ tải trang" |

**Tuyệt đối tránh:**
- "Xem tại đây", "Click here", "Đọc thêm" — không có keyword
- Cùng anchor text trỏ về nhiều trang khác nhau
- Quá nhiều exact-match anchor (>30%) — có thể bị Google penalty

### Số lượng internal links
| Loại trang | Links đi ra | Links đi vào |
|------------|------------|-------------|
| Pillar Page | 8–15 (đến tất cả clusters) | Tất cả clusters trong cluster |
| Cluster Page | 4–8 (1 về pillar + cross-links) | Pillar + 2–3 clusters liên quan |
| Micro-content | 2–4 (1 về cluster, 1 về pillar) | Cluster tương ứng |

---

## 5. Content Cannibalization Prevention

Keyword cannibalization xảy ra khi 2+ trang cùng target một keyword — chúng "ăn nhau", làm giảm thứ hạng cả hai.

### Quy tắc "1 keyword = 1 trang"
- [ ] Mỗi keyword chính chỉ được 1 trang target
- [ ] Kiểm tra cannibalization bằng: `site:example.com "keyword"` trên Google
- [ ] Nếu 2 trang cùng SERP → xem xét merge, canonical, hoặc differentiate angle

### Cách differentiate trang có chủ đề tương tự
| Trang 1 | Trang 2 | Cách differentiate |
|---------|---------|-------------------|
| "SEO là gì" | "SEO là gì? Hướng dẫn cho người mới" | Intent khác: definition vs. beginner guide |
| "Công cụ SEO" | "Công cụ SEO miễn phí" | Modifier khác: general vs. free |
| "Tốc độ website" | "Tối ưu tốc độ website WordPress" | Audience khác: general vs. WordPress |

---

## 6. Thứ tự triển khai Content Architecture

Đây là thứ tự **quan trọng** — sai thứ tự sẽ tạo orphan pages và mất link equity.

### Giai đoạn 1: Nền tảng (Tháng 1)
1. Xây `topical-map` cho toàn niche
2. Xác định 2–3 Main Topics ưu tiên cao nhất
3. Viết và publish **Pillar Pages** trước
4. Setup `technical-seo-audit` — fix lỗi trước khi build content

### Giai đoạn 2: Build Clusters (Tháng 2–4)
5. Viết Cluster Pages theo từng cluster — mỗi lần viết 1 cluster xong hoàn chỉnh
6. Thêm internal links ngay khi publish (không để sau)
7. Update Pillar Page để link tới Cluster Pages mới

### Giai đoạn 3: Mở rộng & Deepen (Tháng 5+)
8. Viết Micro-content cho các Cluster Pages đã rank top 10–20
9. Refresh Pillar Pages với nội dung mới
10. Mở rộng sang Main Topics mới trong topical map

---

## 7. URL Structure Chuẩn

| Cấp trang | URL Pattern | Ví dụ |
|-----------|------------|-------|
| Homepage | `/` | `example.com/` |
| Category/Pillar | `/[pillar]/` | `/seo/` |
| Cluster Page | `/[pillar]/[cluster]/` | `/seo/seo-ky-thuat/` |
| Micro-content | `/[pillar]/[cluster]/[micro]/` | `/seo/seo-ky-thuat/toc-do-website/` |

**Quy tắc URL:**
- [ ] Lowercase, không dấu, dùng `-` không dùng `_`
- [ ] Tối đa 3–4 cấp (tránh URL quá dài)
- [ ] Không thay đổi URL sau khi đã indexed (gây mất link equity)
- [ ] URL phản ánh đúng cấu trúc cluster

---

## 8. Topical Authority Monitoring

Theo dõi tiến độ xây dựng Topical Authority:

| Chỉ số | Đo lường bằng | Mục tiêu |
|--------|--------------|---------|
| Topical Coverage Score | Topical Map (% nodes có content) | >70% sau 12 tháng |
| Topic Cluster Completeness | Số clusters hoàn chỉnh / tổng clusters | >80% |
| Internal Link Density | Avg. internal links/page | >5 links/trang |
| Orphan Pages | Trang không có internal link vào | 0 |
| Cannibalization | Số cặp trang tranh nhau keyword | 0 |
| Ranking velocity | Thời gian trung bình từ publish → top 10 | Giảm dần qua thời gian |
