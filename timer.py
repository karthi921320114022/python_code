import time

count=int(input("Enter time in seconds :"))

for x in range(count,0,-1):
    time.sleep(1)
    seconds=int(x%60)
    minutes=int((x/60)%60)
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
print("Time's up!")