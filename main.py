per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму: "))
deposit = []
for i in per_cent.values():
    deposit.append(round((i*money), 2))
print(deposit)
print("Максимальная сумма, которую вы можете заработать — " + str(max(deposit)) + " руб.")