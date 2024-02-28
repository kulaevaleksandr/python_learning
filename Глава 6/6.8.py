# 6.8. Домашние животные: создайте несколько словарей, имена которых представляют клички домашних животных.
# В каждом словаре сохраните информацию о виде животного и имени владельца. Сохраните словари в списке с именем pets
pets = {
    'Масик': {
        'animal': 'кот',
        'owner': 'Саша Кулаев',
        },
    'Малышка': {
        'animal': 'кошка',
        'owner': 'Катя',
    },
    'Дейзи': {
        'animal': 'собака',
        'owner': 'Николай Васильевич',
    }
}
for name, pet_info in pets.items():
    print(f'\nPet: {name}')
    animal = pet_info['animal']
    owner = pet_info['owner']
    print(f'\tAnimal: {animal.lower()}')
    print(f'\tOwner: {owner.title()}')