DAI = float(input("Cuanto dinero vas a invertir?"))
IA = float(input("interés anual?"))
NA = int(input("Cuantos años?"))
print("Dinero total: " + str(round(DAI * (IA / 100 + 1) ,2)))           