import hashlib
import os
import enum

class Role(enum.Enum):
    """Enum định nghĩa vai trò người dùng"""
    ADMIN = "admin"
    STAFF = "staff"

class User:
    """Class quản lý thông tin và phân quyền người dùng"""
    
    def __init__(self, username: str, password: str, role: Role, full_name: str = ""):
        self.username = username
        self.full_name = full_name
        self.role = role
        self.salt = os.urandom(16).hex()  # Tạo salt ngẫu nhiên
        self.password_hash = self.hash_password(password)

    def hash_password(self, password: str) -> str:
        """Hash mật khẩu bằng SHA-256 + salt"""
        salted_password = password + self.salt
        return hashlib.sha256(salted_password.encode('utf-8')).hexdigest()

    def verify_password(self, password: str) -> bool:
        """Kiểm tra mật khẩu nhập vào có đúng không"""
        return self.hash_password(password) == self.password_hash

    def check_permission(self, required_role: Role) -> bool:
        """Kiểm tra quyền hạn. Admin có mọi quyền, Staff chỉ có quyền staff."""
        if self.role == Role.ADMIN:
            return True
        return self.role == required_role

    def __str__(self):
        return f"User({self.username}, Role: {self.role.value})"

# --- Dữ liệu mẫu mặc định ---
DEFAULT_USERS = [
    User("admin", "admin123", Role.ADMIN, "Quản trị viên"),
    User("manager", "manager123", Role.ADMIN, "Quản lý"),
    User("staff01", "staff123", Role.STAFF, "Nhân viên 1"),
    User("staff02", "staff123", Role.STAFF, "Nhân viên 2"),
]