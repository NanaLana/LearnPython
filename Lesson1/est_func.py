def get_vat(price, vat_rate):
    price = int(price)
    vat_rate = int(vat_rate)
    vat = price / 100 * vat_rate
    print(vat)

price = int(input("Ввести цену "))
vat_rate = int(input("Ввести процент "))
if price and vat_rate <= 0:
    print("Цена не может быть равна нулю")
else:
    get_vat(price, vat_rate)


