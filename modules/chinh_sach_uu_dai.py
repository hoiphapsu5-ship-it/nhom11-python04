import Customer, CustomerType

class ChinhSachUuDai:
    @staticmethod
    def apply_discount(customer: Customer, base_price: float) -> float:
        """Áp dụng giảm giá dựa trên hạng VIP"""
        discount_rate = customer.get_discount()
        final_price = base_price * (1 - discount_rate)
        print(f"Khách {customer.vip_tier.value} được giảm {discount_rate*100}%")
        return final_price

    @staticmethod
    def check_vip_priority(customer: Customer) -> bool:
        """Ưu tiên xếp bàn cho khách VIP và Đối tác"""
        if customer.customer_type in [CustomerType.VIP, CustomerType.DOITAC]:
            print("🌟 Được ưu tiên xếp phòng VIP!")
            return True
        return False

