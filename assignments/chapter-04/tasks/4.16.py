import time
print(f"The random uppercase letter is "
      f"{chr(ord('A') + int(time.time() % 26))}")

