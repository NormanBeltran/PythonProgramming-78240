with open("nombres.txt", "a") as f:
    nombres = ["JOSE", "ANA", "MARIA", "PEDRO"]
    for n in nombres:        
        f.write(n +"\n")