# -*- coding: utf-8 -*-
from model.contacts import Contacts
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "C:/StudySoftwareTesting/STHW_1/data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_digits(maxlen):
    digits = string.digits
    return "".join([random.choice(digits) for i in range(random.randrange(maxlen))])


def random_email():
    symbols_for_mail_name = string.ascii_letters + string.digits + "." + "-" + "_"
    mail_name = "".join([random.choice(symbols_for_mail_name) for i in range(random.randrange(2, 10))])
    domain_name = "".join([random.choice(string.ascii_letters) for i in range(random.randrange(2, 10))])
    country_name = "".join([random.choice(string.ascii_letters) for i in range(random.randrange(2, 5))])
    generated_email = f"{mail_name}@{domain_name}.{country_name}"
    return generated_email


testdata = [
    Contacts(firstname=random_string("firstname", 10),
             middlename=random_string("middlenamename", 10),
             lastname=random_string("lastname", 10),
             nickname=random_string("nickname", 10),
             title=random_string("title", 10),
             company=random_string("company", 10),
             address=random_string("address", 10),
             home=random_digits(11),
             mobile=random_digits(11),
             work=random_digits(11),
             fax=random_digits(11),
             email=random_email(),
             email2=random_email(),
             email3=random_email())
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
