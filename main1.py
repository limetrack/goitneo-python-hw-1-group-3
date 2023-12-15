from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    # Отримання поточної дати
    today = datetime.today().date()
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Структура для зберігання результатів
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертація до типу date
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув, перевіряємо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Різниця днів між поточною датою та днем народження
        delta_days = (birthday_this_year - today).days

        # Перевірка, що день народження в межах наступного тижня
        if 0 <= delta_days < 7:
            # Визначення дня тижня
            day_of_week = weekdays[birthday_this_year.weekday()]
            # Якщо вихідний, переносимо на понеділок
            if day_of_week in ["Saturday", "Sunday"]:
                day_of_week = "Monday"
            birthdays[day_of_week].append(name)

    # Виведення результату
    for day in weekdays:
        if birthdays[day]:
            print(f"{day}: {', '.join(birthdays[day])}")

# Тестування функції
test_users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 14)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)}
]

get_birthdays_per_week(test_users)
