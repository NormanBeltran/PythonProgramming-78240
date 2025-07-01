import subprocess as sp

p = sp.run("dir", capture_output=True, encoding="cp850", shell=True)

print(f"Standard Output {p.stdout}")
print(f"Standard Error {p.stderr}")

print(f"Código de Retorno {p.returncode}")