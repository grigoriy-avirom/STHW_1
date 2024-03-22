# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_contact(app):
    old_contacts = app.contacts.get_contact_list()
    contact = Contacts(firstname="firstname", middlename="middlename", lastname="lastname",
                    nickname="nickname", title="title", company="company", address="address", home="123home",
                    mobile="123mobile", work="123work", fax="123fax", email="email", email2="email2",
                    email3="email3", homepage="www.homepage.ru", bday="1",
                    bmonth="January", byear="2000", aday="1", amonth="January", ayear="2025")
    app.contacts.create(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert  sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

