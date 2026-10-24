import enum

class RoomType(enum.Enum):
    """5 loại phòng theo yêu cầu"""
    VIP = "VIP"
    THUONG = "Thường"       # <-- Sửa chỗ này: bỏ dấu Ầ
    HOI_NGHI = "Hội nghị"
    GIA_DINH = "Gia đình"
    SAN_VUON = "Sân vườn"

class TableStatus(enum.Enum):
    """Các trạng thái của bàn"""
    TRONG = "Trống"
    DA_DAT = "Đã đặt"
    DANG_PHUC_VU = "Đang phục vụ"
    DA_DAT_COC = "Đã đặt cọc"
    BAO_TRI = "Bảo trì"

class Area:
    """Class đại diện cho Khu vực trong nhà hàng"""
    def __init__(self, area_id: str, name: str):
        self.area_id = area_id
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

class Room:
    """Class đại diện cho Phòng ăn"""
    def __init__(self, room_id: str, name: str, room_type: RoomType, capacity: int):
        self.room_id = room_id
        self.name = name
        self.room_type = room_type
        self.capacity = capacity
        self.tables = []
        
        # Quy định phụ thu theo loại phòng
        self.surcharge_rate = self._get_surcharge_rate()

    def _get_surcharge_rate(self) -> float:
        """Trả về tỷ lệ phụ thu (VIP 20-30%, thường 0%)"""
        if self.room_type == RoomType.VIP:
            return 0.25 # 25%
        return 0.0

    def get_surcharge(self, bill_amount: float) -> float:
        """Tính tiền phụ thu dựa trên tổng hóa đơn"""
        return bill_amount * self.surcharge_rate

    def get_room_type(self) -> str:
        return self.room_type.value

class Table:
    """Class đại diện cho Bàn ăn"""
    def __init__(self, table_id: str, room: Room, name: str, seats: int, x: int, y: int):
        self.table_id = table_id
        self.room = room
        self.name = name
        self.seats = seats
        self.position = (x, y) # Tọa độ x, y để vẽ GUI
        self.status = TableStatus.TRONG

    def change_status(self, new_status: TableStatus):
        """Đổi trạng thái bàn"""
        self.status = new_status
        print(f"Bàn {self.name} đã chuyển sang trạng thái: {self.status.value}")

    def is_available(self) -> bool:
        """Kiểm tra bàn có trống để đặt không"""
        return self.status == TableStatus.TRONG