import requests

try:
    arg = {"nombre": "norman", "apellido": "beltran", "edad": 35}
    r = requests.get("https://httpbin.org/get", params=arg)
except Exception as e:
    print(f"Error {e}")    
else:
    print(r.status_code)    
    print(r.url)
    print(r.json())
    