from datetime import datetime, timedelta
current_date= datetime.now().date()
new_date= current_date-timedelta(days=5)
print(f"Current date: {current_date}")
print(f"Date after subtrackting 5 days: {new_date}")