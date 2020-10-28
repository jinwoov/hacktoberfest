# A hello world with time-based greeting

from datetime import datetime

now = datetime.now()
hour = int(now.strftime("%H"))

greeting = ""

if hour >= 5 and hour <= 11:
    greeting = "Good morning!"
elif hour >= 12 and hour <= 17:
    greeting = "Good afternoon!"
elif hour >= 18 and hour <= 20:
    greeting = "Good evening!"
elif hour >= 21 and hour <= 23:
    greeting = "Good night!"
else:
    greeting = "Please, go to sleep."

print(f"Hello World. {greeting}")
