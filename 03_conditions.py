#Условия погоды

weather = input('Какая сейчас погода ?: ').lower().strip()

if weather == 'sunny':
    print('Идем гулять!')
elif weather == 'rain':
    print('Возьми зонит, на улице дождь')
elif weather == 'snow':
    print('На улице снег, оденься по теплее')
else:
    print('Погода странная, останусь дома')


#Угадывания числа
secrets = 6
attempt = 0

while attempt < 3:
    guess = int(input('Угадай число: '))
    
    if guess == secrets:
        print('Ты угадал!')
        break
    
    elif guess <= secrets:
        print('Больше')
    
    elif guess >= secrets:
        print('Меньше')
    
    attempt += 1

else:
        print('Попытки закончились')

#Проверка возраста.
def plural_years(n):
    if n % 10 == 1 and n % 100 != 11:
        return 'Год'
    
    elif 2 <= n % 10 <= 4 and not (12 <= n % 100 <= 14):
        return "года"
    
    else:
        return "лет"

age = int(input('Сколько тебе лет?: '))

if age >= 18:
    print('Добро пожаловать!')
elif 12 <= age <= 18:
    years_left = 18 - age
    print(f'Ты подросток приходи позже через {years_left} {plural_years(years_left)}.')
else:
    print('Ты еще слишком мал! ')

