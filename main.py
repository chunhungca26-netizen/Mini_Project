import os

# 1. Hàm tạo dữ liệu nhân viên 
def create_employee(emp_id, name, base_salary, work_days):
    # Lương = Lương cơ bản * (Ngày công / 26) [Yêu cầu của mày]
    total_salary = base_salary * (work_days / 26)
    return {
        "id": emp_id,
        "name": name,
        "base_salary": base_salary,
        "work_days": work_days,
        "total_salary": round(total_salary, 2)
    }

# 2. Xử lý File TXT 
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
                temp_list.append({
                    "id": data[0], "name": data[1],
                    "base_salary": float(data[2]), "work_days": int(data[3]),
                    "total_salary": float(data[4])
                })
    return temp_list

# 3. Nhập liệu có xác thực 
def input_employee():
    emp_id = input("Nhập mã NV: ")
    name = input("Nhập họ tên: ")
    while True:
        try:
            base_salary = float(input("Lương cơ bản: "))
            work_days = int(input("Ngày công (0-31): "))
            if 0 <= work_days <= 31: break
            print("Lỗi: Ngày công phải từ 0-31!")
        except ValueError:
            print("Lỗi: Vui lòng nhập số!")
    return create_employee(emp_id, name, base_salary, work_days)

# 4. Menu chính 
def main():
    employees = load_from_txt()
    while True:
        print("\n1. Thêm NV | 2. Hiện List (Thô) | 0. Thoát")
        choice = input("Chọn: ")
        if choice == '1':
            employees.append(input_employee())
            save_to_txt(employees)
        elif choice == '2':
            print(employees)
        elif choice == '0':
            save_to_txt(employees)
            break

if __name__ == "__main__":
    main()