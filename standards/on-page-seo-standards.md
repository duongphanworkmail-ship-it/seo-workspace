# Tiêu chuẩn On-page SEO

Tài liệu tham chiếu cho: `on-page-optimizer`, `content-brief-generator`

---

## 1. Checklist On-page theo thứ tự kiểm tra

Thứ tự dưới đây phản ánh mức độ ảnh hưởng đến ranking từ cao xuống thấp.

---

### Bước 1: Kiểm tra Search Intent Match

Đây là yếu tố quan trọng nhất — nội dung sai intent sẽ không bao giờ rank dù có tối ưu tốt đến đâu.

- [ ] Xác định intent thực tế của từ khóa (dùng `serp-analysis`)
- [ ] Content type của trang phù hợp với top 10 SERP:
  - Informational intent → Blog post, Guide, How-to
  - Commercial intent → Comparison, Review, Best-of list
  - Transactional intent → Product page, Landing page, Pricing page
  - Navigational intent → Brand page, Login page
- [ ] Content angle phù hợp (top 3 đang dùng angle nào? Mới nhất? Dễ nhất? Toàn diện nhất?)
- [ ] Content format phù hợp (listicle, step-by-step, table comparison, definition...)

> **Nguyên tắc:** Nếu intent sai, dừng lại và đánh giá lại content type trước khi tối ưu tiếp.

---

### Bước 2: Title Tag Optimization

| Tiêu chí | Tiêu chuẩn | Kiểm tra |
|----------|-----------|---------|
| Độ dài | 45–60 ký tự | [ ] |
| Có từ khóa chính | Đặt gần đầu | [ ] |
| Unique trên toàn site | Không trùng page nào | [ ] |
| Emotional trigger | Số, năm, lợi ích, câu hỏi | [ ] |
| Không spam keyword | Mỗi keyword ≤1 lần | [ ] |

**Công thức title:**
- `[Keyword] + [Kết quả/Lợi ích]` — cho how-to
- `[Số] + [Keyword] + [Context]` — cho listicle
- `[Keyword]: Hướng dẫn [tính từ] [Năm]` — cho guide
- `[Keyword] là gì? [Giải thích cơ bản]` — cho definition

---

### Bước 3: Heading Structure (H1–H6)

**H1:**
- [ ] Duy nhất 1 H1
- [ ] Chứa từ khóa chính
- [ ] Khác với title tag (không cần giống hệt)

**H2 (section chính):**
- [ ] Mỗi H2 = 1 angle/sub-topic độc lập
- [ ] Ít nhất 1 H2 chứa từ khóa chính hoặc synonym
- [ ] H2 còn lại chứa semantic terms / related keywords
- [ ] Số lượng H2: 3–8 cho bài tiêu chuẩn

**H3+ (sub-section):**
- [ ] Là con trực tiếp của H2 tương ứng (không nhảy cấp)
- [ ] Phù hợp cho FAQ answers, step-by-step, examples

**Lỗi thường gặp cần kiểm tra:**
- [ ] Không có H2 → H4 (bỏ qua H3)
- [ ] Không có 2 H1 trên cùng trang
- [ ] Heading không dùng làm decoration (dùng bold/CSS thay)

---

### Bước 4: Keyword Placement & Density

**Vị trí keyword chính phải có:**
- [ ] Title tag
- [ ] H1
- [ ] Trong 100 từ đầu tiên (intro paragraph)
- [ ] Ít nhất 1 H2
- [ ] Kết bài (outro)
- [ ] Meta description
- [ ] URL slug
- [ ] Alt text ảnh đại diện

**Keyword density:**
- [ ] 1–2% cho từ khóa chính (= khoảng 15–30 lần trong bài 1500 từ)
- [ ] Sử dụng biến thể tự nhiên: synonyms, related phrases, pronouns
- [ ] Không nhồi nhét: không có ≥3 lần keyword trong 1 đoạn

**Semantic/LSI terms:**
- [ ] Ít nhất 10–15 semantic terms rải trong toàn bài
- [ ] Semantic terms cần có trong: body text, H3s, alt texts, captions

---

### Bước 5: Content Depth & Quality

**Độ toàn diện (Comprehensiveness):**
- [ ] Phủ tất cả sub-topics mà top 3 competitor đã đề cập
- [ ] Có ít nhất 1 angle mà competitor chưa có (differentiation)
- [ ] Trả lời đủ PAA questions liên quan

