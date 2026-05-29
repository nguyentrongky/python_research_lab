import multiprocessing
import time

def heavy_calculation(num):
    print(f"[Core {num}] Đang kích nổ vòng lặp tính toán...")
    # Chạy một vòng lặp vô nghĩa 50 triệu lần để ép CPU làm việc
    count = 0
    for i in range(50_000_000):
        count += i
    print(f"[Core {num}] Hoàn thành tác vụ.")

if __name__ == "__main__":
    start_time = time.time()
    processes = []
    
    # Kích hoạt 4 tiến trình độc lập chạy trên 4 vCPUs cùng lúc
    for i in range(4):
        p = multiprocessing.Process(target=heavy_calculation, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"==> Tổng thời gian hủy diệt tác vụ: {time.time() - start_time:.2f} giây")
