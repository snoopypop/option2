# Prints public IPv4 and IPv6 addresses with ISP and country info

import requests

# API endpoints
IPV4_INFO = "https://ipinfo.io/json"   # Returns IPv4 + location + ISP data
IPV6_INFO = "https://ipinfo.io/json"   # Same endpoint works for IPv6-capable networks
TIMEOUT = 8  # seconds

def get_ip_info(url):
    """Fetches IP, ISP, and country info from the given URL."""
    try:
        r = requests.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        data = r.json() or {}
        return {
            "ip": data.get("ip"),
            "isp": data.get("org"),
            "country": data.get("country")
        }
    except Exception:
        return {"ip": None, "isp": None, "country": None}

def main():
    # Get public IPv4 info
    ipv4_info = get_ip_info(IPV4_INFO)
    # Get public IPv6 info (may be same if IPv6 not available)
    ipv6_info = get_ip_info(IPV6_INFO)

    print("Your Public IP Information:")
    print(f"  IPv4: {ipv4_info['ip'] or '(none)'}")
    print(f"   ├─ ISP: {ipv4_info['isp'] or '(unknown)'}")
    print(f"   └─ Country: {ipv4_info['country'] or '(unknown)'}")
    print()
    print(f"  IPv6: {ipv6_info['ip'] or '(none)'}")
    print(f"   ├─ ISP: {ipv6_info['isp'] or '(unknown)'}")
    print(f"   └─ Country: {ipv6_info['country'] or '(unknown)'}")

if __name__ == "__main__":
    main()
