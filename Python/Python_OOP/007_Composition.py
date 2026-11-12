"12/11/2026 - Idempotency therefore the lesson is composition "
"Idempotency is a property where performing an operation multiple times produces the exact same system state and final result as performing it just once"

import uuid


# ---------- The money: a simple ledger of balances ----------
class Ledger:
    def __init__(self, balances):
        self._balances = dict(balances)

    def transfer(self, sender, receiver, amount):
        if self._balances[sender] < amount:
            raise ValueError("Insufficient funds")
        self._balances[sender] -= amount
        self._balances[receiver] += amount

    def balance(self, name):
        return self._balances[name]


# ---------- A network that delivers requests but loses replies ----------
class UnreliableNetwork:
    def __init__(self, drops):
        self._drops = drops              # how many replies to lose

    def reply(self, result):
        if self._drops > 0:
            self._drops -= 1
            raise ConnectionError("reply lost")
        return result


# ---------- Version 1: no idempotency ----------
class NaivePaymentService:
    def __init__(self, ledger, network):
        self._ledger = ledger            # HAS-A ledger   (composition)
        self._network = network          # HAS-A network  (composition)

    def send(self, key, sender, receiver, amount):
        self._ledger.transfer(sender, receiver, amount)
        return self._network.reply("Payment confirmed")


# ---------- Version 2: idempotent ----------
class IdempotentPaymentService(NaivePaymentService):
    def __init__(self, ledger, network):
        super().__init__(ledger, network)
        self._processed = {}             # key -> result already produced

    def send(self, key, sender, receiver, amount):
        if key not in self._processed:   # first time we've seen this payment
            self._ledger.transfer(sender, receiver, amount)
            self._processed[key] = "Payment confirmed"
        return self._network.reply(self._processed[key])


# ---------- The customer's phone: retries when no reply arrives ----------
def pay_with_retries(service, sender, receiver, amount, attempts=4):
    key = str(uuid.uuid4())              # ONE key, reused for every retry
    for attempt in range(1, attempts + 1):
        try:
            return service.send(key, sender, receiver, amount)
        except ConnectionError:
            print(f"  attempt {attempt}: no reply, retrying...")
    return "Gave up"


for Service in [NaivePaymentService, IdempotentPaymentService]:
    ledger = Ledger({"Calowe": 1000, "Shop": 0})
    service = Service(ledger, UnreliableNetwork(drops=2))
    print(Service.__name__)
    print("  ->", pay_with_retries(service, "Calowe", "Shop", 300))
    print("  Calowe:", ledger.balance("Calowe"), "| Shop:", ledger.balance("Shop"))