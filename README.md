# Hub Video Cấp Tốc 2026

Đây là Hub phân phối video khóa Cấp Tốc, được thiết kế với giao diện Space/Sci-Fi hiện đại và quy trình tự động hoàn toàn bằng Python + CSV.

## Quy trình làm việc hàng ngày

1. **Thêm/Sửa Video:** Mở file `quan_ly_video.csv` bằng Excel hoặc Text Editor. Chỉnh sửa ID Youtube, tên bài, hoặc bật/tắt bài học (Cột `Trang_Thai` để "Hien" hoặc "An").
2. **Build và Đồng bộ (1-click):** Chỉ cần nhấp đúp vào file `Sync_Len_Web.bat`.
   - Hệ thống sẽ gọi `build_video.py` để lấy dữ liệu từ CSV, nhúng vào `template.txt` và tự động tạo ra file `index.html` hoàn chỉnh.
   - Hệ thống sẽ tự động commit và push toàn bộ lên kho chứa Github (`videocaptoc26`).

## Cấu trúc file quan trọng

- `quan_ly_video.csv`: Dữ liệu trung tâm (Nguồn sống của giao diện).
- `template.txt`: Khung giao diện tĩnh (Chứa toàn bộ CSS Tailwind và giao diện gốc).
- `build_video.py`: Script build (Đọc CSV và nạp vào template).
- `index.html`: File cuối cùng xuất ra web. **CẢNH BÁO: KHÔNG sửa trực tiếp file này vì mỗi lần chạy build nó sẽ bị ghi đè!**
- `Sync_Len_Web.bat`: Kịch bản tự động hoá để đẩy lên Github.
