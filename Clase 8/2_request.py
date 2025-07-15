import requests

try:
    r = requests.get("https://country.io/capital.json")
except Exception as e:
    print(f"Error {e}")    
else:
    print(r.status_code)    
    print(r.url)
    print(r.json())
    