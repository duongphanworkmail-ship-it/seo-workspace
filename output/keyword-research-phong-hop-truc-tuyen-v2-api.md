# Keyword Research v2: "phòng họp trực tuyến" — Dữ liệu SerpAPI thực tế

**Nguồn:** Google Autocomplete API + Google Trends API
**Market:** Việt Nam | **Ngày:** 2026-05-10
**Raw data:** `output/kw-phong-hop-truc-tuyen-api.json`

---

## Phát hiện quan trọng từ dữ liệu thực

> API tiết lộ 2 insight lớn mà phân tích không có API đã bỏ sót:

**1. Niche thực tế là thiết bị AV, không phải phần mềm**
Autocomplete top 10 gồm: camera, micro, webcam, loa, setup → người dùng đang tìm
kiếm lắp đặt phòng họp vật lý tích hợp video, không chỉ app họp online.

**2. Chính phủ / hành chính là segment lớn**
"phòng họp trực tuyến chính phủ" (relevance: 561) và "phòng họp trực tuyến xã" (558)
xuất hiện cao → cơ quan nhà nước từ cấp xã đến trung ương là audience chính.

---

## Bảng từ khóa từ dữ liệu API

| Từ khóa | Relevance | Intent | Cluster | Ưu tiên |
|---------|-----------|--------|---------|---------|
| phòng họp trực tuyến | 1250 | C | Tổng quan | P1 |
| phòng họp trực tuyến cần những gì | 601 | I | Kiến thức & Setup | P1 |
| phòng họp trực tuyến là gì | 600 | I | Kiến thức & Setup | P1 |
| cách tạo phòng họp trực tuyến trên Google Meet | 601 | I | Hướng dẫn | P1 |
| cách tạo phòng họp trực tuyến | 600 | I | Hướng dẫn | P1 |
| phòng họp trực tuyến zoom | 600 | N | Nền tảng | P1 |
| phòng họp trực tuyến chính phủ | 561 | C | Chính phủ | P1 |
| phòng họp trực tuyến đẹp | 559 | C | Thiết kế | P1 |
| phòng họp trực tuyến xã | 558 | C | Chính phủ | P2 |
| camera phòng họp trực tuyến | 557 | T | Thiết bị AV | P1 |
| micro phòng họp trực tuyến | 556 | T | Thiết bị AV | P1 |
| setup phòng họp trực tuyến | 555 | I | Thiết bị AV | P1 |
| webcam phòng họp trực tuyến | 554 | T | Thiết bị AV | P1 |
| loa phòng họp trực tuyến | 553 | T | Thiết bị AV | P1 |
| tạo phòng họp trực tuyến | 552 | T | Hướng dẫn | P1 |
| mẫu phòng họp trực tuyến | 550 | C | Thiết kế | P2 |
| camera phòng họp trực tuyến hikvision ds mego 202ptz | 551 | T | Thiết bị AV | P2 |
| cách lắp đặt phòng họp trực tuyến | 554 | I | Thiết kế | P2 |
| cách thiết lập phòng họp trực tuyến | 553 | I | Thiết kế | P2 |
| làm phòng họp trực tuyến | 551 | I | Thiết kế | P2 |
| phòng họp là gì | 550 | I | Kiến thức & Setup | P3 |

---

## Phân tích Trend 12 tháng (Thực tế)

| Giai đoạn | Keyword | Điểm | Nhận xét |
|-----------|---------|------|---------|
| Aug 17–23, 2025 | phòng họp trực tuyến | 100 | Đỉnh cao — sự kiện chuyển đổi số |
| Aug 17–23, 2025 | phòng họp trực tuyến chính phủ | 93 | Spike đồng thời → nguyên nhân từ chính phủ |
| Sep 7–13, 2025 | phong hop truc tuyen (không dấu) | 97 | Người dùng tìm không dấu |
| Dec 14–20, 2025 | phòng họp trực tuyến | 87 | Cuối năm, tổng kết |
| May 3–9, 2026 | phòng họp trực tuyến | 29 | Đang tăng nhẹ gần đây |

**Kết luận:** Demand theo đợt/sự kiện, không phải evergreen. Cần theo dõi tin tức
chính phủ về chuyển đổi số để bắt kịp spike.

---

## Topic Cluster — Điều chỉnh theo dữ liệu thực

```
[PILLAR] phòng họp trực tuyến
    ├── [C1] Kiến thức & Yêu cầu setup
    │         "là gì", "cần những gì"
    ├── [C2] Thiết bị AV (cluster lớn nhất — API xác nhận)
    │         camera, micro, webcam, loa, setup
    ├── [C3] Hướng dẫn tạo phòng họp
    │         "cách tạo", "cách thiết lập", Google Meet/Zoom
    ├── [C4] Thiết kế & Thi công
    │         "phòng họp đẹp", "mẫu", "lắp đặt"
    ├── [C5] Chính phủ & Hành chính (segment đặc thù VN)
    │         "chính phủ", "cấp xã", "cơ quan nhà nước"
    └── [C6] Nền tảng cụ thể
              Zoom, Google Meet, Microsoft Teams
```

---

## So sánh: API vs Phân tích thuần Claude

| Điểm | Phân tích thuần Claude | Dữ liệu API (thực tế) |
|------|----------------------|----------------------|
| Niche chính | Phần mềm video conferencing | Thiết bị AV + lắp đặt phòng họp |
| Audience | Doanh nghiệp tổng quát | Chính phủ + cơ quan nhà nước |
| Cluster quan trọng | So sánh Zoom/Meet/Teams | Thiết bị AV (camera, micro, loa) |
| Search pattern | Evergreen | Spike theo sự kiện/chính sách |
| Từ khóa bỏ sót | — | camera Hikvision, phòng họp xã, setup AV |

---

## Top 5 từ khóa P1 ưu tiên

| # | Từ khóa | Relevance | Lý do |
|---|---------|-----------|-------|
| 1 | phòng họp trực tuyến cần những gì | 601 | KD thấp, dẫn vào cluster thiết bị AV |
| 2 | setup phòng họp trực tuyến | 555 | Hub toàn bộ cluster thiết bị |
| 3 | camera phòng họp trực tuyến | 557 | Transactional, conversion cao |
| 4 | phòng họp trực tuyến chính phủ | 561 | B2G ít cạnh tranh, spike mạnh |
| 5 | cách tạo phòng họp trực tuyến | 600 | Entry point đầu phễu |
