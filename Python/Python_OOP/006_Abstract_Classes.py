"11/10/2026"
"Today I am implementing retry backoff - it is a techniques used in software and networks to wait for a period of time before trying a failed operation again "
"An abstract class is a blueprint for other classes in (OOP) that cannot be instantiated directly."
"It continues abstract methods -They can contain abstract methods (methods declared without a body) that must be implemented by any child class that inherits from it."
from abc import ABC, abstractmethod
import random
import time


# ---------- Parent: an ABSTRACT retry policy ----------
class RetryPolicy(ABC):
    def __init__(self, base_delay):
        self._base = base_delay

    @abstractmethod
    def delay(self, attempt):
        """How long to wait before retry number `attempt` (1, 2, 3...)."""


# ---------- Child 1: same wait every time ----------
class FixedDelay(RetryPolicy):
    def delay(self, attempt):
        return self._base


# ---------- Child 2: exponential backoff (#27) ----------
class ExponentialBackoff(RetryPolicy):
    def delay(self, attempt):
        return self._base * 2 ** (attempt - 1)      # 1x, 2x, 4x, 8x ...


# ---------- Child 3: backoff + jitter (#28) ----------
class BackoffWithJitter(ExponentialBackoff):         # child of a child!
    def delay(self, attempt):
        ceiling = super().delay(attempt)             # reuse the parent's maths
        return random.uniform(0, ceiling)            # pick a random wait below it


# ---------- The retry mechanism (#26): works with ANY policy ----------
def call_with_retry(func, policy, max_attempts):
    for attempt in range(1, max_attempts + 1):
        try:
            return func()
        except ConnectionError:
            if attempt == max_attempts:
                raise                                # out of attempts: give up
            wait = policy.delay(attempt)
            print(f"  attempt {attempt} failed, waiting {wait:.2f}s")
            time.sleep(wait)


# ---------- A fake payment API that fails 3 times, then works ----------
class FlakyPaymentAPI:
    def __init__(self, failures):
        self._failures_left = failures

    def send(self):
        if self._failures_left > 0:
            self._failures_left -= 1
            raise ConnectionError("network timeout")
        return "Payment confirmed"


random.seed(7)  # makes the "random" jitter repeatable for this demo
for policy in [FixedDelay(0.1), ExponentialBackoff(0.1), BackoffWithJitter(0.1)]:
    print(type(policy).__name__)
    api = FlakyPaymentAPI(failures=3)
    print("  ->", call_with_retry(api.send, policy, max_attempts=5))

try:
    RetryPolicy(0.1)
except TypeError as e:
    print("Abstract parent:", e)

    "How I would explain how these three child classes - have three strategies."
    "Think of it as calling a friend who isn’t picking up. There are three ways you might keep trying:"

"Fixed delay: you call back every 5 minutes, no matter what."
"Exponential backoff: you wait 5 minutes, then 10, then 20. They’re clearly busy, so you give them more space each time."
"Backoff with jitter: you still back off, but you don’t call at a predictable moment. Now imagine 1,000 people all calling the same friend: if they all call back at exactly minute 10, the phone gets jammed again. Randomness spreads them out."