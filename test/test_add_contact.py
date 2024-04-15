# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_add_contact(app, json_contacts, db, check_ui):
    contacts = json_contacts
    old_contacts = db.get_contact_list()
    app.contacts.create(contacts)
    new_contacts = db.get_contact_list()
    old_contacts.append(contacts)
    assert  sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contacts.get_contact_list(), key=Contacts.id_or_max)
