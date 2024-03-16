# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    app.group.edit(Group(name="name edit", header="header edit", footer="footer edit"))
