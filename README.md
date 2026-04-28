# Dự án Quản lý nhân viên và Tiền lương (Topic 8)
    Sinh viên thực hiện: Chu Thị Nhung

# Giới thiệu dự án
    Dự án này là một ứng dụng quản lý nhân sự hoàn chỉnh chạy trên giao diện dòng lệnh (CLI). Mục tiêu của dự án là giải quyết bài toán quản lý thông tin nhân viên, tính toán tiền lương tự động và lưu trữ dữ liệu bền vững. Ứng dụng được thiết kế chú trọng vào tính chính xác của dữ liệu (Validation) và cấu trúc mã nguồn sạch (Clean Code).

# Cấu trúc mã nguồn (Modular Design)
    Dự án được tổ chức theo kiến trúc mô-đun để dễ dàng bảo trì và mở rộng, tránh tình trạng "Spaghetti Code":
- main.py: Đóng vai trò là bộ điều phối chính (Controller). Chứa vòng lặp tương tác người dùng và điều hướng các chức năng.
- functions.py: Thư viện nghiệp vụ. Chứa toàn bộ logic xử lý dữ liệu, các thuật toán tìm kiếm, sắp xếp, thống kê và các hàm đọc/ghi file.
- employees.json: Cơ sở dữ liệu của hệ thống, lưu trữ thông tin dưới dạng cấu trúc JSON chuyên nghiệp thay vì file văn bản thô.

# Chức năng:
- Thêm nhân viên mới: Nhập ID, họ tên, và hệ số lương với cơ chế kiểm tra lỗi nhập liệu.
- Hiển thị danh sách: Xuất bảng dữ liệu được căn lề ngay ngắn, dễ quan sát.
- Tìm kiếm nâng cao: Hỗ trợ tìm kiếm theo ID hoặc tìm kiếm một phần tên (Substring Search).
- Thống kê báo cáo: Tính tổng quỹ lương, lương trung bình và phân loại nhân viên theo mức lương.
- Lưu & Thoát: Tự động đồng bộ dữ liệu vào file JSON trước khi đóng chương trình.

# Cách khởi chạy chương trình
    Yêu cầu máy tính đã cài đặt Python 3.x.
    Mở thư mục dự án trong Terminal hoặc Command Prompt.
    Chạy lệnh:
    Bash
    python main.py

# Các tính năng nâng cao (Advanced Features)
-   Xử lý ngoại lệ (Error Handling): Sử dụng try-except để ngăn chặn chương trình bị sập khi người dùng nhập sai định dạng số hoặc file dữ liệu bị lỗi.
-   Dữ liệu cấu trúc JSON: Sử dụng thư viện json để đảm bảo dữ liệu được lưu trữ có kiểu (Data Type) rõ ràng, giúp việc xuất/nhập dữ liệu luôn chính xác.
-   Thống kê phân nhóm (Grouped Statistics): Tự động phân loại nhân viên theo hệ số lương (Hệ số cao >= 5.0 và Hệ số thấp < 5.0) để hỗ trợ quản lý ra quyết định.

# Quá trình làm việc (Workflow & Git)
    Sử dụng Git để quản lý phiên bản với hơn 10 lần Commit (Atomic Commits). Mỗi lần thêm một tính năng hoặc sửa một lỗi nhỏ đều được ghi nhận lại minh bạch.
    Áp dụng quy tắc Indentation và Comment rõ ràng để mã nguồn dễ đọc nhất cho người khác khi tiếp cận.

# TỰ ĐÁNH GIÁ THEO THANG ĐIỂM : 10 điểm
1. Hệ thống Menu CLI (1.0đ): Hoàn thành. ( Vòng lặp while True và xử lý lựa chọn sai trong main.py).
2. Nhập & Xác thực dữ liệu (1.0đ): Hoàn thành. (try-except ValueError trong hàm input_employee()).
3. Hiển thị dữ liệu (1.0đ): Hoàn thành. ( Định dạng bảng bằng f-string trong display_employees()).
4. Tìm kiếm cơ bản (1.0đ): Hoàn thành. ( Tìm kiếm chính xác ID trong hàm search_employee()).
5. Cơ chế Sắp xếp (1.0đ): Hoàn thành. ( Sử dụng .sort() và lambda để sắp xếp theo Lương/Tên).
6. Tính toán cơ bản (1.0đ): Hoàn thành. ( Hàm show_stats() tính đúng Tổng và Trung bình lương).
7. Xử lý tệp tin (1.0đ): Hoàn thành. ( Hàm load_employees() và save_employees() hoạt động ổn định).
8. Logic phức tạp nâng cao (1.0đ): Hoàn thành. (Thống kê phân nhóm nhân viên theo hệ số lương).
9. Cấu trúc dữ liệu JSON (1.0đ): Hoàn thành. ( Sử dụng tệp .json  thay vì file .txt).
10. Git & Cấu trúc Mô-đun (1.0đ): Hoàn thành. ( Chia file rõ ràng, có README chi tiết và 10+ commits trên GitHub).
