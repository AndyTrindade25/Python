distance = float(input("Digite a distãncia a percorrer\n"))
if distance <= 200:
    ticket = 0.5 * distance
    
else:
    ticket = 0.35 * distance
    
print(f"Preço da passagem é {ticket:.2f}")

#Aumento de salário do funcionário
salary = float(input("Digite o seu salário"))
perc_increase =  0.15

if salary > 1250:
    perc_increase = 0.10
increase = salary * perc_increase
print(f"Seu aumento será de {increase:.2f}")