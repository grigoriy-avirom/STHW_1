# -*- coding: utf-8 -*-
from model.contacts import Contacts


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.edit(Contacts(firstname="firstname edit", middlename="middlename edit", lastname="lastname edit",
                               nickname="nickname edit", title="title edit", company="company edit",
                               address="address edit", home="123home edit", mobile="123mobile edit",
                               work="123work edit", fax="123fax edit", email="email edit", email2="email2 edit",
                               email3="email3 edit", homepage="www.homepage.ru edit", bday="1",
                               bmonth="June", byear="2010", aday="1", amonth="June", ayear="2035"))
    app.contacts.open_contacts_page()
    app.session.logout()
