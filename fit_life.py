# Константы
WATER_PER_KG = 30  # Рекомендуемое количество воды в мл на кг веса
ML_PER_LITER = 1000  # Количество миллилитров в литре

# Приветствуем пользователя
print('Добро пожаловать в FitLife!')
print('-' * 40)

# Запрашиваем данные пользователя
user_name = input('Пожалуйста, введите ваше имя: ')
print(f'Привет, {user_name}!')
user_age = int(input('Введите ваш возраст: '))

# Сбор параметров и расчеты
user_weight = float(input('Введите ваш вес (в кг), например 79.5: '))
user_height = float(input('Введите ваш рост (в м), например 1.75: '))
bmi = round(user_weight / (user_height ** 2), 1)  # Расчет индекса массы тела
# Расчет рекомендуемого количества воды в литрах
water_liters = round(user_weight * WATER_PER_KG / ML_PER_LITER, 2)

# Вывод результатов
print('-' * 40)
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Ваш индекс массы тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_liters} л в день')
print('-' * 40)
print('Расчет окончен. Будьте здоровы! Ваш FitLife!')
