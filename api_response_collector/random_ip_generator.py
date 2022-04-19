import random
import socket
import struct
import ipcalc

RESERVED_SUBNET_LIST = [
]


def generate_ip_addresses(return_num=1):
    ip_addresses = []
    for _ in range(return_num):
        ip_addresses.append(_pick_random_ip())
    return ip_addresses


def _pick_random_ip():
    while True:
        random_ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))  
        if _is_reserved(random_ip):
            continue
        break
    return random_ip


def _is_reserved(ip):
    for reserved_ip in RESERVED_SUBNET_LIST:
        if ip in ipcalc.Network(reserved_ip):
            return True
    return False


if __name__ == '__main__':
    print(generate_ip_addresses())
