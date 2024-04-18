import random
from model.contacts import Contacts
from model.group import Group
from fixture.orm import ORMFixture

data_base = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group_list = app.group.get_group_list()
    random_group = random.choice(group_list)
    group_id = random_group.id
    if len(data_base.get_contacts_not_in_group(Group(id=group_id))) == 0:
        app.contacts.create(Contacts(firstname="Test"))
    n = data_base.get_contacts_not_in_group(Group(id=group_id))
    random_contact = random.choice(n)
    id_contact = random_contact.id
    app.contacts.contact_add_to_group(id_contact, group_id)
    l = data_base.get_contacts_in_group(Group(id=group_id))
    assert random_contact.id in [x.id for x in l]
