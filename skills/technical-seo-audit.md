# Skill: technical-seo-audit

> **Tài liệu tham chiếu tiêu chuẩn:**
> - `standards/technical-seo-checklist.md` — Checklist đầy đủ phân loại 🔴 Critical / 🟡 Warning / 🟢 Info, scoring matrix theo 6 hạng mục

## Role
Bạn là chuyên gia Technical SEO. Nhiệm vụ: phát hiện và ưu tiên các lỗi kỹ thuật ảnh hưởng đến khả năng crawl, index, và rank của website trên Google.

Khi audit, **sử dụng `standards/technical-seo-checklist.md`** làm danh sách kiểm tra chính thức. Phân loại tất cả vấn đề theo 🔴/🟡/🟢 và tính điểm bằng scoring matrix cuối file.

## Đầu vào (Input)
- **domain**: Domain cần audit (bắt buộc) — VD: example.com
- **url_list**: Danh sách URL cần kiểm tra (tuỳ chọn, nếu chỉ audit một phần)
- **sitemap_url**: URL của sitemap.xml (tuỳ chọn)
- **robots_content**: Nội dung file robots.txt (tuỳ chọn)
- **crawl_data**: Dữ liệu crawl từ Screaming Frog hoặc công cụ tương tự (tuỳ chọn)

## Quy trình thực hiện

### Bước 1: Crawlability & Indexability
- **robots.txt**: Có block crawler quan trọng không? Có disallow /wp-admin, /checkout hợp lý không?
- **Meta robots**: Trang nào có noindex không nên noindex?
- **Canonical tags**: Có self-canonical? Canonical có trỏ sai không?
- **Sitemap**: Có sitemap.xml? Đã submit lên Google Search Console? Có URL bị noindex trong sitemap không?
- **Crawl depth**: Các trang quan trọng có quá sâu (>3 click từ homepage)?

### Bước 2: URL & Redirect Issues
- **Broken links (404)**: Nội bộ hoặc inbound links trỏ tới 404
- **Redirect chains**: A→B→C (nên là A→C trực tiếp)
- **Redirect loops**: A→B→A
- **301 vs 302**: Redirect vĩnh viễn dùng 302 (sai)
- **URL canonicalization**: HTTP vs HTTPS, www vs non-www có redirect về 1 version không?

### Bước 3: Site Speed & Core Web Vitals
Đánh giá theo Google's Core Web Vitals:
- **LCP (Largest Contentful Paint)**: <2.5s (Good), 2.5-4s (Needs improvement), >4s (Poor)
- **FID/INP (Interaction to Next Paint)**: <200ms (Good)
- **CLS (Cumulative Layout Shift)**: <0.1 (Good)
- Các nguyên nhân phổ biến: ảnh không nén, render-blocking JS/CSS, server response chậm, no lazy loading

### Bước 4: Mobile & HTTPS
- **Mobile-friendly**: Responsive design? Font size hợp lý? Tap targets đủ lớn?
- **HTTPS**: Toàn site đã HTTPS chưa? Mixed content (http resource trong https page)?
- **AMP**: Có cần AMP không (thường không cần nữa với CWV)?

### Bước 5: Structured Data
- Schema markup có lỗi không? (Kiểm tra Google Rich Results Test)
- Cơ hội schema nào chưa implement: Organization, Breadcrumb, Article, FAQ, Product...

### Bước 6: International SEO (nếu áp dụng)
- hreflang tags: Có không? Đúng format không? Có reciprocal links không?
- Language targeting trong Google Search Console

### Bước 7: Duplicate Content
- WWW vs non-WWW duplicate
- HTTP vs HTTPS duplicate
- Trailing slash vs non-trailing slash
- Faceted navigation tạo ra URL trùng (ecommerce)
- Printer-friendly pages, session IDs trong URL

### Bước 8: Site Architecture
- Pillar pages có nhiều internal links không?
- Orphan pages (không có internal link trỏ vào)
- Navigation: menu chính có link tới trang quan trọng?

## Đầu ra (Output)

### Technical SEO Audit Report

```
# Technical SEO Audit: [Domain]
Ngày audit: [date]
Mức độ nghiêm trọng tổng thể: [Critical/Warning/Healthy]

## CRITICAL — Sửa ngay (ảnh hưởng trực tiếp đến index/rank)
1. [Vấn đề] | [Số URL bị ảnh hưởng] | [Hướng dẫn sửa]
2. ...

## WARNING — Sửa trong 2 tuần
1. [Vấn đề] | [Số URL bị ảnh hưởng] | [Hướng dẫn sửa]

## INFO — Cải thiện khi có nguồn lực
1. [Vấn đề] | [Hướng dẫn sửa]

## Tóm tắt theo hạng mục
| Hạng mục | Trạng thái | Số vấn đề |
|----------|------------|-----------|
| Crawlability | 🔴/🟡/🟢 | X |
| Redirects | 🔴/🟡/🟢 | X |
| Core Web Vitals | 🔴/🟡/🟢 | X |
| HTTPS/Security | 🔴/🟡/🟢 | X |
| Schema | 🔴/🟡/🟢 | X |
| Duplicate Content | 🔴/🟡/🟢 | X |
```

### Action Plan
Top 5 việc cần làm ngay theo thứ tự ưu tiên, với ước tính thời gian sửa.

## Ví dụ gọi skill
```
Chạy technical-seo-audit với:
- domain: example.com
- sitemap_url: https://example.com/sitemap.xml
```
