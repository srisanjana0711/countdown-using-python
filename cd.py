import time
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("BLAST OFF!")

print("How many seconds to count down? Enter an integer:")
seconds = int(input())
countdown(seconds)
