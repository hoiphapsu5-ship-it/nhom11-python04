import re
import enum

class CustomerType(enum.Enum):
    VIP = "VIP"
    VANGLAI = "Vãng lai"
    DOITAC = "Đối tác"

class VIPTier(enum.Enum):
    STANDARD = "Standard"
    SILVER = "Silver"
    GOLD = "Gold"
    DIAMOND = "Diamond"

class Customer:
    def __init__(self, customer_id: str, name: str, phone: str, email: str, customer_type: CustomerType, total_spent: float = 0.0):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email
        self.customer_type = customer_type
        self.total_spent = total_spent
        self.vip_tier = self.update_vip_tier()
        
        # Validate dữ liệu ngay khi tạo
        self._validate_data()

    def _validate_data(self):
        """Validate Regex: SĐT VN, Email, Họ tên"""
        # Regex SĐT VN: bắt đầu bằng 0 hoặc +84, theo sau là 3,5,7,8,9 và 8 số
        phone_pattern = r"^(0|\+84)(3|5|7|8|9)[0-9]{8}$"
        if not re.match(phone_pattern, self.phone):
            raise ValueError(f"Số điện thoại không hợp lệ: {self.phone}")
        
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(email_pattern, self.email):
            raise ValueError(f"Email không hợp lệ: {self.email}")

    def update_vip_tier(self) -> VIPTier:
        """Tự động nâng hạng VIP theo tổng chi tiêu"""
        if self.total_spent >= 50000000:
            return VIPTier.DIAMOND
        elif self.total_spent >= 20000000:
            return VIPTier.GOLD
        elif self.total_spent >= 5000000:
            return VIPTier.SILVER
        return VIPTier.STANDARD

    def get_discount(self) -> float:
        """Trả về % giảm giá dựa trên hạng VIP"""
        discounts = {
            VIPTier.STANDARD: 0.0,
            VIPTier.SILVER: 0.05,   # 5%
            VIPTier.GOLD: 0.10,     # 10%
            VIPTier.DIAMOND: 0.15   # 15%
        }
        return discounts.get(self.vip_tier, 0.0)

    def add_spending(self, amount: float):
        """Cộng chi tiêu và cập nhật hạng VIP"""
        self.total_spent += amount
        self.vip_tier = self.update_vip_tier()
