import pymysql.cursors
from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group

# db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
# try:
#     groups = db.get_group_list()
#     for group in groups:
#         print(group)
#     print(len(groups))
# finally:
#     db.destroy()


# try:
#     contacts = db.get_contact_list()
#     for contact in contacts:
#         print(contact)
#     print(len(contacts))
# finally:
#     db.destroy()

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# try:
#     l = db.get_group_list()
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass

# try:
#     l = db.get_contact_list()
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass

try:
    t = db.get_contacts_not_in_group(Group(id="351"))
    for item in t:
        print(item)
    print(len(t))
finally:
    pass
