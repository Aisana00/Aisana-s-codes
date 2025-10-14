from datetime import datetime
date1=datetime(2025,10,6,18,30,1)
date2=datetime(2025,10,5,9,45,20)
difference=(date1-date2).total_seconds()
print(f"Difference between two days in seconds: {difference}")