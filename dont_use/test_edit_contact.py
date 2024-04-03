# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_edit_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create(Contacts(firstname="firstname", middlename="middlename", lastname="lastname",
                                     nickname="nickname", title="title", company="company", address="address", home="123home",
                                     mobile="123mobile", work="123work", fax="123fax", email="email", email2="email2",
                                     email3="email3", homepage="www.homepage.ru", bday="1",
                                     bmonth="January", byear="2000", aday="1", amonth="January", ayear="2025"))
    app.contacts.edit(Contacts(firstname="firstname edit", middlename="middlename edit", lastname="lastname edit",
                               nickname="nickname edit", title="title edit", company="company edit",
                               address="address edit", home="123home edit", mobile="123mobile edit",
                               work="123work edit", fax="123fax edit", email="email edit", email2="email2 edit",
                               email3="email3 edit", homepage="www.homepage.ru edit", bday="1",
                               bmonth="June", byear="2010", aday="1", amonth="June", ayear="2035"))

