from employee.employee import Employee
from employee.hourly_employee import HourlyEmployee
from employee.salaried_employee import SalariedEmployee
from employee.sales_employee import SalesEmployee
from payroll import Payroll


def test_boundary():
    print("===== KIỂM THỬ BIÊN (10 TÌNH HUỐNG) =====")

    # 1. Mã nhân sự rỗng
    try:
        SalariedEmployee("", "A")
        print(" 1. Mã rỗng: Không báo lỗi")
    except ValueError:
        print(" 1. Mã rỗng: Báo lỗi đúng")

    # 2. Thưởng âm
    e = SalariedEmployee("E1", "A", "P", 1_000_000, 0)
    try:
        e.add_bonus(-100)
        print(" 2. Thưởng âm: Không báo lỗi")
    except ValueError:
        print(" 2. Thưởng âm: Báo lỗi đúng")

    # 3. Tỷ lệ thưởng = 0
    try:
        e.add_bonus(0, 100_000, "x")
        print(" 3. Tỷ lệ = 0: Không báo lỗi")
    except ValueError:
        print(" 3. Tỷ lệ = 0: Báo lỗi đúng")

    # 4. Tỷ lệ thưởng > 0.5
    try:
        e.add_bonus(0.6, 100_000, "x")
        print(" 4. Tỷ lệ > 0.5: Không báo lỗi")
    except ValueError:
        print(" 4. Tỷ lệ > 0.5: Báo lỗi đúng")

    # 5. Giờ làm > 250
    try:
        HourlyEmployee("H1", "A", "P", 100_000, 251)
        print(" 5. Giờ > 250: Không báo lỗi")
    except ValueError:
        print(" 5. Giờ > 250: Báo lỗi đúng")

    # 6. Hoa hồng > 0.3
    try:
        SalesEmployee("S1", "A", "P", 1_000_000, 100, 0.31)
        print(" 6. Hoa hồng > 0.3: Không báo lỗi")
    except ValueError:
        print(" 6. Hoa hồng > 0.3: Báo lỗi đúng")

    # 7. Trùng mã trong Payroll
    payroll = Payroll("2026-09")
    payroll.add_employee(SalariedEmployee("E1", "A", "P", 1_000_000, 0))
    try:
        payroll.add_employee(SalariedEmployee("E1", "B", "Q", 1_000_000, 0))
        print(" 7. Trùng mã: Không báo lỗi")
    except ValueError:
        print(" 7. Trùng mã: Báo lỗi đúng")

    # 8. Giờ làm = 160 (đúng ngưỡng)
    h160 = HourlyEmployee("H160", "A", "P", 100_000, 160)
    assert h160.calculate_gross_pay() == 16_000_000
    print(" 8. Giờ = 160: Lương = 16.000.000")

    # 9. Giờ làm = 250 (biên trên hợp lệ)
    h250 = HourlyEmployee("H250", "A", "P", 100_000, 250)
    expected = 160 * 100_000 + 90 * 100_000 * 1.5  # = 29.500.000
    assert h250.calculate_gross_pay() == expected
    print(f" 9. Giờ = 250: Lương = {expected:,.0f}")

    # 10. Payroll rỗng
    empty = Payroll("2026-10")
    assert empty.calculate_total_payroll() == 0
    assert empty.find_highest_paid_employee() is None
    print(" 10. Payroll rỗng: Tổng = 0, người cao nhất = None")


if __name__ == "__main__":
    test_boundary()