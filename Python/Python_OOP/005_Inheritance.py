"10/11/2026"
"After being prodigal for like two weeks - I mean life had happened - I am back like I never left. "
"**What I am building and Why**"
"I now have two limiters, fixed window and sliding window, that do the same job in different ways. Real systems treat them as interchangeable: an API gateway lets you swap one for the other without rewriting the code that uses it. Inheritance is how we make that official. One parent class defines what every limiter must look like, and each child fills in its own strategy. It’s the same idea as Java’s extends."

from collections import deque
import time


# ---------- Parent: the shared "shape" of every limiter ----------
class Limiter:
    def __init__(self, limit, window):
        self._limit = limit
        self._window = window
        #It stores _limit and _window, which every limiter needs, and gives everyone a describe() method for free. Its allow() deliberately raises an error that says “each child must write its own”.

    def allow(self):
        raise NotImplementedError("Each limiter must write its own allow()") 

    def describe(self):
        name = type(self).__name__
        return f"{name}: {self._limit} requests per {self._window}s"
"Summary: the parent holds what’s shared and sets the rules. It isn’t meant to be used on its own, which is why calling Limiter(3, 1).allow() prints “Each limiter must write its own allow()”."

# ---------- Child 1: fixed window ----------
class FixedWindowLimiter(Limiter):
    def __init__(self, limit, window):
        super().__init__(limit, window)      # let the parent set limit/window
        self._count = 0
        self._window_start = time.time()

    def allow(self):
        now = time.time()
        if now - self._window_start >= self._window:
            self._window_start = now
            self._count = 0
        if self._count < self._limit:
            self._count += 1
            return True
        return False


# ---------- Child 2: sliding window ----------
class SlidingWindowLimiter(Limiter):
    def __init__(self, limit, window):
        super().__init__(limit, window)
        self._timestamps = deque()

    def allow(self):
        now = time.time()
        while self._timestamps and now - self._timestamps[0] >= self._window:
            self._timestamps.popleft()
        if len(self._timestamps) < self._limit:
            self._timestamps.append(now)
            return True
        return False

"Summary:children inherit everything from the parent, call super() to reuse the parent’s setup, and override only what differs. Notice that neither child writes describe(), yet both can use it. "
# ---------- Code that works with ANY limiter ----------
def login_attempts(limiter, attempts):
    results = [limiter.allow() for _ in range(attempts)]
    print(limiter.describe(), "->", results)


login_attempts(FixedWindowLimiter(3, 1), 5)
login_attempts(SlidingWindowLimiter(3, 1), 5)

try:
    Limiter(3, 1).allow()
except NotImplementedError as e:
    print("Parent alone:", e)

# When I am keen I can see that this polymorphism and it is overriding:one piece of code, many object types, each behaving in its own way. A login page could switch from fixed to sliding by changing one word, with nothing else touched.