# Bước 1: Nhập khẩu "vũ khí"
# Module `platform` là một phần của thư viện chuẩn Python, không cần cài đặt.
import platform
import sys

def conduct_system_check():
    """
    Thực hiện một cuộc "kiểm tra hệ thống" toàn diện và in ra kết quả.
    Hàm này sẽ thu thập thông tin về hệ điều hành, phiên bản, kiến trúc, và Python.
    """
    print(" BẮT ĐẦU CUỘC KIỂM TRA HỆ THỐNG TOÀN DIỆN ")
    print("="*50)

    # --- 1. Thông tin Hệ điều hành (OS) ---
    # Đây là phần trả lời trực tiếp nhất cho câu hỏi của ông.
    print("\n--- 1. Thông Tin Hệ Điều Hành ---")
    print(f" Tên hệ điều hành chung : {platform.system()}")     # Ví dụ: Windows, Linux, Darwin (cho macOS)
    print(f" Phiên bản HĐH (Release): {platform.release()}")  # Ví dụ: 10, 11
    print(f" Build chi tiết HĐH     : {platform.version()}")    # Chuỗi thông tin build rất dài và chi tiết
    print(f" Chuỗi thông tin đầy đủ  : {platform.platform()}")   # Tổng hợp tất cả thông tin trên thành một chuỗi

    # --- 2. Thông tin Phần cứng ---
    print("\n--- 2. Thông Tin Phần Cứng ---")
    print(f" Kiến trúc máy          : {platform.machine()}")      # Ví dụ: AMD64, x86_64
    print(f" Bộ xử lý (Processor)   : {platform.processor()}")  # Tên CPU
    print(f" Tên máy (Hostname)     : {platform.node()}")

    # --- 3. Thông tin Môi trường Python ---
    # Cực kỳ quan trọng để biết chúng ta đang chạy code bằng "bộ não" nào
    print("\n--- 3. Thông Tin Môi Trường Python ---")
    print(f" Trình triển khai Python: {platform.python_implementation()}") # Ví dụ: CPython
    print(f" Phiên bản Python       : {platform.python_version()}")        # Ví dụ: 3.11.7
    print(f" Trình thông dịch tại   : {sys.executable}")                   # Vô cùng quan trọng để xác nhận đang dùng đúng .venv

    print("\n" + "="*50)
    print(" KẾT THÚC KIỂM TRA ")

# Đây là quy ước chuyên nghiệp trong Python.
# Đoạn mã bên dưới chỉ chạy khi file này được thực thi trực tiếp bằng lệnh:
# python check_env.py
# Nó sẽ không chạy nếu file này được import bởi một file khác.
if __name__ == "__main__":
    conduct_system_check()