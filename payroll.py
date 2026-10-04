from typing import List, Optional
from employee.employee import Employee


class Payroll:

    def __init__(self, period: str):
        if not period or not period.strip():
            raise ValueError("Kỳ lương không được rỗng.")
        self.__period = period.strip()
        self.__employees: List[Employee] = []

    @property
    def period(self) -> str:
        return self.__period

    @property
    def employees(self) -> List[Employee]:
        return list(self.__employees)

    def add_employee(self, employee: Employee) -> None:
        if not isinstance(employee, Employee):
            raise TypeError("Chỉ thêm đối tượng thuộc lớp Employee.")
        if self.find_employee(employee.employee_id) is not None:
            raise ValueError(
                f"Mã nhân sự {employee.employee_id} đã tồn tại trong bảng lương."
            )
        self.__employees.append(employee)

    def find_employee(self, employee_id: str) -> Optional[Employee]:
        for emp in self.__employees:
            if emp.employee_id == employee_id:
                return emp
        return None

    def calculate_total_payroll(self) -> float:
        # Gọi calculate_gross_pay() qua kiểu chung Employee -> đa hình
        return sum(emp.calculate_gross_pay() for emp in self.__employees)

    def calculate_payroll_by_department(self, department: str) -> float:
        return sum(
            emp.calculate_gross_pay()
            for emp in self.__employees
            if emp.department.lower() == department.lower()
        )

    def find_highest_paid_employee(self) -> Optional[Employee]:
        if not self.__employees:
            return None
        return max(self.__employees, key=lambda e: e.calculate_gross_pay())

    def display_payroll(self) -> None:
        print(f"\n===== BẢNG LƯƠNG KỲ {self.__period} =====")
        if not self.__employees:
            print("(Danh sách rỗng)")
            return
        for emp in self.__employees:
            print(emp.display_payroll_info())
            print("-" * 60)
        print(f"TỔNG BẢNG LƯƠNG: {self.calculate_total_payroll():,.0f}")