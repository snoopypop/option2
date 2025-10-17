"""
Simple IPv4/IPv6 Address App
- Gets public IPv4 and IPv6
- Looks up basic details (ipapi.co)
- --json for machine-readable output
"""

import json
import argparse
from typing import Optional, Dict, Tuple
import requests

# Endpoints 
IPV4_URL  = "https://api.ipify.org?format=json"
IPV6_URL  = "https://api64.ipify.org?format=json"
IPAPI_URL = "https://ipapi.co/{ip}/json/"
TIMEOUT   = 10

# Order and labels for printing details
DETAIL_KEYS = [
    ("ip",            "ip"),
    ("version",       "version"),
    ("city",          "city"),
    ("region",        "region"),
    ("country_name",  "country_name"),
    ("country_code",  "country_code"),
    ("latitude",      "latitude"),
    ("longitude",     "longitude"),
    ("organization",  "organization"), 
    ("asn",           "asn"),
    ("timezone",      "timezone"),
]

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
        "organization": d.get("org"),  
        "asn": d.get("asn"),
        "timezone": d.get("timezone"),
    }

def print_section(title: str, rows: Dict):
    print(f"\n{title}")
    print("-" * len(title))
    for key, label in DETAIL_KEYS:
        v = rows.get(key)
        if v in (None, ""):
            v = "(n/a)"
        if key in ("latitude", "longitude") and v not in ("(n/a)",):
            try:
                v = f"{float(v):.4f}"
            except Exception:
                pass
        print(f"{label}: {v}")

def main():
    ap = argparse.ArgumentParser(description="Show public IPv4/IPv6 + details.")
    ap.add_argument("--json", action="store_true", help="Output JSON only")
    args = ap.parse_args()

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

    # IPv4 
    if result["ipv4"]:
        print_section("IPv4", {"ip": result["ipv4"]["details"].get("ip", ipv4), **result["ipv4"]["details"]})
    else:
        print_section("IPv4", {k: None for k, _ in DETAIL_KEYS})

    # IPv6 
    if result["ipv6"]:
        print_section("IPv6", {"ip": result["ipv6"]["details"].get("ip", ipv6), **result["ipv6"]["details"]})
    else:
        print_section("IPv6", {k: None for k, _ in DETAIL_KEYS})

if __name__ == "__main__":
    main()
