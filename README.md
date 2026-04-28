**1.Dự án Quản lý nhân viên và Tiền lương (Topic 8)**
    Sinh viên thực hiện: Chu Thị Nhung

**2.  Giới thiệu dự án**

Dự án này là một ứng dụng quản lý nhân sự hoàn chỉnh chạy trên giao diện dòng lệnh (CLI). Mục tiêu của dự án là giải quyết bài toán quản lý thông tin nhân viên, tính toán tiền lương tự động và lưu trữ dữ liệu bền vững. Ứng dụng được thiết kế chú trọng vào tính chính xác của dữ liệu (Validation) và cấu trúc mã nguồn sạch (Clean Code).


**3. Mục tiêu dự án**
 
 - Giúp nhà quản lý theo dõi thông tin nhân viên và bảng lương một cách chính xác.
   - Tự động hóa việc tính lương dựa trên hệ số và lương cơ bản.
   - Hỗ trợ ra quyết định thông qua các số liệu thống kê tài chính.
   - Đảm bảo dữ liệu được lưu trữ để tái sử dụng cho các lần chạy sau.
   - Thực hành tư duy lập trình mô-đun và tổ chức mã nguồn sạch sẽ.
   

**4. Các file trong dự án**

     - main.py: Bộ điều phối chính (Controller). Chứa vòng lặp tương tác người dùng và điều hướng các chức năng.
    - functions.py: Thư viện nghiệp vụ. Chứa toàn bộ logic xử lý: Nhập, Xuất, Tìm kiếm, Sắp xếp, Thống kê, Xóa, Sửa.
    - employees.json: Cơ sở dữ liệu của hệ thống, lưu trữ dữ liệu dưới dạng cấu trúc.
    - README.md: Tài liệu hướng dẫn, báo cáo và tự đánh giá dự án.


**5. Cấu trúc thư mục dự án**
  

Plaintext
    QUAN-LY-LUONG-NHAN-VIEN/
    |-- main.py           (Mã nguồn chính)
    |-- employees.txt    (Cơ sở dữ liệu file văn bản)
    |-- employees.json   (File xuất dữ liệu JSON)
    |-- README.md        (Mô tả và tự đánh giá)

**6.  Cấu trúc mã nguồn (Modular Design)**
 

 Dự án được tổ chức theo kiến trúc mô-đun để dễ dàng bảo trì và mở rộng, tránh tình trạng "Spaghetti Code":
- main.py: Đóng vai trò là bộ điều phối chính (Controller). Chứa vòng lặp tương tác người dùng và điều hướng các chức năng.
- functions.py: Thư viện nghiệp vụ. Chứa toàn bộ logic xử lý dữ liệu, các thuật toán tìm kiếm, sắp xếp, thống kê và các hàm đọc/ghi file.
- employees.json: Cơ sở dữ liệu của hệ thống, lưu trữ thông tin dưới dạng cấu trúc JSON chuyên nghiệp thay vì file văn bản thô.

**7. Các hàm chính trong chương trình**

| Tên hàm | Vai trò |
|:---|:---|
| `display_menu()` | Hiển thị giao diện menu chính |
| `load_from_txt()` | Đọc dữ liệu từ file `employees.txt` |
| `save_to_txt()` | Ghi dữ liệu vào file `employees.txt` |
| `export_to_json()` | Xuất danh sách ra file JSON chuyên nghiệp |
| `calculate_salary()` | Công thức tính: Hệ số * Lương cơ bản |
| `add_employee()` | Nhập liệu và xác thực nhân viên mới |
| `display_payroll()` | In bảng lương định dạng đẹp |
| `show_statistics()` | Tính toán tổng quỹ lương và trung bình |
| `main()` | Điều khiển luồng chạy chính của ứng dụng |

**8.  Chức năng**

- Thêm nhân viên mới: Nhập ID, họ tên, và hệ số lương với cơ chế kiểm tra lỗi nhập liệu.
- Hiển thị danh sách: Xuất bảng dữ liệu được căn lề ngay ngắn, dễ quan sát.
- Tìm kiếm nâng cao: Hỗ trợ tìm kiếm theo ID hoặc tìm kiếm một phần tên (Substring Search).
- Thống kê báo cáo: Tính tổng quỹ lương, lương trung bình và phân loại nhân viên theo mức lương.
- Lưu & Thoát: Tự động đồng bộ dữ liệu vào file JSON trước khi đóng chương trình.

