# Prints only public IPv4 and IPv6 

import requests

IPV4 = "https://api4.ipify.org?format=json"
IPV6 = "https://api6.ipify.org?format=json"
TIMEOUT = 8

def get_ip(url):
    try:
        r = requests.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        return (r.json() or {}).get("ip")
    except Exception:
        return None

def main():
    v4 = get_ip(IPV4)
    v6 = get_ip(IPV6)  

    print(f"IPv4: {v4 if v4 else '(none)'}")
    print(f"IPv6: {v6 if v6 else '(none)'}")

if __name__ == "__main__":
    main()
