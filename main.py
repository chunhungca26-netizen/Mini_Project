from functions import *

def main():
    # Tải dữ liệu khi khởi động 
    employees = load_employees()
    
    while True: 
        print("\n1. Thêm NV  2. Hiện bảng  3. Tìm kiếm  4. Thống kê  0. Thoát")
        choice = input("Chọn chức năng (0-4): ")
        
        if choice == '1':      # Chức năng thêm nv
            employees.append(input_employee())
            save_employees(employees) # Lưu tự động
        elif choice == '2':    # Chức năng hiển thị nv
            display_employees(employees)
        elif choice == '3':    # Chức năng tìm kiếm 
            search_employee(employees)
        elif choice == '4':
            show_stats(employees)
        elif choice == '0':
            save_employees(employees)
            print("Đã lưu dữ liệu. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()