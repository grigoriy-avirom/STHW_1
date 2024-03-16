# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.edit(Group(name="name edit", header="header edit", footer="footer edit"))
