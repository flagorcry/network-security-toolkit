def is_valid_ipv4_address(address: str) -> bool:
    try:
        parts = address.split(".")

        if len(parts) != 4:
            return False

        for part in parts:
            if not part.isdigit():
                return False

        number = int(part)
        if number < 0 or number > 255:
            return False

        return True

    except Exception:
        return False


if __name__ == "__main__":
    tests = ["192.168.1.1"]

    for test in tests:
        result = is_valid_ipv4_address(test)
        print(result)