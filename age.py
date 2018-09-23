age = int(input('Укажите ваш возраст: '))

if age < 6:
    text = 'Вы ходите в детский сад'
elif age in range(6, 17):
    text = 'Вы учитесь в школе'
elif age in range(17, 24):
    text = 'Вы учитесь в институте'
elif age >= 24:
    text = 'Вы работаете'

print('Ваш возраст ', age, text)