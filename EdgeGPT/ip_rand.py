import random
import socket
import struct
import time

IP_RANGE = [
    ["23.142.0.0", "23.142.255.255"],
    ["3.168.0.0", "3.168.255.255"],  
]

def get_random_ip():
    seed = int(time.time() * 1000)
    rng = random.Random(seed)

    # Generate random index
    random_index = rng.randint(0, len(IP_RANGE) - 1)

    # Get random IP address range
    start_ip = IP_RANGE[random_index][0]
    end_ip = IP_RANGE[random_index][1]

    # Convert start IP address to integer
    start_ip_int = ip_to_uint32(socket.inet_aton(start_ip))
    # Convert end IP address to integer
    end_ip_int = ip_to_uint32(socket.inet_aton(end_ip))

    # Generate random IP address
    random_ip_int = rng.randint(start_ip_int, end_ip_int)
    random_ip = uint32_to_ip(random_ip_int)

    return random_ip

def ip_to_uint32(ip):
    return struct.unpack("!I", ip)[0]

def uint32_to_ip(int_ip):
    return socket.inet_ntoa(struct.pack("!I", int_ip))

