import time

countdown = 60
while countdown > 0:
    print(f"T-minus {countdown} seconds")
    countdown -= 1
    time.sleep(1)  # Simulate a 1-second wait
print("Boom!")