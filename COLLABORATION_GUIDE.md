# Cẩm Nang Phối Hợp Dự Án & Cộng Tác Kỹ Thuật (Collaboration Guide)

Cẩm nang này hướng dẫn các thành viên trong ban tổ chức, đội ngũ thiết kế (Designers), lập trình viên (Developers), và đội ngũ sản xuất nội dung (Content/Marketing) cùng làm việc đồng bộ trên kho mã nguồn **Diễn đàn M&A Miền Trung 2026**.

---

## 1. Nguyên Tắc Quản Trị Nội Dung (Single Source of Truth)

Toàn bộ thông tin văn bản, lịch trình, số liệu, thông tin diễn giả và đối tác đều được quản trị tập trung tại:
👉 **`vmaa_draft_content_config.json`**

### Cấu trúc file cấu hình:
```json
{
  "event_meta": {
    "title_main": "M&A 2026",
    "title_sub": "MIỀN TRUNG",
    "topic_vn": "KIẾN TRÚC GIÁ TRỊ: BẤT ĐỘNG SẢN × CÔNG NGHỆ",
    "topic_en": "ARCHITECTURE OF VALUE: REAL ESTATE × TECHNOLOGY",
    "date": "13.12.2026",
    "time": "13:30 – 17:30",
    "location": "Đà Nẵng, Việt Nam",
    "venue": "Ariyana Convention Centre / Grand Ballroom",
    "organizer": "VMAA · Central Vietnam Chapter"
  },
  "speakers": [ ... ],
  "sponsors": { ... }
}
```
**Khi có thay đổi:**
- Không sửa chay trên từng file ảnh hoặc script riêng lẻ.
- Sửa trực tiếp trong `vmaa_draft_content_config.json`, sau đó chạy lại lệnh build. Tất cả file từ Key Visual, Social Media, Slides đến Poster Diễn giả sẽ tự động cập nhật đồng loạt.

---

## 2. Quy Trình Làm Việc Dành Cho Designer

### 2.1. Thay đổi hoặc bổ sung Logo nhà tài trợ & Đối tác
1. Đặt file logo (ưu tiên định dạng `.svg` hoặc `.png` nền trong suốt RGBA sắc nét) vào thư mục `assets/`.
2. Mở file `build_vmaa_next_forum_format.py` hoặc `build_social_landing_slide_suite.py`.
3. Khai báo data URI cho logo mới:
   ```python
   u_sponsor_logo = to_data_uri(PROJECT_DIR / "assets" / "ten_logo_moi.png")
   ```
4. Gán biến `u_sponsor_logo` vào vị trí tương ứng trong thẻ `<img>`.

### 2.2. Cập nhật ảnh chân dung Diễn giả (Speaker Portraits)
1. Trong file `build_vmaa_next_forum_format.py`, danh sách `SPEAKERS` chứa mảng các diễn giả:
   ```python
   SPEAKERS = [
       {
           "name": "HỌ VÀ TÊN DIỄN GIẢ",
           "role": "Chức vụ chính",
           "sub": "Đơn vị công tác / Chức danh kiêm nhiệm",
           "avatar_path": "assets/speakers/speaker_01.png"
       },
       ...
   ]
   ```
2. Nếu có ảnh chụp thật, thay hàm `generate_avatar_svg` bằng thẻ `<img>` trỏ đến ảnh thật, hệ thống sẽ tự động bo tròn và phủ viền hào quang phát sáng (dual-ring glowing halo).

### 2.3. Tinh chỉnh màu sắc ("Loan Loan" Palette Tuning)
Nếu muốn điều chỉnh sắc độ tím hoặc cobalt, can thiệp vào các biến CSS trong `build_vmaa_6_options.py`:
- Ánh tím hoàng gia: `#6B2D9B`
- Ánh tím điện tử: `#9B4DFF`
- Ánh tím oải hương: `#E9D5FF`
- Ánh cobalt công nghệ: `#245BFF`
- Ánh xanh băng: `#63B4FF`
- Luôn giữ `mix-blend-mode: screen;` cho các lớp aurora gradient để ánh sáng không bị đục hoặc che khuất hình khối 3D bên dưới.

---

## 3. Quy Trình Dành Cho Motion Graphics & Video Editors

### 3.1. Làm việc với Blender 3D (`blender_architecture_of_value.py`)
File script tạo hình 3D procedural trong Blender:
```bash
blender --background --python blender_architecture_of_value.py
```
- Tự động tạo khối pha lê trung tâm (Monolith), các thanh lam tán sắc (Fluted glass caustics), hệ thống camera chuyển động dọc theo trục Z và nguồn sáng thể tích (Volumetric point lights).
- Render ra chuỗi ảnh EXR/PNG 32-bit màu để đưa vào DaVinci Resolve hoặc After Effects.

### 3.2. Xuất video bằng FFmpeg
Pipeline `build_vmaa_6_options.py` sử dụng OpenCV và FFmpeg nội suy chuyển động 30fps:
- Video xuất chuẩn H.264 (MP4) và VP9 (WebM) với bitrate 5.5 Mbps, âm thanh stereo 48kHz.
- Để thay file âm thanh mở màn, thay thế file `videos/opener_audio.wav`.

---

## 4. Quy Trình Dành Cho Web Developers (Frontend & Landing Page)

- **`landing_page.html`:** Chạy độc lập, không phụ thuộc vào framework nặng, tối ưu tải trang cực nhanh (Core Web Vitals điểm 99+). Tích hợp sẵn form đăng ký vé VIP và responsive hoàn toàn trên iPhone/Android/Desktop.
- **`index.html`:** WebGL 3D tương tác. Có thể tích hợp nhúng (embed `<iframe>`) vào bất kỳ website sự kiện nào của VMAA.

---

## 5. Quy Chuẩn Đặt Tên Nhánh & Commit Git

Khi làm việc nhóm qua Git:
```bash
# Tạo nhánh mới cho tính năng hoặc cập nhật tài sản
git checkout -b feature/update-sponsor-logos
# hoặc
git checkout -b design/adjust-speaker-portraits

# Commit rõ ràng
git commit -m "feat(sponsors): update Diamond sponsor logo and tier labels"

# Push lên repo private
git push origin feature/update-sponsor-logos
```
Mọi thay đổi trên nhánh `main` / `master` phải đảm bảo chạy lệnh test render không có lỗi cú pháp Python.
