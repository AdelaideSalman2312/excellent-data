"Day 2 - Monday October 26th 2026 "

"Encapsulation in Python is the practice of bundling data (attributes) and behaviors (methods) together into a single unit—a class—while restricting direct access to some of the object's components."
"Think of it like a capsule: the internal workings are protected from the outside world, and you can only interact with it through a controlled interface"

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



# Encapsulation 

limiter = RateLimiter(3, 1)
for _ in range(3):
    limiter.allow()
limiter.count = 0          # anyone can reset it!
print(limiter.allow())     # True — limit bypassed
"Summary: yesterday’s limiter keeps its count in plain sight, so any code (buggy or malicious) can wipe it. A security control that can be switched off from outside isn’t really a control."

from collections import deque
import time

class SlidingWindowLimiter:
    def __init__(self, limit, window):
        self._limit = limit
        self._window = window
        self._timestamps = deque()   # times of recent requests

"A deque(pronounced deck short for double-ended queue) is a linear data structure that allows you to add and remove items from both the front and the rear."

"Summary: a leading underscore (_limit) is Python’s signal for “internal, don’t touch from outside”. Python won’t stop you, but every Python developer reads it as a warning sign. A deque is a list that’s fast to add to on the right and remove from on the left, which is exactly what we need."     
def allow(self):
        now = time.time()
        while self._timestamps and now - self._timestamps[0] >= self._window:
            self._timestamps.popleft()     # drop requests older than window
        if len(self._timestamps) < self._limit:
            self._timestamps.append(now)
            return True
        return False
"Summary: theres no reset moment anymore. On every call, we throw away requests older than 1 second and count what’s left. The window always looks back exactly 1 second from right now, which is why it’s called “sliding”."
@property
def used(self):
        return len(self._timestamps)
"Summary: @property lets outside code read limiter.used like a plain attribute, with no brackets. But since there’s no setter, limiter.used = 0 raises an error. This is the getter-without-setter pattern from Java, done the Python way."

def burst(limiter):
    time.sleep(0.9)
    first = [limiter.allow() for _ in range(3)]
    time.sleep(0.2)                        # cross the 1.0s boundary
    second = [limiter.allow() for _ in range(3)]
    return (first + second).count(True)

print("Fixed:", burst(RateLimiter(3, 1)))             # 6
print("Sliding:", burst(SlidingWindowLimiter(3, 1)))  # 3
s = SlidingWindowLimiter(3, 1)
s.used = 0      # what happens?

"Summary : The fixed window lets 6 requests through and the sliding window holds the line at 3. The cheat attempt crashes with AttributeError, which means the property is doing its job."


####################################################################################################################
#TRADE OFF AND WHY THIS MATTERS FOR SYSTEM DESIGN 
####################################################################################################################
"the fixed window stores 2 numbers per user. The sliding window stores up to limit timestamps per user. With 1 million users and a limit of 100 requests per minute, that’s up to 100 million timestamps in memory. Real systems such as API gateways often use a hybrid called the sliding window counter to get most of the accuracy for a fraction of the memory."
