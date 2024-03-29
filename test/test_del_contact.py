# -*- coding: utf-8 -*-
from model.contacts import Contacts
from random import randrange


def test_delete_some_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="firstname", middlename="middlename", lastname="lastname",
                    nickname="nickname", title="title", company="company", address="address", home="123home",
                    mobile="123mobile", work="123work", fax="123fax", email="email", email2="email2",
                    email3="email3", homepage="www.homepage.ru", bday="1",
                    bmonth="January", byear="2000", aday="1", amonth="January", ayear="2025"))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    app.contacts.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts

