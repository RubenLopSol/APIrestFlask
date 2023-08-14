class CurrencyConverter:
    def __init__(self, currency_rates):
        self.currency_rates = currency_rates

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        
        conversion_rate = self.get_conversion_rate(from_currency, to_currency)
        if conversion_rate is None:
            return None  # Conversion rate no disponible
        
        converted_amount = amount * conversion_rate
        return converted_amount

    def get_conversion_rate(self, from_currency, to_currency):
        for rate in self.currency_rates:
            if rate.from_currency == from_currency and rate.to_currency == to_currency:
                return rate.rate
        return self.convert_through_intermediate(from_currency, to_currency)

    def convert_through_intermediate(self, from_currency, to_currency):
        intermediate_currency = None
        conversion_rate = 1.0

        for rate in self.currency_rates:
            if rate.from_currency == from_currency:
                intermediate_currency = rate.to_currency
                conversion_rate *= rate.rate
                break

        if intermediate_currency is None:
            return None  # Cannot convert

        return conversion_rate * self.get_conversion_rate(intermediate_currency, to_currency)
