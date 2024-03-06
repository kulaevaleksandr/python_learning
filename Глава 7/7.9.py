# 7.9. Без пастрами: используя список sandwich_orders из упражнения 7.8, проследите за
# тем, чтобы значение 'pastrami' встречалось в списке как минимум три раза. Добавьте в начало программы код для вывода сообщения о том, что пастрами больше нет, и напишите
# цикл while для удаления всех вхождений 'pastrami' из sandwich_orders. Убедитесь в том,
# что в finished_sandwiches значение 'pastrami' не встречается ни одного раза

sandwich_orders = ['easy sandwich','pastrami', 'club sandwich', 'pastrami', 'cheese sandwich', 'pastrami', 'crab sandwich']
print('Sorry, pastrami is gone.')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)