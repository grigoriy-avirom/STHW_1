# -*- coding: utf-8 -*-
import pytest
from contacts import Contacts
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contacts(firstname="qwe", middlename="asd", lastname="zxc", nickname="qwerty", title="asdfgh", company="zxcvbn", address="dfjhgdfkjhgdjkfhg", home="123", mobile="456",
                        work="789", fax="000", email="rty", email2="fgh", email3="fgh", homepage="iop", bday="1", bmonth="January", byear="2000", aday="1", amonth="January", ayear="2025"))
    app.return_to_contacts_page()
    app.logout()

