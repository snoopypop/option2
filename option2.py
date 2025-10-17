# Prints public IPv4 and IPv6 addresses

import requests

# API endpoints for both IP versions
IPV4 = "https://api4.ipify.org?format=json"
IPV6 = "https://api6.ipify.org?format=json"
TIMEOUT = 8  # seconds

def get_ip(url):
    """Fetches the public IP address from the given URL."""
    try:
        r = requests.get(url, timeout=TIMEOUT)
        r.raise_for_status()  # raises error if status != 200
        return (r.json() or {}).get("ip")
    except Exception:
        return None

def main():
    # Get both IPv4 and IPv6 addresses
    v4 = get_ip(IPV4)
    v6 = get_ip(IPV6)

    # Print results
    print("Your Public IP Addresses:")
    print(f"  IPv4: {v4 if v4 else '(none)'}")
    print(f"  IPv6: {v6 if v6 else '(none)'}")

if __name__ == "__main__":
    main()
