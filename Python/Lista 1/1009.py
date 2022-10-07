#https://www.beecrowd.com.br/judge/pt/runs/code/29347301#

nVendedor=input()
salarioF=float(input())
totalV=float(input())

bonus = float(totalV*(15/100))
total = (salarioF+bonus)
print("TOTAL = R$ %.2f" % total)