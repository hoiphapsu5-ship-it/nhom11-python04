from modules.thuc_don import MenuItem
from datetime import datetime


class OrderItem:
    """Chi tiết một món trong hóa đơn"""
    def __init__(self, item: MenuItem, quantity: int, note: str = ""):
        self.item = item
        self.quantity = quantity
        self.note = note

    def get_subtotal(self) -> float:
        """Thành tiền = giá cuối * số lượng"""
        return self.item.get_final_price() * self.quantity


class Order:
    """Hóa đơn của một bàn/phòng"""
    def __init__(self, order_id: str, table, customer=None):
        self.order_id = order_id
        self.table = table
        self.customer = customer
        self.items = []  # Danh sách OrderItem
        self.created_at = datetime.now()
        self.status = "Chưa thanh toán"

    def add_item(self, item: MenuItem, quantity: int, note: str = ""):
        """Thêm món vào hóa đơn"""
        order_item = OrderItem(item, quantity, note)
        self.items.append(order_item)
        print(f"✅ Đã thêm {quantity}x {item.name} vào hóa đơn")

    def get_subtotal(self) -> float:
        """Tổng tiền trước thuế và phụ thu"""
        return sum(item.get_subtotal() for item in self.items)

    def get_tax(self) -> float:
        """Tổng thuế của tất cả món"""
        return sum(item.item.get_final_price() - item.item.price for item in self.items
                   for _ in range(item.quantity))

    def get_room_surcharge(self) -> float:
        """Phụ thu phòng (gọi method của Người A)"""
        if hasattr(self.table, 'room'):
            return self.table.room.get_surcharge(self.get_subtotal())
        return 0.0

    def get_total(self) -> float:
        """Tổng cộng = subtotal + phụ thu phòng"""
        return self.get_subtotal() + self.get_room_surcharge()

    def print_invoice(self):
        """In hóa đơn dạng text"""
        print("=" * 50)
        print(f"HÓA ĐƠN #{self.order_id}")
        print(f"Bàn: {self.table.name}")
        print(f"Ngày: {self.created_at.strftime('%d/%m/%Y %H:%M')}")
        print("-" * 50)
        for item in self.items:
            print(f"{item.item.name} x{item.quantity}: {item.get_subtotal():,.0f}đ")
        print("-" * 50)
        print(f"Tổng món: {self.get_subtotal():,.0f}đ")
        print(f"Phụ thu phòng: {self.get_room_surcharge():,.0f}đ")
        print(f"TỔNG CỘNG: {self.get_total():,.0f}đ")
        print("=" * 50)
