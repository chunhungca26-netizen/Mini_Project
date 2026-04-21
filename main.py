import os

# --- 1. CẤU TRÚC DỮ LIỆU & TÍNH TOÁN ---
def create_employee(emp_id, name, base_salary, work_days):
    # Công thức tính lương thực tế 
    total_salary = base_salary * (work_days / 26)
    return {
        "id": emp_id,
        "name": name,
        "base_salary": base_salary,
        "work_days": work_days,
        "total_salary": round(total_salary, 2)
    }

# --- 2. XỬ LÝ FILE TXT  ---
def save_to_txt(employees):
    with open("employees.txt", "w", encoding="utf-8") as f:
        for e in employees:
            line = f"{e['id']}|{e['name']}|{e['base_salary']}|{e['work_days']}|{e['total_salary']}\n"
            f.write(line)

def load_from_txt():
    if not os.path.exists("employees.txt"): return []
    temp_list = []
    with open("employees.txt", "r", encoding="utf-8") as f:
        for line in f:
            data = line.strip().split("|")
            if len(data) == 5:
                try:
                    temp_list.append({
                        "id": data[0], "name": data[1],
                        "base_salary": float(data[2]), "work_days": int(data[3]),
                        "total_salary": float(data[4])
                    })
                except: continue
    return temp_list

# --- 3. HIỂN THỊ BẢNG CHUYÊN NGHIỆP  ---
def display_employees(emp_list):
    if not emp_list:
        print("\n=> Danh sách trống!")
        return
    header = f"{'ID':<10} | {'Họ Tên':<25} | {'Lương CB':<15} | {'Công':<5} | {'Lương Nhận':<15}"
    print("\n" + "="*80)
    print(header)
    print("-" * 80)
    for e in emp_list:
        print(f"{e['id']:<10} | {e['name']:<25} | {e['base_salary']:<15,.0f} | {e['work_days']:<5} | {e['total_salary']:<15,.0f}")
    print("="*80)

# --- 4. TÌM KIẾM, SẮP XẾP & XÓA  ---
def search_employee(employees):
    query = input("Nhập tên hoặc ID cần tìm: ").lower()
    found = [e for e in employees if query in e['name'].lower() or query in e['id'].lower()]
    display_employees(found)

def sort_employees(employees):
    employees.sort(key=lambda x: x['total_salary'], reverse=True)
    print("\n=> Đã sắp xếp theo lương thực nhận giảm dần!")
    display_employees(employees)

def delete_employee(employees):
    emp_id = input("Nhập Mã NV muốn xóa: ")
    for e in employees:
        if e['id'] == emp_id:
            employees.remove(e)
            save_to_txt(employees)
            print(f"=> Đã xóa thành công nhân viên {emp_id}!")
            return
    print("=> Không tìm thấy mã này.")

# --- 5. NHẬP LIỆU CÓ XÁC THỰC  ---
def input_employee():
    emp_id = input("Mã NV: ")
    name = input("Họ tên: ")
    while True:
        try:
            base_salary = float(input("Lương cơ bản (VNĐ): "))
            work_days = int(input("Ngày công (0-31): "))
            if 0 <= work_days <= 31: break
            print("Lỗi: Ngày công không hợp lệ!")
        except ValueError:
            print("Lỗi: Vui lòng nhập số!")
    return create_employee(emp_id, name, base_salary, work_days)

# --- 6. VÒNG LẶP CHÍNH (MAIN LOOP)  ---
def main():
    employees = load_from_txt()
    while True:
        print("\n1. Thêm NV  2. Hiện bảng  3. Tìm kiếm  4. Sắp xếp  5. Xóa NV  0. Thoát")
        choice = input("Chọn chức năng (0-5): ")
        if choice == '1':
            employees.append(input_employee())
            save_to_txt(employees)
        elif choice == '2':
            display_employees(employees)
        elif choice == '3':
            search_employee(employees)
        elif choice == '4':
            sort_employees(employees)
        elif choice == '5':
            delete_employee(employees)
        elif choice == '0':
            save_to_txt(employees)
            print("Đã lưu dữ liệu. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()