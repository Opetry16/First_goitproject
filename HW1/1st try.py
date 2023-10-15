from datetime import datetime, timedelta, date
from collections import defaultdict

def get_birthdays_per_week(users):
    # Створюємо словник для зберігання ім'ян користувачів по днях тижня
    birthday_dict = defaultdict(list)
    
    # Отримуємо поточну дату
    today = date.today()

    # Перебираємо користувачів
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        
        # Визначаємо дату народження на цей рік
        birthday_this_year = birthday.replace(year=today.year)
        
        # Обчислюємо різницю між днем народження та поточною датою
        delta = (birthday_this_year - today).days
        
        # Визначаємо день тижня дня народження
        day_of_week = birthday_this_year.strftime('%A')
        
        # Якщо день народження на вихідний, переносимо на понеділок
        if delta < 0:
            delta += 365  # Переводимо на наступний рік
            day_of_week = (today + timedelta(days=delta)).strftime('%A')
        
        # Додаємо ім'я до списку відповідного дня тижня
        birthday_dict[day_of_week].append(name)
    
    # Виводимо результат
    for day, names in birthday_dict.items():
        print(f"{day}: {', '.join(names)}")

# Приклад користувачів
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)}
]

# Викликаємо функцію з прикладом користувачів
get_birthdays_per_week(users)