def convert_currency(amount, choice):

    print("exchange rate: 1 USD = 33 THB")

    if choice == "USD":
        result = amount / 33
        print(f"result: {result:.2f} usd")

    elif choice == "THB":
        result = amount * 33
        print(f"result : {result:.2f} THB")

convert_currency(100, "USD")
convert_currency(200, "THB")