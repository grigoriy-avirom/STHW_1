# -*- coding: utf-8 -*-
from model.contacts import Contacts



def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.edit(Contacts(firstname="qwe", middlename="asd", lastname="zxc", nickname="qwerty", title="asdfgh", company="zxcvbn",
                 address="dfjhgdfkjhgdjkfhg", home="123", mobile="456",
                 work="789", fax="000", email="rty", email2="fgh", email3="fgh", homepage="iop", bday="1",
                 bmonth="January", byear="2000", aday="1", amonth="January", ayear="2025"))
    app.contacts.return_to_contacts_page()
    app.session.logout()