
config = {
    "mastercard": {
        "bankidprefix": [ 51, 52, 53, 54, 55 ],
        "length": 16
    }
}

testcards = {
    "mastercard": {
        "5555555555554444": True,
        "5555555555554445": False,
        "5555565555554444": False,
    }
}

def validatenumber(cardnumber):
    # starting with the first number double every other digit
    total = 0
    double = True
    for digit in cardnumber:
        digit = int(digit)
        if double:
            digit = digit*2
            # if result is two digits, then add those two digits together
            if digit > 9:
                tens = digit // 10
                units = digit % 10
                digit = tens+units
        double = not double
        # calculate total of all digits
        total += digit
    # valid number is divisible by ten
    return total % 10 == 0

for provider in testcards:
    print(provider)
    for cardnumber in testcards[provider]:
        print(cardnumber)
        isvalid = validatenumber(cardnumber)
        print(f"valid: {isvalid}")
        passed = testcards[provider][cardnumber] == isvalid
        print(f"passed: {passed}")

