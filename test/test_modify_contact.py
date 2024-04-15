# -*- coding: utf-8 -*-
from model.contacts import Contacts
from random import randrange


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contacts.create(Contacts(firstname="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contacts = Contacts(firstname="New firstname", middlename="New middlename", lastname="New lastname")
    contacts.id = old_contacts[index].id
    app.contacts.modify_contact_by_id(contacts.id, contacts)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contacts
    if check_ui:
        assert sorted(new_contacts, key=Contacts.id_or_max) == sorted(app.contact.get_contact_list(), key=Contacts.id_or_max)