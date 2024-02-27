# 6.6. Опрос: Создайте список людей, которые должны участвовать в опросе по поводу любимого языка программирования.
# Включите некоторые имена, которые уже присутствуют в списке, и некоторые имена, которых в списке еще нет.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
workers = ['jen', 'sarah', 'bob', 'mike']
for name in workers:
    if name in favorite_languages.keys():
        print(f"\nThanks for your taking our poll, {name.title()}!")
    else:
        print(f"\n{name.title()}, please take our poll!")
