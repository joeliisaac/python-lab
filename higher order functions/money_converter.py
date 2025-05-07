#takes in a rate name 'usd_to_eur' or 'uds_to_gbp'
def currency_converter(rate_name):
    rates = {
        'usd_to_eur': 0.91,
        'usd_to_gbp': 0.78,
        'usd_to_jpy': 154.73
    }
    def convert(amount):
        if rate_name in rates:
            return rates[rate_name] * amount
        else:
            return "No conversion"
    return convert



convert_to_eur = currency_converter('usd_to_eur')
print(convert_to_eur(100))  # Output: 91.0

