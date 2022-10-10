#https://www.beecrowd.com.br/judge/pt/runs/code/29430215#

nome = input()
salarioFixo = float(input())
vendas = float(input())

salarioFinal = salarioFixo + ((vendas / 100) * 15)

print("TOTAL = R$ %.2f" %(salarioFinal))