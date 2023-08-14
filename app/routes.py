from flask import Blueprint, jsonify
from models import CurrencyRate, Transaction
from currency_converter import CurrencyConverter

api = Blueprint("api", __name__)

currency_rates_data = [
    {"from": "EUR", "to": "USD", "rate": 1.359},
    {"from": "CAD", "to": "EUR", "rate": 0.732},
    {"from": "USD", "to": "EUR", "rate": 0.736},
    {"from": "EUR", "to": "CAD", "rate": 1.366},
]

transactions_data = [
    {"sku": "T2006", "amount": 10.00, "currency": "USD"},
    {"sku": "M2007", "amount": 34.57, "currency": "CAD"},
    {"sku": "R2008", "amount": 17.95, "currency": "USD"},
    {"sku": "T2006", "amount": 7.63, "currency": "EUR"},
    {"sku": "B2009", "amount": 21.23, "currency": "USD"},
]

currency_rates = [
    CurrencyRate(rate_data["from"], rate_data["to"], rate_data["rate"])
    for rate_data in currency_rates_data
]
transactions = [
    Transaction(trans_data["sku"], trans_data["amount"], trans_data["currency"])
    for trans_data in transactions_data
]
currency_converter = CurrencyConverter(currency_rates)

@api.route("/currency_rates", methods=["GET"])
def get_currency_rates():
    return jsonify([rate.__dict__ for rate in currency_rates])

@api.route("/currency_rates/<string:currency>", methods=["GET"])
def get_currency_rate(currency):
    for rate in currency_rates:
        if rate.from_currency == currency:
            return jsonify(rate.__dict__)
    return jsonify({"error": "Currency rate not found"}), 404

@api.route("/transactions/<string:currency>", methods=["GET"])
def get_transactions_by_currency(currency):
    filtered_transactions = [
        trans.__dict__ for trans in transactions if trans.currency == currency
    ]
    return jsonify(filtered_transactions)

@api.route("/transactions/<string:sku>/<string:currency>", methods=["GET"])
def get_transactions_by_sku_and_currency(sku, currency):
    filtered_transactions = [
        trans.__dict__
        for trans in transactions
            if trans.sku == sku and trans.currency == currency
    ]
    return jsonify(filtered_transactions)