**Readable & Scannable:**
- [ ] Đoạn văn tối đa 3–4 câu
- [ ] Có bullet points khi liệt kê ≥3 items
- [ ] Bold terms quan trọng (không quá 5% text)
- [ ] Table khi có dữ liệu so sánh
- [ ] Ảnh/diagram minh họa ít nhất mỗi H2

**E-E-A-T signals:**
- [ ] Tên tác giả + bio ngắn
- [ ] Ngày đăng + ngày cập nhật
- [ ] Trích dẫn số liệu từ nguồn có uy tín
- [ ] Kinh nghiệm thực tế / case study cá nhân (nếu phù hợp)

---

### Bước 6: Internal Linking

**Số lượng & chất lượng:**
- [ ] Tối thiểu 3–5 internal links
- [ ] Nếu là Cluster Page: có link về Pillar Page (bắt buộc)
- [ ] Nếu là Pillar Page: có link tới tất cả Cluster Pages trong cluster

**Anchor text:**
- [ ] Mô tả chính xác nội dung trang đích
- [ ] Đa dạng: không dùng cùng 1 anchor cho nhiều link
- [ ] Tránh: "xem tại đây", "click here", "bài viết này"
- [ ] Tránh over-optimized exact-match anchor cho cùng 1 trang

**Kiểm tra lỗi:**
- [ ] Không có broken internal links (404)
- [ ] Không link về trang noindex
- [ ] Kiểm tra với `internal-link-plan.csv` từ `topic-cluster-planner`

---

### Bước 7: Images & Media

| Hạng mục | Tiêu chuẩn |
|----------|-----------|
| Alt text | Mô tả ảnh + keyword tự nhiên, ≤125 ký tự |
| Tên file | Lowercase, có keyword, dấu gạch ngang |
| Kích thước | WebP/AVIF, <200KB, có width+height attribute |
| Số lượng | ≥1 ảnh mỗi H2 section |
| Caption | Khi ảnh cần giải thích thêm |

**Checklist:**
- [ ] Không có ảnh thiếu alt text
- [ ] Không có ảnh tên file là `IMG001.jpg` hoặc tương tự
- [ ] Ảnh hero/đầu bài đã được preload
- [ ] Ảnh below-the-fold có `loading="lazy"`

---

### Bước 8: Schema Markup

- [ ] Article schema (blog posts)
- [ ] Breadcrumb schema
- [ ] FAQ schema (nếu có FAQ section)
- [ ] HowTo schema (nếu là tutorial từng bước)
- [ ] Validate bằng Google Rich Results Test — không có errors

---

### Bước 9: Meta Description & Social Tags

**Meta description:**
- [ ] 120–160 ký tự
- [ ] Chứa từ khóa chính
- [ ] Có CTA (Tìm hiểu / Xem ngay / Khám phá)
- [ ] Unique mỗi trang

**Open Graph (cho social sharing):**
- [ ] `og:title` — tương tự title tag
- [ ] `og:description` — tương tự meta description
- [ ] `og:image` — ảnh 1200×630px, <1MB
- [ ] `og:type` — article cho blog posts

---

## 2. On-page SEO Scoring Matrix

Dùng để tính điểm nhanh cho mỗi trang:

| Hạng mục | Điểm tối đa | Điểm đạt được |
|----------|------------|---------------|
| Search intent match | 20 | |
| Title tag | 10 | |
| Heading structure | 10 | |
| Keyword placement | 15 | |
| Content depth | 20 | |
| Internal linking | 10 | |
| Images & media | 5 | |
| Schema markup | 5 | |
| Meta description | 5 | |
| **Tổng** | **100** | |

**Đánh giá:**
- 85–100: Xuất sắc — giữ nguyên, chỉ update khi có data mới
- 70–84: Tốt — sửa 1–2 điểm yếu để đẩy lên tốt hơn
- 55–69: Cần cải thiện — có thể mất thứ hạng nếu không sửa
- 0–54: Kém — ưu tiên rewrite toàn bộ

---

## 3. Quick Wins On-page (làm trong 30 phút)

Những việc nhỏ có tác động lớn, làm ngay không cần nhiều thời gian:

1. **Thêm từ khóa vào title tag** nếu chưa có
2. **Thêm/sửa meta description** nếu thiếu hoặc quá dài/ngắn
3. **Thêm alt text cho ảnh thiếu** — đặc biệt ảnh đầu bài
4. **Thêm internal link về Pillar Page** nếu là Cluster Page
5. **Thêm FAQ section** dựa trên PAA nếu chưa có
6. **Fix broken internal links** — chuyển về URL đúng
7. **Thêm keyword vào H2 đầu tiên** nếu chưa có
