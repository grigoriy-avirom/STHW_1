# -*- coding: utf-8 -*-
from model.contacts import Contacts
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contacts.create(Contacts(firstname="firstname", middlename="middlename", lastname="lastname",
                                     nickname="nickname", title="title", company="company", address="address", home="123home",
                                     mobile="123mobile", work="123work", fax="123fax", email="email", email2="email2",
                                     email3="email3", homepage="www.homepage.ru", bday="1",
                                     bmonth="January", byear="2000", aday="1", amonth="January", ayear="2025"))
    old_contacts = db.get_contact_list()
    contacts = random.choice(old_contacts)
    app.contacts.delete_contact_by_id(contacts.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contacts)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contact.get_contact_list(), key=Contacts.id_or_max)

