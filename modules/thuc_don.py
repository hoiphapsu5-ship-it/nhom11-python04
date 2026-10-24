from abc import ABC, abstractmethod
import enum


class DanhMuc(enum.Enum):
    """4 loại món ăn theo yêu cầu"""
    KHAI_VI = "Khai vị"
    MON_CHINH = "Món chính"
    TRANG_MIENG = "Tráng miệng"
    DO_UONG = "Đồ uống"


class MenuItem(ABC):
    """Lớp trừu tượng cha - bắt buộc các lớp con phải cài đặt tax_rate()"""

    def __init__(self, item_id: str, name: str, price: float, category: DanhMuc):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category

    @abstractmethod
    def tax_rate(self) -> float:
        """Phương thức trừu tượng - mỗi loại món có thuế suất khác nhau"""
        pass

    def get_final_price(self) -> float:
        """Tính giá cuối cùng = giá gốc * (1 + thuế suất)"""
        return self.price * (1 + self.tax_rate())

    def __str__(self):
        return f"{self.name} - {self.price:,.0f}đ (Thuế: {self.tax_rate()*100}%)"


class Appetizer(MenuItem):
    """Khai vị - thuế 5%"""
    def tax_rate(self) -> float:
        return 0.05


class MainCourse(MenuItem):
    """Món chính - thuế 8%"""
    def tax_rate(self) -> float:
        return 0.08


class Dessert(MenuItem):
    """Tráng miệng - thuế 5%"""
    def tax_rate(self) -> float:
        return 0.05


class Beverage(MenuItem):
    """Đồ uống - thuế 10%"""
    def tax_rate(self) -> float:
        return 0.10


# --- Dữ liệu mẫu 30 món ăn ---
SAMPLE_MENU = [
    # Khai vị (5 món)
    Appetizer("M01", "Gỏi cuốn tôm thịt", 45000, DanhMuc.KHAI_VI),
    Appetizer("M02", "Chả giò hải sản", 55000, DanhMuc.KHAI_VI),
    Appetizer("M03", "Súp cua", 60000, DanhMuc.KHAI_VI),
    Appetizer("M04", "Salad rau củ", 40000, DanhMuc.KHAI_VI),
    Appetizer("M05", "Bánh xèo", 50000, DanhMuc.KHAI_VI),

    # Món chính (10 món)
    MainCourse("M06", "Bò lúc lắc", 180000, DanhMuc.MON_CHINH),
    MainCourse("M07", "Cá hồi áp chảo", 220000, DanhMuc.MON_CHINH),
    MainCourse("M08", "Gà nướng mật ong", 150000, DanhMuc.MON_CHINH),
    MainCourse("M09", "Heo quay", 200000, DanhMuc.MON_CHINH),
    MainCourse("M10", "Cơm chiên hải sản", 120000, DanhMuc.MON_CHINH),
    MainCourse("M11", "Phở bò đặc biệt", 90000, DanhMuc.MON_CHINH),
    MainCourse("M12", "Bún chả Hà Nội", 85000, DanhMuc.MON_CHINH),
    MainCourse("M13", "Lẩu thái hải sản", 350000, DanhMuc.MON_CHINH),
    MainCourse("M14", "Vịt quay Bắc Kinh", 280000, DanhMuc.MON_CHINH),
    MainCourse("M15", "Steak bò Úc", 450000, DanhMuc.MON_CHINH),

    # Tráng miệng (5 món)
    Dessert("M16", "Chè ba màu", 35000, DanhMuc.TRANG_MIENG),
    Dessert("M17", "Kem dừa", 40000, DanhMuc.TRANG_MIENG),
    Dessert("M18", "Bánh flan", 30000, DanhMuc.TRANG_MIENG),
    Dessert("M19", "Trái cây theo mùa", 45000, DanhMuc.TRANG_MIENG),
    Dessert("M20", "Tiramisu", 55000, DanhMuc.TRANG_MIENG),

    # Đồ uống (10 món)
    Beverage("M21", "Coca Cola", 25000, DanhMuc.DO_UONG),
    Beverage("M22", "7 Up", 25000, DanhMuc.DO_UONG),
    Beverage("M23", "Nước suối", 15000, DanhMuc.DO_UONG),
    Beverage("M24", "Bia Heineken", 45000, DanhMuc.DO_UONG),
    Beverage("M25", "Rượu vang đỏ", 150000, DanhMuc.DO_UONG),
    Beverage("M26", "Nước cam tươi", 35000, DanhMuc.DO_UONG),
    Beverage("M27", "Cà phê đen", 30000, DanhMuc.DO_UONG),
    Beverage("M28", "Trà đá", 10000, DanhMuc.DO_UONG),
    Beverage("M29", "Sinh tố bơ", 45000, DanhMuc.DO_UONG),
    Beverage("M30", "Nước ép dưa hấu", 40000, DanhMuc.DO_UONG),
]
