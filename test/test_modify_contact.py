# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_modify_contact_firstname(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="test"))
    app.contacts.modify_first_contact(Contacts(firstname="New firstname",
                                               middlename="New middlename",
                                               lastname="New lastname"))
