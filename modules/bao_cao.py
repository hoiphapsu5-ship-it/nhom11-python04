import csv
import os
from datetime import datetime


class BaoCao:
    """Xuất báo cáo CSV và TXT"""

    @staticmethod
    def export_csv(reservations: list, filename="bao_cao_dat_ban.csv"):
        """Xuất báo cáo đặt bàn ra CSV"""
        os.makedirs('database', exist_ok=True)
        filepath = f"database/{filename}"

        with open(filepath, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(["Mã đặt", "Khách hàng", "Bàn", "Ngày giờ",
                             "Số khách", "Trạng thái", "Tiền cọc"])
            for r in reservations:
                writer.writerow([
                    r.reservation_id,
                    r.customer.name if r.customer else "N/A",
                    r.table.name,
                    r.booking_datetime.strftime("%d/%m/%Y %H:%M"),
                    r.num_guests,
                    r.status.value,
                    f"{r.deposit:,.0f}đ"
                ])
        print(f"✅ Đã xuất CSV: {filepath}")

    @staticmethod
    def export_txt(reservations: list, customers: list, filename="bao_cao_tong_hop.txt"):
        """Xuất báo cáo tổng hợp ra TXT"""
        os.makedirs('database', exist_ok=True)
        filepath = f"database/{filename}"

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("BÁO CÁO TỔNG HỢP HỆ THỐNG QUẢN LÝ NHÀ HÀNG\n")
            f.write(f"Ngày xuất: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
            f.write("=" * 60 + "\n\n")

            f.write(f"Tổng số phiếu đặt: {len(reservations)}\n")
            f.write(f"Tổng số khách hàng: {len(customers)}\n\n")

            f.write("CHI TIẾT ĐẶT BÀN:\n")
            f.write("-" * 60 + "\n")
            for r in reservations:
                f.write(f"- {r.reservation_id}: {r.customer.name if r.customer else 'N/A'} "
                        f"tại {r.table.name} ({r.status.value})\n")

        print(f"✅ Đã xuất TXT: {filepath}")
