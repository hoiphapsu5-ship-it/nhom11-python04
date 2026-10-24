import matplotlib.pyplot as plt
from datetime import datetime, timedelta


class ThongKe:
    """Thống kê và Dashboard"""

    @staticmethod
    def tinh_kpi(reservations: list, customers: list, orders: list, tables: list):
        """Tính 4 KPI tổng quan"""
        kpi = {
            "ty_le_su_dung_ban": 0,
            "tong_so_dat_ban": len(reservations),
            "so_luong_khach_hang": len(customers),
            "doanh_thu": sum(o.get_total() for o in orders)
        }

        # Tỷ lệ bàn đang sử dụng
        ban_dang_dung = sum(1 for t in tables if t.status.value == "Đang phục vụ")
        if tables:
            kpi["ty_le_su_dung_ban"] = (ban_dang_dung / len(tables)) * 100

        return kpi

    @staticmethod
    def ve_bieu_do_trang_thai_ban(tables: list):
        """Biểu đồ tròn trạng thái bàn"""
        trang_thai = {}
        for t in tables:
            status = t.status.value
            trang_thai[status] = trang_thai.get(status, 0) + 1

        labels = list(trang_thai.keys())
        sizes = list(trang_thai.values())
        colors = ['green', 'red', 'orange', 'gold', 'gray']

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, colors=colors[:len(labels)], autopct='%1.1f%%')
        plt.title("Trạng thái bàn hiện tại")
        plt.savefig("bieu_do_trang_thai_ban.png")
        plt.close()
        print("✅ Đã lưu biểu đồ tròn: bieu_do_trang_thai_ban.png")

    @staticmethod
    def ve_bieu_do_dat_ban_14_ngay(reservations: list):
        """Biểu đồ đường đặt bàn 14 ngày gần nhất"""
        hom_nay = datetime.now()
        ngay_list = []
        so_luong_list = []

        for i in range(14):
            ngay = hom_nay - timedelta(days=i)
            ngay_list.append(ngay.strftime("%d/%m"))
            dem = sum(1 for r in reservations
                      if r.booking_datetime.date() == ngay.date())
            so_luong_list.append(dem)

        ngay_list.reverse()
        so_luong_list.reverse()

        plt.figure(figsize=(10, 5))
        plt.plot(ngay_list, so_luong_list, marker='o', color='blue')
        plt.title("Số lượng đặt bàn 14 ngày gần nhất")
        plt.xlabel("Ngày")
        plt.ylabel("Số đơn")
        plt.grid(True)
        plt.savefig("bieu_do_dat_ban_14_ngay.png")
        plt.close()
        print("✅ Đã lưu biểu đồ đường: bieu_do_dat_ban_14_ngay.png")

    @staticmethod
    def top_5_khach_thiet_than(customers: list):
        """Top 5 khách hàng theo tổng chi tiêu"""
        sorted_customers = sorted(customers, key=lambda c: c.total_spent, reverse=True)
        print("\n TOP 5 KHÁCH HÀNG THÂN THIẾT:")
        print("-" * 50)
        for i, c in enumerate(sorted_customers[:5], 1):
            print(f"{i}. {c.name} - {c.total_spent:,.0f}đ ({c.vip_tier.value})")
