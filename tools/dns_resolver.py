import socket
from ipaddress import ip_address


def resolve_hostname(hostname: str) -> str | None:
    try:
       ip_address = socket.gethostbyname(hostname)
       return ip_address
    except socket.gaierror:
        return None


def reverse_dns(ip_address: str) -> str | None:
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except (socket.gaierror, socket.herror):
        return None


if __name__ == "__main__":
    target = "google.com"

    print(f"Resolving hostname: {target}")
    ip = resolve_hostname(target)

    if ip:
        print(f"Ip address: {ip}")

        print("Performing reverse DNS lookup")
        hostname = reverse_dns(ip)

        if hostname:
            print(f"Hostname: {hostname}")
        else:
            print("Reverse DNS not found")
    else:
        print("Failed to resolve hostname")
