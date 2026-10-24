import enum
from datetime import datetime, timedelta
from modules.quan_ly_khach_hang import Customer
# Import Class Table của Người A để dùng
from modules.quan_ly_ban_phong import Table, TableStatus 

class ReservationStatus(enum.Enum):
    CHO_XAC_NHAN = "Chờ xác nhận"
    DA_XAC_NHAN = "Đã xác nhận"
    DA_COC = "Đã cọc"
    DA_HUY = "Đã hủy"
    HOAN_THANH = "Hoàn thành"

class Reservation:
    def __init__(self, reservation_id: str, customer: Customer, table: Table, 
                 booking_datetime: datetime, duration_hours: int, num_guests: int):
        self.reservation_id = reservation_id
        self.customer = customer
        self.table = table
        self.booking_datetime = booking_datetime
        self.duration_hours = duration_hours
        self.num_guests = num_guests
        self.status = ReservationStatus.CHO_XAC_NHAN
        self.deposit = 0.0
        self.notes = ""

    def get_end_time(self) -> datetime:
        """Tính thời gian kết thúc đặt bàn"""
        return self.booking_datetime + timedelta(hours=self.duration_hours)

    def check_time_overlap(self, other_reservation: 'Reservation') -> bool:
        """
        Kiểm tra trùng thời gian với một phiếu đặt khác trên cùng một bàn.
        Logic: (Start1 < End2) và (End1 > Start2)
        """
        if self.table.table_id != other_reservation.table.table_id:
            return False # Khác bàn thì không trùng
        
        my_start = self.booking_datetime
        my_end = self.get_end_time()
        other_start = other_reservation.booking_datetime
        other_end = other_reservation.get_end_time()

        return (my_start < other_end) and (my_end > other_start)

    def calculate_deposit(self) -> float:
        """Tính tiền cọc: Phòng VIP cọc 50%, thường cọc 0%"""
        if self.table.room.room_type.value == "VIP":
            self.deposit = 500000 # Ví dụ cọc cố định 500k cho VIP
            self.status = ReservationStatus.DA_COC
            return self.deposit
        return 0.0

    def confirm(self):
        """Xác nhận đặt bàn và đổi trạng thái bàn của Người A"""
        if self.table.is_available() or self.status == ReservationStatus.DA_COC:
            self.table.change_status(TableStatus.DA_DAT)
            self.status = ReservationStatus.DA_XAC_NHAN
            print(f"✅ Xác nhận đặt {self.table.name} cho {self.customer.name} thành công!")
        else:
            print("❌ Bàn này không khả dụng!")

    def cancel(self):
        """Hủy đặt bàn"""
        self.status = ReservationStatus.DA_HUY
        self.table.change_status(TableStatus.TRONG)
        print(f"❌ Đã hủy đặt {self.table.name}")
