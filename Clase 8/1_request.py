import requests

try:
    #r = requests.get("https://www.clarin.com")
    #r = requests.get("https://en.wikipedia.org/wiki/List_of_tz_database_time_zones")
    r = requests.get("https://www.infobae.com/economia/2025/07/14/el-salario-acumulo-un-trimestre-de-caida-contra-la-inflacion-y-el-empleo-formal-sigue-estancado-segun-datos-oficiales/")
except Exception as e:
    print(f"Error {e}")    
else:
    print(r.status_code)    
    print(r.headers)
    print(r.url)
    print(r._content)

"""
Códigos de respuestas Web Services

1xx Respuestas informativas
2xx Peticion correcta
3xx Redirección
4xx Errores del lado del Cliente
5xx Errores del lado del Servidor
"""    