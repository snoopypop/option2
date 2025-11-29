import requests

IPV4_INFO = "https://ipinfo.io/json"
IPV6_INFO = "https://ipinfo.io/json"
TIMEOUT = 8

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

def main():
    ipv4_info = get_ip_info(IPV4_INFO)
    ipv6_info = get_ip_info(IPV6_INFO)

    print("Your Public IP Information:")
    print(f"  IPv4: {ipv4_info['ip'] or '(none)'}")
    print(f"   ├─ ISP: {ipv4_info['isp'] or '(unknown)'}")
    print(f"   ├─ Country: {ipv4_info['country'] or '(unknown)'}")
    print(f"   ├─ City: {ipv4_info['city'] or '(unknown)'}")
    print(f"   ├─ Region: {ipv4_info['region'] or '(unknown)'}")
    print(f"   └─ Location: {ipv4_info['location'] or '(unknown)'}\n")

    print(f"  IPv6: {ipv6_info['ip'] or '(none)'}")
    print(f"   ├─ ISP: {ipv6_info['isp'] or '(unknown)'}")
    print(f"   ├─ Country: {ipv6_info['country'] or '(unknown)'}")
    print(f"   ├─ City: {ipv6_info['city'] or '(unknown)'}")
    print(f"   ├─ Region: {ipv6_info['region'] or '(unknown)'}")
    print(f"   └─ Location: {ipv6_info['location'] or '(unknown)'}")

if __name__ == "__main__":
    main()
