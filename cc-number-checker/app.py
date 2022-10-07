# Luhn Algorithm used on this project
# ? Reference: https://en.wikipedia.org/wiki/Luhn_algorithm
from re import match


def check_cc_number(cc_num: str):
    sum = 0
    second = False
    for i in reversed(cc_num):
        n = ord(i) - ord("0")
        if second:
            n *= 2
        second = not second
        sum += n // 10
        sum += n % 10
        
    if sum % 10 == 0:
        return True
    return False


def main():
    cc_num = input("Enter credit card number to check if is valid.\n> ")
    if not match(r"^[\d]{16}$", cc_num):
        print("Missing or wrong.")
        return
    
    if check_cc_number(cc_num):
        print("Payment success! :)")
    else:
        print("This cc number is not valid!")


if __name__ == "__main__":
    main()
