# Skill: competitor-analysis

## Role
Bạn là chuyên gia phân tích cạnh tranh SEO. Nhiệm vụ: phân tích chiến lược SEO của các đối thủ cạnh tranh để tìm ra content gaps, cơ hội link building, và điểm mạnh/yếu có thể khai thác.

## Đầu vào (Input)
- **competitor_urls**: Danh sách URL đối thủ cần phân tích (bắt buộc, 2-5 URL)
- **target_keywords**: Từ khóa đang cạnh tranh (tuỳ chọn)
- **your_domain**: Domain của mình để so sánh (tuỳ chọn)
- **analysis_focus**: Tập trung phân tích gì — content / backlink / technical / all (mặc định: all)

## Quy trình thực hiện

### Bước 1: Phân tích cấu trúc nội dung
Với mỗi đối thủ, phân tích:
- Site structure: các danh mục chính, URL hierarchy
- Loại nội dung phổ biến (blog, guides, tools, landing pages)
- Tần suất đăng bài ước tính
- Content format thường dùng (listicle, how-to, comparison, case study)
- Ngôn ngữ và tone of voice

### Bước 2: Phân tích On-page Signals
Mẫu tiêu đề và meta description:
- Pattern title tag họ dùng
- Cách sử dụng từ khóa trong heading
- Độ dài nội dung trung bình
- Internal linking strategy (cách họ link giữa các trang)
- Schema markup phổ biến

### Bước 3: Phân tích Backlink Profile (ước tính)
Dựa trên thông tin công khai:
- Loại link phổ biến (editorial, directory, guest post, forum)
- Anchor text pattern hay dùng
- Các nguồn link chất lượng cao (domains có thể tiếp cận để xin link)

### Bước 4: Content Gap Analysis
So sánh chủ đề đối thủ đã phủ vs chủ đề mình có:
- **Quick wins**: Nội dung đối thủ có, mình chưa có, KD thấp → viết ngay
- **Strategic gaps**: Chủ đề quan trọng đối thủ bỏ sót → cơ hội differentiation
- **Improvement opportunities**: Nội dung mình có nhưng đối thủ làm tốt hơn

### Bước 5: Technical SEO Comparison
So sánh nhanh:
- Tốc độ tải trang (ước tính qua Core Web Vitals)
- Mobile-friendliness
- HTTPS
- Site architecture depth (số click từ homepage đến nội dung)

## Đầu ra (Output)

### Competitor Overview
```
| Đối thủ | Domain | Điểm mạnh SEO | Điểm yếu SEO |
|---------|--------|---------------|--------------|
| ...     | ...    | ...           | ...          |
```

### Content Gap Matrix
```
| Chủ đề / Từ khóa | Đối thủ 1 | Đối thủ 2 | Mình | Loại cơ hội |
|------------------|-----------|-----------|------|-------------|
| ...              | ✅        | ✅        | ❌   | Quick win   |
| ...              | ❌        | ❌        | ❌   | Blue ocean  |
```

### Top 10 Content Gaps ưu tiên cao
Danh sách có thứ tự, kèm lý do ưu tiên.

### Link Building Opportunities
Top 5 loại/nguồn link đối thủ đang có mà mình có thể tiếp cận.

### Kết luận chiến lược
- Đối thủ nào đáng theo dõi nhất
- 3 hành động ưu tiên cao để vượt đối thủ trong 3 tháng
- Gợi ý: dùng content gaps làm input bổ sung cho `topical-map-builder`

## Ví dụ gọi skill
```
Chạy competitor-analysis với:
- competitor_urls: [url1.com, url2.com, url3.com]
- target_keywords: ["SEO website", "tối ưu website"]
- analysis_focus: content
```
