import unittest
from modules.nguoi_dung import User, Role
from modules.quan_ly_ban_phong import Table, Room, RoomType, TableStatus

class TestNguoiA(unittest.TestCase):
    
    def test_phan_quyen(self):
        """Test kiểm tra quyền Admin và Staff"""
        admin = User("admin", "123", Role.ADMIN)
        staff = User("staff", "123", Role.STAFF)
        
        self.assertTrue(admin.check_permission(Role.STAFF)) # Admin làm được việc của Staff
        self.assertFalse(staff.check_permission(Role.ADMIN)) # Staff không làm được việc của Admin

    def test_doi_trang_thai_ban(self):
        """Test đổi trạng thái bàn"""
        room = Room("R1", "Phòng thường", RoomType.THUONG, 10)
        table = Table("T1", room, "Bàn 1", 4, 10, 10)
        self.assertTrue(table.is_available())
        table.change_status(TableStatus.DA_DAT)
        self.assertFalse(table.is_available())

if __name__ == '__main__':
    unittest.main()