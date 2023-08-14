class CurrencyRate:
    def __init__(self, from_currency, to_currency, rate):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.rate = rate

class Transaction:
    def __init__(self, sku, amount, currency):
        self.sku = sku
        self.amount = amount
        self.currency = currency
