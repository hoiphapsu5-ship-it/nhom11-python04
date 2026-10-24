import unittest
from datetime import datetime, timedelta
from modules.quan_ly_khach_hang import Customer, CustomerType, VIPTier
from modules.dat_ban import Reservation, ReservationStatus
from modules.quan_ly_ban_phong import Table, Room, RoomType, TableStatus

class TestNguoiB(unittest.TestCase):
    
    def test_validate_va_nang_hang_vip(self):
        """Test validate SĐT và tự động nâng hạng VIP"""
        # Test SĐT đúng
        khach1 = Customer("C01", "Nguyen Van A", "0901234567", "a@gmail.com", CustomerType.VANGLAI, total_spent=6000000)
        self.assertEqual(khach1.vip_tier, VIPTier.SILVER) # > 5 triệu phải lên Silver
        self.assertEqual(khach1.get_discount(), 0.05)
        
        # Test SĐT sai (phải báo lỗi)
        with self.assertRaises(ValueError):
            Customer("C02", "Nguyen Van B", "0123456789", "b@gmail.com", CustomerType.VANGLAI)

    def test_kiem_tra_trung_thoi_gian(self):
        """Test logic kiểm tra trùng giờ đặt bàn"""
        room = Room("R1", "Phòng thường", RoomType.THUONG, 4)
        table = Table("T1", room, "Bàn 1", 4, 10, 10)
        
        khach = Customer("C01", "Test", "0901234567", "test@test.com", CustomerType.VANGLAI)
        
        # Đặt bàn 1: 18:00 đến 20:00
        res1 = Reservation("R01", khach, table, datetime(2023, 10, 25, 18, 0), 2, 4)
        # Đặt bàn 2: 19:00 đến 21:00 (Trùng với res1)
        res2 = Reservation("R02", khach, table, datetime(2023, 10, 25, 19, 0), 2, 4)
        # Đặt bàn 3: 20:30 đến 22:00 (Không trùng)
        res3 = Reservation("R03", khach, table, datetime(2023, 10, 25, 20, 30), 1.5, 4)

        self.assertTrue(res1.check_time_overlap(res2))  # Phải trùng
        self.assertFalse(res1.check_time_overlap(res3)) # Không trùng

if __name__ == '__main__':
    unittest.main()

