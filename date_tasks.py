from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print("1. Текущая дата:", current_date.date())
print("   5 дней назад:", five_days_ago.date())
print("-" * 30)

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("2. Вчера:", yesterday)
print("   Сегодня:", today)
print("   Завтра:", tomorrow)
print("-" * 30)

dt_with_micro = datetime.now()
dt_without_micro = dt_with_micro.replace(microsecond=0)
print("3. С микросекундами:", dt_with_micro)
print("   Без микросекунд:", dt_without_micro)
print("-" * 30)

date1 = datetime(2024, 1, 1, 12, 0, 0)
date2 = datetime(2024, 2, 5, 14, 30, 0) # Пример другой даты
diff_seconds = (date2 - date1).total_seconds()
print(f"4. Разница между {date1} и {date2}")
print(f"   В секундах: {diff_seconds}")