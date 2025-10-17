# Prints public IPv4 

import requests

#IPv4
IPV4 = "https://api4.ipify.org?format=json"
TIMEOUT = 8

 # Call the endpoint and pull the ip field from the JSON.
def get_ip(url):
    try:
        r = requests.get(url, timeout=TIMEOUT)
        r.raise_for_status()
        return (r.json() or {}).get("ip")
    except Exception:
        return None

# Ask ipify for the public IPv4 address
def main():
    v4 = get_ip(IPV4)

    # Print the IPv4 address
    print(f"IPv4: {v4 if v4 else '(none)'}")

if __name__ == "__main__":
    main()
