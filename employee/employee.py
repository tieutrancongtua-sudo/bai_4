from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, employee_id: str, full_name: str,
                 department: str = "Unassigned"):
        
        if not employee_id or not employee_id.strip():
            raise ValueError("Mã nhân sự không được rỗng.")
        if not full_name or not full_name.strip():
            raise ValueError("Họ tên không được rỗng.")
        if not department or not department.strip():
            raise ValueError("Phòng ban không được rỗng.")

        self.__employee_id = employee_id.strip()
        self.__full_name = full_name.strip()
        self.__department = department.strip()
        self.__monthly_bonus = 0.0  # Mặc định = 0

    @property
    def employee_id(self) -> str:
        return self.__employee_id

    @property
    def full_name(self) -> str:
        return self.__full_name

    @property
    def department(self) -> str:
        return self.__department

    @property
    def monthly_bonus(self) -> float:
        return self.__monthly_bonus

    #  Nạp chồng addBonus() 
    def add_bonus(self, *args) -> None:

        if len(args) == 1:
            amount = args[0]
            self._validate_amount(amount)
            self.__monthly_bonus += amount
        elif len(args) == 2:
            amount, reason = args
            self._validate_amount(amount)
            self._validate_reason(reason)
            self.__monthly_bonus += amount
        elif len(args) == 3:
            rate, reference_amount, reason = args
            self._validate_rate(rate)
            self._validate_reference(reference_amount)
            self._validate_reason(reason)
            self.__monthly_bonus += rate * reference_amount
        else:
            raise TypeError("add_bonus() chỉ nhận 1, 2 hoặc 3 tham số.")

    @staticmethod
    def _validate_amount(amount: float) -> None:
        if amount <= 0:
            raise ValueError("Số tiền thưởng phải lớn hơn 0.")

    @staticmethod
    def _validate_rate(rate: float) -> None:
        if rate <= 0 or rate > 0.5:
            raise ValueError("Tỷ lệ thưởng phải nằm trong khoảng (0, 0.5].")

    @staticmethod
    def _validate_reference(reference_amount: float) -> None:
        if reference_amount <= 0:
            raise ValueError("Giá trị tham chiếu phải lớn hơn 0.")

    @staticmethod
    def _validate_reason(reason: str) -> None:
        if not reason or not reason.strip():
            raise ValueError("Lý do thưởng không được rỗng.")

    # Reset thưởng cho kỳ lương mới 
    def reset_monthly_bonus(self) -> None:
        self.__monthly_bonus = 0.0

    # Phương thức trừu tượng
    @abstractmethod
    def calculate_gross_pay(self) -> float:
        pass

    @abstractmethod
    def get_employee_type(self) -> str:
        pass

    def display_payroll_info(self) -> str:
        return (
            f"[{self.get_employee_type()}] "
            f"Mã: {self.employee_id} | "
            f"Họ tên: {self.full_name} | "
            f"Phòng: {self.department} | "
            f"Thưởng: {self.monthly_bonus:,.0f} | "
            f"Thu nhập: {self.calculate_gross_pay():,.0f}"
        )

    def __str__(self) -> str:
        return self.display_payroll_info()