import random
from model.contacts import Contacts
from model.group import Group
from fixture.orm import ORMFixture

data_base = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact_from_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contacts.create(Contacts(firstname="Test"))
    group_list = app.group.get_group_list()
    random_group = random.choice(group_list)
    group_id = random_group.id
    if len(data_base.get_contacts_in_group(Group(id=group_id))) == 0:
        contacts_from_ui = app.contacts.get_contact_list()
        any_contact = random.choice(contacts_from_ui)
        id_contact = any_contact.id
        app.contacts.contact_add_to_group(id_contact, group_id)
    contacts_list_in_group = app.contacts.get_contact_list_in_group(group_id)
    random_contact = random.choice(contacts_list_in_group)
    index = contacts_list_in_group.index(random_contact)
    app.group.delete_contact_from_group(index, group_id)
    l = data_base.get_contacts_not_in_group(Group(id=group_id))
    assert random_contact.id in [x.id for x in l]
