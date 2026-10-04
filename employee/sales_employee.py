from .employee import Employee


class SalesEmployee(Employee):

    MIN_COMMISSION = 0.0
    MAX_COMMISSION = 0.3

    def __init__(self, employee_id: str, full_name: str,
                 department: str = "Unassigned",
                 base_salary: float = 0.0,
                 sales_revenue: float = 0.0,
                 commission_rate: float = 0.0):
        # Constructor ủy quyền
        super().__init__(employee_id, full_name, department)
        self._validate_base_salary(base_salary)
        self._validate_sales_revenue(sales_revenue)
        self._validate_commission_rate(commission_rate)
        self.__base_salary = base_salary
        self.__sales_revenue = sales_revenue
        self.__commission_rate = commission_rate

    @property
    def base_salary(self) -> float:
        return self.__base_salary

    @property
    def sales_revenue(self) -> float:
        return self.__sales_revenue

    @property
    def commission_rate(self) -> float:
        return self.__commission_rate

    @staticmethod
    def _validate_base_salary(value: float) -> None:
        if value < 0:
            raise ValueError("Lương cơ bản không được âm.")

    @staticmethod
    def _validate_sales_revenue(value: float) -> None:
        if value < 0:
            raise ValueError("Doanh số không được âm.")

    @staticmethod
    def _validate_commission_rate(rate: float) -> None:
        if rate < SalesEmployee.MIN_COMMISSION or rate > SalesEmployee.MAX_COMMISSION:
            raise ValueError(
                f"Tỷ lệ hoa hồng phải từ {SalesEmployee.MIN_COMMISSION} "
                f"đến {SalesEmployee.MAX_COMMISSION}."
            )

    def update_sales_revenue(self, new_revenue: float) -> None:
        self._validate_sales_revenue(new_revenue)
        self.__sales_revenue = new_revenue

    def calculate_gross_pay(self) -> float:
        return (self.__base_salary
                + self.__sales_revenue * self.__commission_rate
                + self.monthly_bonus)

    def get_employee_type(self) -> str:
        return "SalesEmployee"

    def display_payroll_info(self) -> str:
        return (
            f"{super().display_payroll_info()}\n"
            f"    Lương CB: {self.__base_salary:,.0f} | "
            f"Doanh số: {self.__sales_revenue:,.0f} | "
            f"Hoa hồng: {self.__commission_rate:.0%}"
        )