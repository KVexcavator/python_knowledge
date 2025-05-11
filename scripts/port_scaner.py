# сканер открытых портов
import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=1):
            print(f"Порт открыт: {port}")
    except:
        pass

def scan_ports(ip, ports):
    print(f"Сканирование IP: {ip}")
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports:
            executor.submit(scan_port, ip, port)

# Пример использования
target_ip = "192.168.1.1"  # IP-адрес роутера, сервера или ПК
port_range = range(20, 1024)  # Порты для сканирования

scan_ports(target_ip, port_range)
