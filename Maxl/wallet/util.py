import random
import string

def generate_account_number():
    return "44" + str(random.randrange(00000000,99999999))


def generate_reference_number():
    "MA" + str(random.shuffle([string.ascii_letters][:31]))
    return "MA" + str(random.randrange(00000000,99999999))