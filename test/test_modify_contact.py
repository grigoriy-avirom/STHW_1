# -*- coding: utf-8 -*-
from model.contacts import Contacts
from random import randrange


def test_modify_contact_firstname(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="test"))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    contacts = Contacts(firstname="New firstname", middlename="New middlename", lastname="New lastname")
    contacts.id = old_contacts[index].id
    app.contacts.modify_contact_by_index(index, contacts)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) == app.contacts.count()
    old_contacts[index] = contacts
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
