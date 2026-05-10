# Checklist Technical SEO

Tài liệu tham chiếu cho: `technical-seo-audit`

Phân loại theo mức độ: 🔴 Critical | 🟡 Warning | 🟢 Info

---

## 1. Crawlability & Indexability

### robots.txt
- 🔴 [ ] File robots.txt tồn tại và accessible tại `/robots.txt`
- 🔴 [ ] Không block Googlebot crawl toàn site (`Disallow: /`)
- 🟡 [ ] Không block CSS, JS quan trọng (Google cần render page)
- 🟡 [ ] Block các thư mục không cần index: `/wp-admin/`, `/checkout/`, `/cart/`, `/account/`
- 🟢 [ ] Có khai báo `Sitemap:` trong robots.txt

### XML Sitemap
- 🔴 [ ] Có sitemap.xml tại `/sitemap.xml` hoặc `/sitemap_index.xml`
- 🔴 [ ] Sitemap đã được submit lên Google Search Console
- 🔴 [ ] Không có URL `noindex` trong sitemap
- 🟡 [ ] Không có URL 4xx/5xx trong sitemap
- 🟡 [ ] Sitemap cập nhật tự động khi có bài mới
- 🟡 [ ] Sitemap có `<lastmod>` cho mỗi URL
- 🟢 [ ] Tách sitemap nếu >10.000 URLs (sitemap index)
- 🟢 [ ] Có image sitemap, video sitemap nếu cần

### Meta Robots & Canonical
- 🔴 [ ] Trang quan trọng không có `<meta name="robots" content="noindex">`
- 🔴 [ ] Mỗi trang có canonical tag tự trỏ về chính nó (self-canonical)
- 🔴 [ ] Canonical không trỏ về trang noindex
- 🔴 [ ] Không có canonical chain (A → B → C, nên là A → C)
- 🟡 [ ] Trang pagination: `rel="next"` / `rel="prev"` hoặc canonical về trang chính
- 🟡 [ ] Faceted navigation URLs không bị index (dùng canonical hoặc noindex)

### Crawl Depth
- 🟡 [ ] Trang quan trọng nhất (Pillar Pages) nằm trong 2–3 click từ homepage
- 🟡 [ ] Không có "orphan pages" (trang không có internal link nào trỏ vào)
- 🟢 [ ] Trang quan trọng được link từ navigation chính

---

## 2. URL & Redirect

### URL Structure
- 🔴 [ ] Toàn site dùng HTTPS (không HTTP)
- 🔴 [ ] Chọn 1 canonical version: www hoặc non-www — nhất quán toàn site
- 🟡 [ ] URL lowercase (không MixedCase)
- 🟡 [ ] Dùng dấu gạch ngang `-` không phải gạch dưới `_`
- 🟡 [ ] URL ngắn, mô tả rõ nội dung, chứa keyword
- 🟡 [ ] Không có tham số session/tracking trong URL được index (`?sessionid=xxx`)
- 🟢 [ ] URL depth tối đa 3–4 cấp (example.com/level1/level2/level3/)

### Redirects
- 🔴 [ ] Không có redirect chain (A → B → C) — hợp nhất thành A → C
- 🔴 [ ] Không có redirect loop (A → B → A)
- 🔴 [ ] Redirect vĩnh viễn dùng **301**, không dùng 302
- 🔴 [ ] www và non-www đều redirect về 1 version (301)
- 🔴 [ ] HTTP redirect về HTTPS (301)
- 🟡 [ ] Trailing slash nhất quán: `/page/` hoặc `/page` — không có cả 2 cùng return 200
- 🟡 [ ] Trang đã xóa: redirect 301 về trang liên quan nhất, hoặc trả 410 nếu không có trang thay thế

### Error Pages
- 🔴 [ ] Không có broken internal links (link nội bộ trỏ tới 404)
- 🔴 [ ] Custom 404 page: có navigation, gợi ý nội dung liên quan, không return 200
- 🟡 [ ] Không có 5xx server errors
- 🟢 [ ] 404 page có liên kết về homepage và các mục chính

---

## 3. Site Speed & Core Web Vitals

### Core Web Vitals Targets (Google's thresholds)
| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| **LCP** (Largest Contentful Paint) | < 2.5s | 2.5–4s | > 4s |
| **INP** (Interaction to Next Paint) | < 200ms | 200–500ms | > 500ms |
| **CLS** (Cumulative Layout Shift) | < 0.1 | 0.1–0.25 | > 0.25 |

### LCP Optimization Checklist
- 🔴 [ ] Hero image / largest element load trong < 2.5s
- 🔴 [ ] Preload LCP image: `<link rel="preload" as="image">`
- 🟡 [ ] Server response time (TTFB) < 600ms
- 🟡 [ ] Không dùng CSS background-image cho LCP element (dùng `<img>` thay)
- 🟡 [ ] Images dùng định dạng modern: WebP hoặc AVIF
- 🟡 [ ] Ảnh có `width` và `height` attribute để tránh layout shift

### CLS Optimization Checklist
- 🔴 [ ] Tất cả ảnh có `width` + `height` hoặc `aspect-ratio` trong CSS
- 🔴 [ ] Không inject nội dung phía trên nội dung hiện có (ads, banners)
- 🟡 [ ] Font loading: dùng `font-display: swap`
- 🟡 [ ] Tránh animation thay đổi kích thước element

