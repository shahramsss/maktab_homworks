from datetime import datetime, date, time, timedelta

my_time = datetime(2018, 2, 19, 14)
print(my_time)
last_time = my_time + timedelta(hours=8 * 9)
another_time = datetime(2018, 2, 20, 10)

for i in range(9):
    print(my_time + timedelta(hours=8 * i))
print()
for j in range(9):
    if another_time <= my_time + timedelta(hours=8 * j):
        print("another time :", another_time)
        print("next pill time :", my_time + timedelta(hours=8 * j))
        break
