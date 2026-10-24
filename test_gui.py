import tkinter as tk
from modules.table_widget import TableWidget
from modules.quan_ly_ban_phong import Table, Room, RoomType, TableStatus

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Test Table Widget - Nhom 11")
root.geometry("600x400")

# Tạo widget
canvas = TableWidget(root, width=600, height=400, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Tạo dữ liệu mẫu
room_vip = Room("R1", "VIP", RoomType.VIP, 10)
room_thuong = Room("R2", "Thuong", RoomType.THUONG, 8)

# Thêm bàn vào widget
table1 = Table("T1", room_vip, "VIP-1", 4, 50, 50)
table2 = Table("T2", room_thuong, "T-1", 4, 150, 50)
table3 = Table("T3", room_thuong, "T-2", 6, 250, 50)

# Đổi trạng thái để test màu
table2.change_status(TableStatus.DA_DAT)

canvas.add_table(table1)  # Màu vàng (VIP)
canvas.add_table(table2)  # Màu đỏ (Da dat)
canvas.add_table(table3)  # Màu xanh (Trong)

# Chạy GUI
root.mainloop()