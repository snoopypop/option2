import requests

IPV4_INFO = "https://ipinfo.io/json"
IPV6_INFO = "https://ipinfo.io/json"
TIMEOUT = 8

GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

def get_ip_info(url):
    try:
        r = requests.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        data = r.json() or {}
        return {
            "ip": data.get("ip"),
            "isp": data.get("org"),
            "country": data.get("country"),
            "city": data.get("city"),
            "region": data.get("region"),
            "location": data.get("loc"),
        }
    except Exception as e:
        print(f"[ERROR] Failed to fetch from {url}: {e}")
        return {"ip": None, "isp": None, "country": None, "city": None, "region": None, "location": None}

def print_ip_info(label, info, color):
    print(color + f"  {label}: {info['ip'] or '(none)'}" + RESET)
    print(color + f"   ├─ ISP: {info['isp'] or '(unknown)'}" + RESET)
    print(color + f"   ├─ Country: {info['country'] or '(unknown)'}" + RESET)
    print(color + f"   ├─ City: {info['city'] or '(unknown)'}" + RESET)
    print(color + f"   ├─ Region: {info['region'] or '(unknown)'}" + RESET)
    print(color + f"   └─ Location: {info['location'] or '(unknown)'}\n" + RESET)

def main():
    ipv4_info = get_ip_info(IPV4_INFO)
    ipv6_info = get_ip_info(IPV6_INFO)

    print("Your Public IP Information:\n")
    
    print_ip_info("IPv4", ipv4_info, GREEN)
    print_ip_info("IPv6", ipv6_info, BLUE)

if __name__ == "__main__":
    main()
