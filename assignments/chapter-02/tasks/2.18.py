import time

offset = eval(input("Enter the time zone offset to GMT: "))
currentTime = time.time()
totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMinute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = (totalHours + offset) % 24
print(f"The current time is {currentHour}:{currentMinute}:{currentSecond}")