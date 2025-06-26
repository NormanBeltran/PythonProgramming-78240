with open("nombres.txt", "w") as f:
    nombres = ["JOSE", "ANA", "MARIA", "PEDRO"]
    for n in nombres:        
        f.write(n +"\n")