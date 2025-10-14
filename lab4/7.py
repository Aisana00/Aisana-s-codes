from datetime import datetime, timedelta
today=datetime.now().date()
yesterday=today-timedelta(days=1)
tomorrow= today+ timedelta(days=1)
print(f"Today: {today}")
print(f"Yesterday: {yesterday}")
print(f"Tomorrow: {tomorrow}")
