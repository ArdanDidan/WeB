import random
# function to generate a random password
def gen_pass(pass_length):
    elements = "abcdefghijklmnopqrstuvwxyz1234567890+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password