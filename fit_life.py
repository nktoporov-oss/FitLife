WATER_PER_KG = 30
"""Рекомендуемое количество воды в мл на кг веса."""
ML_PER_LITER = 1000
"""Количество миллилитров в литре."""
MIN_AGE = 14
"""Минимальный возраст для использования приложения."""
MAX_AGE = 120
"""Максимальный возраст для использования приложения."""
MIN_WEIGHT = 30
"""Минимальный вес для использования приложения."""
MAX_WEIGHT = 300
"""Максимальный вес для использования приложения."""
MIN_HEIGHT = 0.5
"""Минимальный рост для использования приложения."""
MAX_HEIGHT = 2.5
"""Максимальный рост для использования приложения."""

print('Добро пожаловать в FitLife!')
print('-' * 40)

user_name = input('Пожалуйста, введите ваше имя: ')
print(f'Привет, {user_name}!')
while True:
    try:
        user_age = int(input('Введите ваш возраст: '))
        if user_age < MIN_AGE or user_age > MAX_AGE:
            print(
                f'Возраст не может быть меньше {MIN_AGE}'
                f' или больше {MAX_AGE}.'
                ' Пожалуйста, введите корректное значение.'
            )
            continue
        break
    except ValueError:
        print('Пожалуйста, введите возраст числом (например 21).')

while True:
    try:
        user_weight = float(input('Введите ваш вес (в кг), например 79.5: '))
        if user_weight < MIN_WEIGHT or user_weight > MAX_WEIGHT:
            print(
                f'Вес должен быть числом от {MIN_WEIGHT} до {MAX_WEIGHT}. '
                'Пожалуйста, введите корректное значение.'
            )
            continue
        break
    except ValueError:
        print('Пожалуйста, введите вес числом (например 79.5).')

while True:
    try:
        user_height = float(input('Введите ваш рост (в м), например 1.75: '))
        if user_height < MIN_HEIGHT or user_height > MAX_HEIGHT:
            print(
                f'Рост должен быть числом от {MIN_HEIGHT} до {MAX_HEIGHT}. '
                'Пожалуйста, введите корректное значение.'
            )
            continue
        break
    except ValueError:
        print('Пожалуйста, введите рост числом (например 1.75).')

bmi = round(user_weight / (user_height ** 2), 1)  # Расчет индекса массы тела
# Расчет рекомендуемого количества воды в литрах
water_liters = round(user_weight * WATER_PER_KG / ML_PER_LITER, 2)

print('-' * 40)
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Ваш индекс массы тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_liters} л в день')
print('-' * 40)
print('Расчет окончен. Будьте здоровы! Ваш FitLife!')
