"""
Simple IPv4/IPv6 Address App
- Gets public IPv4 and IPv6
- Looks up basic details 
- Prints plain text 
"""

import json
import argparse
from typing import Optional, Dict
import requests

IPV4_URL  = "https://api.ipify.org?format=json"
IPV6_URL  = "https://api64.ipify.org?format=json"
IPAPI_URL = "https://ipapi.co/{ip}/json/"
TIMEOUT   = 10

def fetch_json(url: str) -> Optional[Dict]:
    try:
        r = requests.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json()
    except requests.RequestException:
        return None

def get_public_ip(kind: str) -> Optional[str]:
    url = IPV4_URL if kind == "v4" else IPV6_URL
    data = fetch_json(url)
    return (data or {}).get("ip")

def get_ip_details(ip: str) -> Dict:
    d = fetch_json(IPAPI_URL.format(ip=ip)) or {}
    return {
        "ip": d.get("ip"),
        "version": d.get("version"),
        "city": d.get("city"),
        "region": d.get("region"),
        "country_name": d.get("country_name"),
        "country_code": d.get("country_code"),
        "latitude": d.get("latitude"),
        "longitude": d.get("longitude"),
        "org": d.get("org"), 
        "asn": d.get("asn"),
        "timezone": d.get("timezone"),
    }

def print_section(title: str, payload: Dict):
    print(f"\n{title}")
    print("-" * len(title))
    for k, v in payload.items():
        if v not in (None, ""):
            print(f"{k}: {v}")

def main():
    parser = argparse.ArgumentParser(description="Show public IPv4/IPv6 + basic details.")
    parser.add_argument("--json", action="store_true", help="Output JSON only")
    args = parser.parse_args()

    ipv4 = get_public_ip("v4")
    ipv6 = get_public_ip("v6")

    result = {"ipv4": None, "ipv6": None}
    if ipv4:
        result["ipv4"] = {"address": ipv4, "details": get_ip_details(ipv4)}
    if ipv6:
        result["ipv6"] = {"address": ipv6, "details": get_ip_details(ipv6)}

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return

    print("Public IP Address Information")
    print("=============================")

    if not ipv4 and not ipv6:
        print("No public IP detected. (Network may block requests.)")
        return

    if ipv4:
        print_section("IPv4", {"address": ipv4, **(result["ipv4"]["details"] or {})})
    else:
        print("\nIPv4\n----\n(No IPv4 detected.)")

    if ipv6:
        print_section("IPv6", {"address": ipv6, **(result["ipv6"]["details"] or {})})
    else:
        print("\nIPv6\n----\n(No IPv6 detected.)")

if __name__ == "__main__":
    main()
