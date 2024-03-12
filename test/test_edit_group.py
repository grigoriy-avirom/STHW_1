# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="name edit", header="header edit", footer="footer edit"))
    app.session.logout()
