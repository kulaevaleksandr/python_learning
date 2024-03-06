# 7.8. Сэндвичи: создайте список с именем sandwich_orders, заполните его названиями различных видов сэндвичей. Создайте пустой список с именем finished_sandwiches. В цикле
# переберите элементы первого списка и выведите сообщение для каждого элемента (например, «I made your tuna sandwich»)
sandwich_orders = ['easy sandwich', 'club sandwich', 'cheese sandwich', 'crab sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'In cooking - {current_sandwich}.')
    finished_sandwiches.append(current_sandwich)

# выводим все приготовленные сэндвичи
print('---Finished sandwiches---')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())