import subprocess

p = subprocess.run(["python.exe", "--version"], capture_output=True, encoding="cp850")

print(f"Standard Output {p.stdout}")
print(f"Standard Error {p.stderr}")

print(f"Código de Retorno {p.returncode}")