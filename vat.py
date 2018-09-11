def get_vat(payment, percent=18):
    print(percent)
    try:
        payment = float(payment)
        vat = payment / 100 * percent
        vat = round(vat, 2)
        return 'Сумма НДС {}'.format(vat)
    except (TypeError, ValueError):
        return "Не могу посчитать"

result = get_vat(400, 20)
print(result)