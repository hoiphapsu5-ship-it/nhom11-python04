import tkinter as tk
from modules.quan_ly_ban_phong import Table, TableStatus

class TableWidget(tk.Canvas):
    """Custom Widget kế thừa tk.Canvas để vẽ sơ đồ bàn"""
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.tables = []
        self.bind("<Button-1>", self.on_click) # Bắt sự kiện click chuột

    def add_table(self, table: Table):
        """Thêm bàn vào danh sách và vẽ lên Canvas"""
        self.tables.append(table)
        self.draw_table(table)

    def draw_table(self, table: Table):
        """Vẽ hình chữ nhật đại diện cho bàn"""
        x, y = table.position
        width, height = 40, 40 # Kích thước bàn trên GUI
        
        # Chọn màu theo trạng thái
        color = "green" if table.is_available() else "red"
        if table.room.room_type.value == "VIP":
            color = "gold" # Bàn VIP màu vàng

        # Vẽ hình (Lưu ý: cần lưu ID của hình để update sau này)
        self.create_rectangle(x, y, x+width, y+height, fill=color, tags=table.table_id)
        self.create_text(x+width/2, y+height/2, text=table.name, tags=table.table_id)

    def on_click(self, event):
        """Xử lý khi click vào bàn (Hiện thông tin chi tiết)"""
        # Logic lấy thông tin bàn dựa vào tọa độ click sẽ viết sau
        print(f"Clicked at x={event.x}, y={event.y}")