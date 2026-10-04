from .employee import Employee


class HourlyEmployee(Employee):
 
    MAX_HOURS = 250
    OVERTIME_THRESHOLD = 160
    OVERTIME_RATE = 1.5

    def __init__(self, employee_id: str, full_name: str,
                 department: str = "Unassigned",
                 hourly_rate: float = 0.0,
                 worked_hours: float = 0.0):
        # Constructor ủy quyền
        super().__init__(employee_id, full_name, department)
        self._validate_hourly_rate(hourly_rate)
        self._validate_worked_hours(worked_hours)
        self.__hourly_rate = hourly_rate
        self.__worked_hours = worked_hours

    @property
    def hourly_rate(self) -> float:
        return self.__hourly_rate

    @property
    def worked_hours(self) -> float:
        return self.__worked_hours

    @staticmethod
    def _validate_hourly_rate(rate: float) -> None:
        if rate < 0:
            raise ValueError("Đơn giá giờ không được âm.")

    @staticmethod
    def _validate_worked_hours(hours: float) -> None:
        if hours < 0 or hours > HourlyEmployee.MAX_HOURS:
            raise ValueError(
                f"Số giờ làm phải từ 0 đến {HourlyEmployee.MAX_HOURS}."
            )

    def _calculate_base_pay(self) -> float:
        if self.__worked_hours <= self.OVERTIME_THRESHOLD:
            return self.__worked_hours * self.__hourly_rate
        normal = self.OVERTIME_THRESHOLD * self.__hourly_rate
        overtime = ((self.__worked_hours - self.OVERTIME_THRESHOLD)
                    * self.__hourly_rate * self.OVERTIME_RATE)
        return normal + overtime

    def calculate_gross_pay(self) -> float:
        return self._calculate_base_pay() + self.monthly_bonus

    def get_employee_type(self) -> str:
        return "HourlyEmployee"

    def display_payroll_info(self) -> str:
        return (
            f"{super().display_payroll_info()}\n"
            f"    Đơn giá giờ: {self.__hourly_rate:,.0f} | "
            f"Số giờ: {self.__worked_hours}"
        )