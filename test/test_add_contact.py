# -*- coding: utf-8 -*-
from model.contacts import Contacts
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits(maxlen):
    digits = string.digits
    return "".join([random.choice(digits) for i in range(random.randrange(maxlen))])

def random_email():
    symbols_for_mail_name = string.ascii_letters + string.digits + "." + "-" + "_"
    mail_name = "".join([random.choice(symbols_for_mail_name) for i in range(random.randrange(1, 20))])
    domain_name = "".join([random.choice(string.ascii_letters) for i in range(random.randrange(2, 10))])
    country_name = "".join([random.choice(string.ascii_letters) for i in range(random.randrange(2, 5))])
    generated_email = f"{mail_name}@{domain_name}.{country_name}"
    return generated_email

testdata = [
    Contacts(firstname=random_string("firstname", 10),
             middlename=random_string("middlenamename", 10),
             lastname=random_string("lastname", 10),
             nickname=random_string("nickname", 10),
             title=random_string("title", 20),
             company=random_string("company", 20),
             address=random_string("address", 20),
             home=random_digits(11),
             mobile=random_digits(11),
             work=random_digits(11),
             fax=random_digits(11),
             email=random_email(),
             email2=random_email(),
             email3=random_email())
]

@pytest.mark.parametrize("contacts", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contacts):
    for contacts in testdata:
        old_contacts = app.contacts.get_contact_list()
        app.contacts.create(contacts)
        assert len(old_contacts) + 1 == app.contacts.count()
        new_contacts = app.contacts.get_contact_list()
        old_contacts.append(contacts)
        assert  sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
