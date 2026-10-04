from employee.employee import Employee
from employee.hourly_employee import HourlyEmployee
from employee.salaried_employee import SalariedEmployee
from employee.sales_employee import SalesEmployee
from payroll import Payroll

def main():
    payroll = Payroll("2026-09")

    # E001 - SalariedEmployee
    # Constructor đầy đủ
    e1 = SalariedEmployee(
        employee_id="E001",
        full_name="Nguyễn Minh An",
        department="Đào tạo",
        monthly_salary=15_000_000,
        responsibility_allowance=2_000_000
    )
    e1.add_bonus(1_000_000)  # add_bonus(amount)
    payroll.add_employee(e1)

    # E002 - HourlyEmployee, không vượt ngưỡng
    e2 = HourlyEmployee(
        employee_id="E002",
        full_name="Trần Thu Bình",
        department="Hỗ trợ",
        hourly_rate=100_000,
        worked_hours=150
    )
    e2.add_bonus(500_000)  # add_bonus(amount)
    payroll.add_employee(e2)

    # E003 - HourlyEmployee, có vượt ngưỡng
    e3 = HourlyEmployee(
        employee_id="E003",
        full_name="Lê Hoàng Chi",
        department="Hỗ trợ",
        hourly_rate=100_000,
        worked_hours=170
    )
    # Không thưởng
    payroll.add_employee(e3)

    # E004 - SalesEmployee
    e4 = SalesEmployee(
        employee_id="E004",
        full_name="Phạm Quốc Dũng",
        department="Kinh doanh",
        base_salary=8_000_000,
        sales_revenue=200_000_000,
        commission_rate=0.05
    )
    # add_bonus(rate, reference_amount, reason) -> 2% của 50.000.000
    e4.add_bonus(0.02, 50_000_000, "Thưởng theo tỷ lệ doanh số")
    payroll.add_employee(e4)

    # Hiển thị bảng lương
    payroll.display_payroll()

    # Kiểm tra các giá trị mong đợi
    print("\n===== KIỂM TRA KẾT QUẢ =====")
    print(f"E001 thu nhập: {e1.calculate_gross_pay():,.0f} ")
    print(f"E002 thu nhập: {e2.calculate_gross_pay():,.0f} ")
    print(f"E003 thu nhập: {e3.calculate_gross_pay():,.0f}")
    print(f"E004 thu nhập: {e4.calculate_gross_pay():,.0f} ")
    print(f"Tổng bảng lương: {payroll.calculate_total_payroll():,.0f} ")
    print(f"Tổng phòng Hỗ trợ: {payroll.calculate_payroll_by_department('Hỗ trợ'):,.0f} ")

    highest = payroll.find_highest_paid_employee()
    if highest:
        print(f"Nhân sự thu nhập cao nhất: {highest.full_name} - {highest.calculate_gross_pay():,.0f}")


if __name__ == "__main__":
    main()