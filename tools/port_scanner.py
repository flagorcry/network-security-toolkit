import socket

def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            return result == 0
    except socket.error:
        return False



def scan_ports(host: str, port:list[int]) -> list[int]:
    open_ports = []
    for port in port:
        if scan_port(host, port):
            open_ports.append(port)
    return open_ports

if __name__ == "__main__":
    target_host = "127.0.0.1"
    common_ports = [21,22,23,25,53,80,110,443,3306]

    print(f"Scanning {target_host}...")
    results = scan_ports(target_host, common_ports)

    if results:
        print("open ports:", results)
    else:
        print("no open ports")