from datetime import datetime
current_date=datetime.now()
print(f"Current date: {current_date}")
date_without_microseconds=current_date.replace(microsecond=0)
print(f"Date without microseconds: {date_without_microseconds}")
