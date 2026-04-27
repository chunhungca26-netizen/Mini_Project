import json

# Hàm tải dữ liệu từ file JSON 
def load_employees():
    try:
        with open('employees.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Hàm lưu dữ liệu vào file JSON 
def save_employees(employees):
    with open('employees.json', 'w', encoding='utf-8') as f:
        json.dump(employees, f, ensure_ascii=False, indent=4)

# Hàm nhập liệu có xác thực
def input_employee():
    print("\n--- NHẬP THÔNG TIN NHÂN VIÊN ---")
    id_nv = input("Mã nhân viên (duy nhất): ")
    name = input("Họ và tên: ")
    while True:
        try:
            hso = float(input("Hệ số lương (1.0 - 10.0): "))
            if 1.0 <= hso <= 10.0: break
            print("Lỗi: Hệ số lương phải nằm trong khoảng 1.0 đến 10.0!")
        except ValueError:
            print("Lỗi: Vui lòng nhập số thực cho hệ số lương!")
    
    # Tính toán cơ bản
    salary = hso * 1800000  # Lương cơ bản giả định
    return {"id": id_nv, "name": name, "hso": hso, "salary": salary}

# Hàm hiển thị bảng định dạng đẹp 
def display_employees(employees):
    if not employees:
        print("\nDanh sách trống!")
        return
    print("\n" + "="*65)
    print(f"{'ID':<10} | {'Họ và Tên':<25} | {'Hệ số':<8} | {'Tổng lương':>15}")
    print("-" * 65)
    for emp in employees:
        print(f"{emp['id']:<10} | {emp['name']:<25} | {emp['hso']:<8.2f} | {emp['salary']:>15,.0f} VNĐ")
    print("="*65)

# Tìm kiếm theo chuỗi con 
def search_employee(employees):
    query = input("Nhập tên hoặc ID muốn tìm (khớp một phần): ").lower()
    results = [e for e in employees if query in e['name'].lower() or query in e['id'].lower()]
    display_employees(results)

# Thống kê cơ bản 
def show_stats(employees):
    if not employees:
        print("\nChưa có dữ liệu để thống kê!")
        return
    
    total_salary = sum(e['salary'] for e in employees)
    avg_salary = total_salary / len(employees)
    
    # Phân nhóm theo mức lương 
    high_salary = [e for e in employees if e['hso'] >= 5.0]
    low_salary = [e for e in employees if e['hso'] < 5.0]
    
    print("\n" + "="*30)
    print("      BÁO CÁO THỐNG KÊ")
    print("="*30)
    print(f"1. Tổng số nhân viên: {len(employees)}")
    print(f"2. Tổng quỹ lương:    {total_salary:,.0f} VNĐ")
    print(f"3. Lương trung bình:  {avg_salary:,.0f} VNĐ")
    print(f"4. NV lương cao (Hệ số >= 5.0): {len(high_salary)}")
    print(f"5. NV lương thấp (Hệ số < 5.0): {len(low_salary)}")
    print("="*30)