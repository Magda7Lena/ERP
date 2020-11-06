import random
import string
from string import ascii_letters, digits


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    

    random_small_letters = "".join(random.choice(ascii_letters) for i in range(number_of_small_letters))
    random_capital_letters = "".join(random.choice(ascii_letters) for i in range(number_of_capital_letters))
    random_digits = "".join(random.choice(digits) for i in range(number_of_digits))
    random_special_chars = "".join(random.choice(allowed_special_chars) for i in range(number_of_special_chars))

    symbols = random_small_letters + random_capital_letters + random_digits + random_special_chars
    

    ID = "".join(random.choice(symbols) for i in range(10))

    
    return ID
