"Day 1 - Sunday 25th October"
"Classes -A class is a blueprint used to create objects that share common properties and behavior."
"An object is an instance of a class. It represents a specific entity created from the class template"
" Let me explain in Java - __init__ is your constructor and self is this but the main difference is that python makes you write self out explicitly every time "

class Counter:
    def __init__(self):
         self.count = 0  # attribute: data the object owns - something is stored in this object and it lasts as long as the object .
        

    def hit(self):          # method: behaviour
        self.count += 1
        return self.count

c = Counter() # builds an object 
print(c.hit(), c.hit())     # 1 2


#Rate Limiter's state
import time

class RateLimiter:
    def __init__(self, limit, window):
        self.limit = limit              # max requests allowed
        self.window = window            # per this many seconds
        self.count = 0
        self.window_start = time.time()

#The behaviour (Indent this time is inside the class)
    def allow(self):
        now = time.time()
        if now - self.window_start >= self.window:
            self.window_start = now     # new window, reset
            self.count = 0
        if self.count < self.limit:
            self.count += 1
            return True
        return False

"this approach is called a fixed window. Count requests, and when the window expires, wipe the slate clean. -- this a design flaw since All 6 requests get through in 0.02 seconds (12.00.59 - 12.01.01), which is double the intended limit, because the counter resets at the 1.00s boundary. You spotted the real problem. Whether the server actually crashes depends on how much it can handle, but the limiter has failed at its one job: keeping bursts under control. Attackers doing brute-force logins time their attempts around exactly this kind of boundary. "

limiter = RateLimiter(limit=3, window=1)
results = [limiter.allow() for _ in range(5)]
assert results == [True, True, True, False, False]
time.sleep(1)
assert limiter.allow() is True
print("All tests passed")

"assert crashes loudly if something is wrong. If you see “All tests passed”, it works."


a = RateLimiter(3, 1)
b = RateLimiter(3, 1)

print(a.allow(), a.allow(), a.allow(), a.allow())  # True True True False
print(b.allow())                                   # ?
print(a.count, b.count)