# 7.2. Заказ стола: напишите программу, которая спрашивает у пользователя, на сколько
# мест он хочет забронировать стол в ресторане. Если введенное число больше 8, выведите
# сообщение о том, что пользователю придется подождать. В противном случае сообщите, что стол готов.
guests = input('На сколько мест вы хотели бы забронировать стол? ')
guests = int(guests)
if guests > 8:
    print('Извините, вам придётся подождать.')
else:
    print('Прекрасно, стол для вас уже готов.')