import time

secounds = eval(input("Enter an integer for seconds: "))

while secounds > 0:
    secounds -= 1
    time.sleep(1)
    if secounds == 0:
        print("Stopped")
        break
    print(secounds)