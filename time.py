from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M")
print("The current time is", current_time)

