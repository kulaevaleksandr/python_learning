# 7.4. Топпинг для пиццы: напишите цикл, который предлагает пользователю вводить дополнения для пиццы до тех пор, пока не будет введено значение 'quit'
pizza = "\nПожалуйста, напишите, что добавить в пиццу:"
pizza += "\n(Введите 'quit', когда закончите.) "

while True:
    topping = input(pizza)

    if topping == 'quit':
        break
    else:
        print(f'Хорошо, добавили в вашу пиццу {topping.lower()}!')
