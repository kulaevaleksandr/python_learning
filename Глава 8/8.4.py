# 8.4. Большие футболки: измените функцию make_shirt(), чтобы по умолчанию футболки
# имели размер L и на них выводился текст «I love Python». Создайте футболку с размером L
# и текстом по умолчанию, а также футболку любого размера с другим текстом.

def make_shirt(size='L', text='I love Python!'):
    """Вывод размера футболки и текста на ней"""
    print(f'Размер футболки - {size}, текст на футболке - {text}')


make_shirt()
make_shirt(size='M', text='I love mammy!')
