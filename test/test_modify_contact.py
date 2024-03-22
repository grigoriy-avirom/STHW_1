# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_modify_contact_firstname(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="test"))
    old_contacts = app.contacts.get_contact_list()
    contacts = Contacts(firstname="New firstname", middlename="New middlename", lastname="New lastname")
    contacts.id = old_contacts[0].id
    app.contacts.modify_first_contact(contacts)
    assert len(old_contacts) == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts[0] = contacts
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
