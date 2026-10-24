import unittest
from modules.thuc_don import Appetizer, MainCourse, Dessert, Beverage, DanhMuc


class TestNguoiC(unittest.TestCase):

    def test_da_hinh_thue_suat(self):
        """Test đa hình tax_rate() cho 4 loại món"""
        khai_vi = Appetizer("M01", "Gỏi cuốn", 45000, DanhMuc.KHAI_VI)
        mon_chinh = MainCourse("M06", "Bò lúc lắc", 180000, DanhMuc.MON_CHINH)
        trang_mieng = Dessert("M16", "Chè ba màu", 35000, DanhMuc.TRANG_MIENG)
        do_uong = Beverage("M21", "Coca Cola", 25000, DanhMuc.DO_UONG)

        self.assertEqual(khai_vi.tax_rate(), 0.05)      # 5%
        self.assertEqual(mon_chinh.tax_rate(), 0.08)    # 8%
        self.assertEqual(trang_mieng.tax_rate(), 0.05)  # 5%
        self.assertEqual(do_uong.tax_rate(), 0.10)      # 10%

    def test_tinh_gia_cuoi(self):
        """Test get_final_price() = price * (1 + tax_rate())"""
        do_uong = Beverage("M21", "Coca Cola", 25000, DanhMuc.DO_UONG)
        # 25000 * 1.10 = 27500
        self.assertAlmostEqual(do_uong.get_final_price(), 27500.0)


if __name__ == '__main__':
    unittest.main()
