from .employee import Employee


class SalariedEmployee(Employee):

    def __init__(self, employee_id: str, full_name: str,
                 department: str = "Unassigned",
                 monthly_salary: float = 0.0,
                 responsibility_allowance: float = 0.0):
        # Constructor ủy quyền: gọi constructor của lớp cha
        super().__init__(employee_id, full_name, department)
        self._validate_non_negative(monthly_salary, "Lương tháng")
        self._validate_non_negative(responsibility_allowance, "Phụ cấp trách nhiệm")
        self.__monthly_salary = monthly_salary
        self.__responsibility_allowance = responsibility_allowance

    @property
    def monthly_salary(self) -> float:
        return self.__monthly_salary

    @property
    def responsibility_allowance(self) -> float:
        return self.__responsibility_allowance

    @staticmethod
    def _validate_non_negative(value: float, name: str) -> None:
        if value < 0:
            raise ValueError(f"{name} không được âm.")

    def calculate_gross_pay(self) -> float:
        return (self.__monthly_salary
                + self.__responsibility_allowance
                + self.monthly_bonus)

    def get_employee_type(self) -> str:
        return "SalariedEmployee"

    def display_payroll_info(self) -> str:
        return (
            f"{super().display_payroll_info()}\n"
            f"    Lương tháng: {self.__monthly_salary:,.0f} | "
            f"Phụ cấp: {self.__responsibility_allowance:,.0f}"
        )