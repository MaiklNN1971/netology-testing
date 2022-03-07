boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    super_couple = zip(sorted(boys), sorted(girls))
    print('Идельные пары:')
    for boy_name, girl_name in super_couple:
        print(f'{boy_name} и {girl_name}')
else:
    print('Кто-то может остаться без пары.')
