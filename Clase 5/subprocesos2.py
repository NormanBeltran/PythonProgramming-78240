import subprocess as sp

p = sp.run(["ipconfig", "/all"], capture_output=True, encoding="cp850")

print(f"Standard Output {p.stdout}")
print(f"Standard Error {p.stderr}")

print(f"Código de Retorno {p.returncode}")