### INP / JavaScript Optimization
- 🟡 [ ] Không có long tasks >50ms trên main thread
- 🟡 [ ] Defer non-critical JS: `<script defer>` hoặc `<script async>`
- 🟡 [ ] Không có render-blocking scripts trong `<head>`
- 🟢 [ ] Code splitting: chỉ load JS cần thiết cho từng page

### General Performance
- 🟡 [ ] Enable GZIP/Brotli compression trên server
- 🟡 [ ] Browser caching: static assets có Cache-Control headers
- 🟡 [ ] CDN cho static assets (images, CSS, JS)
- 🟡 [ ] Ảnh lazy loading: `loading="lazy"` cho ảnh below the fold
- 🟢 [ ] CSS Critical Path: inline CSS above-the-fold

---

## 4. Mobile & Security

### Mobile-Friendliness
- 🔴 [ ] Responsive design: site hiển thị đúng trên mobile
- 🔴 [ ] Viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- 🔴 [ ] Font size tối thiểu 16px cho body text
- 🟡 [ ] Touch targets (buttons, links) ít nhất 48x48px
- 🟡 [ ] Không có horizontal scroll trên mobile
- 🟡 [ ] Popup/interstitial không che toàn bộ nội dung ngay khi vào trang

### HTTPS & Security
- 🔴 [ ] SSL certificate hợp lệ, không expired
- 🔴 [ ] Không có mixed content (HTTP resource trong HTTPS page)
- 🟡 [ ] HSTS header: `Strict-Transport-Security`
- 🟢 [ ] Security headers: X-Frame-Options, X-Content-Type-Options, CSP

---

## 5. Structured Data

### Markup bắt buộc
- 🟡 [ ] **Organization** hoặc **LocalBusiness** trên homepage
- 🟡 [ ] **WebSite** với sitelinks searchbox (nếu muốn search box trên SERP)
- 🟡 [ ] **Breadcrumb** trên tất cả trang nội (trừ homepage)
- 🟡 [ ] **Article** trên tất cả blog posts

### Markup theo loại nội dung
- 🟢 [ ] FAQPage trên trang có FAQ section
- 🟢 [ ] HowTo trên trang hướng dẫn từng bước
- 🟢 [ ] Product + Review + AggregateRating trên product pages
- 🟢 [ ] Recipe trên trang công thức
- 🟢 [ ] Event trên trang sự kiện

### Validation
- 🔴 [ ] Không có lỗi (errors) trong Google Rich Results Test
- 🟡 [ ] Không có warnings trong Structured Data Testing Tool
- 🔴 [ ] Markup nhất quán với nội dung hiển thị (không markup thứ ẩn)

---

## 6. International SEO (Áp dụng khi có đa ngôn ngữ)

- 🔴 [ ] hreflang tags đúng format: `<link rel="alternate" hreflang="vi" href="...">`
- 🔴 [ ] Reciprocal hreflang: trang A trỏ tới B, trang B phải trỏ lại A
- 🔴 [ ] x-default hreflang cho fallback version
- 🟡 [ ] URL structure nhất quán cho các ngôn ngữ (subdirectory: /vi/, /en/)
- 🟡 [ ] Sitemap tách theo ngôn ngữ hoặc có hreflang trong sitemap

---

## 7. Duplicate Content

- 🔴 [ ] www và non-www không return 200 cho cùng nội dung (phải redirect)
- 🔴 [ ] HTTP và HTTPS không return 200 cho cùng nội dung
- 🟡 [ ] Trailing slash: `/page/` và `/page` không return 200 cùng lúc
- 🟡 [ ] Không có printer-friendly pages được index
- 🟡 [ ] Không có session IDs, tracking parameters trong URLs được index
- 🟡 [ ] Ecommerce: faceted navigation (filter, sort) dùng canonical hoặc noindex

---

## 8. Log File & Crawl Budget (Dành cho site lớn >10k pages)

- 🟡 [ ] Googlebot đang crawl trang quan trọng không? (kiểm tra Server Logs hoặc GSC)
- 🟡 [ ] Crawl budget không bị lãng phí vào: trang lỗi, trang trùng, infinite scroll URLs
- 🟢 [ ] Sitemap giúp Googlebot tìm trang quan trọng nhanh hơn

---

## 9. Google Search Console Checklist

- 🔴 [ ] Site đã verify trong Google Search Console
- 🔴 [ ] Không có Manual Actions (penalization)
- 🔴 [ ] Không có Security Issues
- 🟡 [ ] Sitemap đã submit và không có lỗi
- 🟡 [ ] Coverage report: trang nào bị Excluded cần review
- 🟡 [ ] Core Web Vitals report: URL nào Failed cần fix
- 🟢 [ ] Breadcrumb, FAQ, HowTo enhancement reports — có errors không?

---

## 10. Technical Audit Scoring

Tính điểm nhanh sau audit:

| Hạng mục | Trọng số | Điểm (0-10) |
|----------|----------|-------------|
| Crawlability & Indexability | 25% | |
| URL & Redirects | 20% | |
| Core Web Vitals | 20% | |
| Mobile & Security | 15% | |
| Structured Data | 10% | |
| Duplicate Content | 10% | |
| **Tổng điểm** | 100% | **/10** |

**Đánh giá:**
- 8–10: Healthy — maintain và monitor
- 6–7.9: Needs Improvement — lên kế hoạch fix
- 0–5.9: Critical — ưu tiên fix ngay trước mọi hoạt động SEO khác
