import time

tim = time.time()

print("The random uppercase letter is", chr(ord('A') + int(tim % 26)))