**9. Tính năng nâng cao đã triển khai**

 Tìm kiếm theo từ khóa (Substring Match)
Người dùng có thể nhập một phần tên để tìm nhân viên. 
Ví dụ: nhập "Chu" sẽ tìm thấy "Chu Thị Nhung". Điều này đáp ứng yêu cầu Logic phức tạp.

**10. Kiểm tra dữ liệu (Validation)**

| Dữ liệu | Quy tắc kiểm tra |
|:---|:---|
| **Mã nhân viên** | Không được để trống / Không được trùng lặp trong hệ thống |
| **Họ và tên** | Không được để trống |
| **Hệ số lương** | Phải là số thực hoặc số nguyên (Ví dụ: từ 1.0 đến 10.0) |
| **Lựa chọn menu** | Phải nằm trong khoảng từ 0-9; có xử lý lỗi (try-except) nếu nhập chữ |

**11.  Cách khởi chạy chương trình** 
    
    Yêu cầu máy tính đã cài đặt Python 3.x.
    Mở thư mục dự án trong Terminal hoặc Command Prompt.
    Mở file main.py.
    Nhấn nút Run.
    Sử dụng các chức năng theo menu hiển thị trong cửa sổ console.

**12. Menu chương trình**
Khi chạy chương trình, hệ thống sẽ hiển thị menu như sau:

1. Thêm NV  2. Hiện bảng    3. Tìm kiếm     4. Thống kê     0. Thoát

======================================================================
ID           | Họ và Tên                 | Hệ số   |        Tổng lương
======================================================================
24s700       | Chu Thị Nhung             | 2.60    |     4,680,000 VNĐ
24s190       | Trần Đức Hiếu             | 3.00    |     5,400,000 VNĐ

======================================================================

**13.  Các tính năng nâng cao (Advanced Features)**

-   Xử lý ngoại lệ (Error Handling): Sử dụng try-except để ngăn chặn chương trình bị sập khi người dùng nhập sai định dạng số hoặc file dữ liệu bị lỗi.
-   Dữ liệu cấu trúc JSON: Sử dụng thư viện json để đảm bảo dữ liệu được lưu trữ có kiểu (Data Type) rõ ràng, giúp việc xuất/nhập dữ liệu luôn chính xác.
-   Thống kê phân nhóm (Grouped Statistics): Tự động phân loại nhân viên theo hệ số lương (Hệ số cao >= 5.0 và Hệ số thấp < 5.0) để hỗ trợ quản lý ra quyết định.

**14.  Quá trình làm việc (Workflow & Git)**

    Sử dụng Git để quản lý phiên bản với hơn 10 lần Commit (Atomic Commits). Mỗi lần thêm một tính năng hoặc sửa một lỗi nhỏ đều được ghi nhận lại minh bạch.
    Áp dụng quy tắc Indentation và Comment rõ ràng để mã nguồn dễ đọc nhất cho người khác khi tiếp cận.

**15. TỰ ĐÁNH GIÁ THEO THANG ĐIỂM : 10 điểm**

| STT | Tiêu chí | Trạng thái | Minh chứng | Điểm |
|:---:|:---|:---:|:---|:---:|
| 1 | Menu CLI | Hoàn thành | Vòng lặp while True tại main.py | 1.0 |
| 2 | Nhập dữ liệu | Hoàn thành | try-except ValueError | 1.0 |
| 3 | Hiển thị | Hoàn thành | Định dạng f-string bảng | 1.0 |
| 4 | Tìm kiếm | Hoàn thành | Search theo ID | 1.0 |
| 5 | Sắp xếp | Hoàn thành | Dùng .sort() và lambda | 1.0 |
| 6 | Tính toán | Hoàn thành | Tính tổng và trung bình lương | 1.0 |
| 7 | File TXT | Hoàn thành | load/save employees.txt | 1.0 |
| 8 | Logic cao | Hoàn thành | Tìm gần đúng tên nhân viên | 1.0 |
| 9 | File JSON | Hoàn thành | Xuất file employees.json | 1.0 |
| 10 | Git/Module | Hoàn thành | Chia file, README, 10+ commits | 1.0 |
| | **TỔNG CỘNG** | | | **10.0** |

