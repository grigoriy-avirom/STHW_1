from selenium.webdriver.support.select import Select
from model.contacts import Contacts

class ContactsHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contacts):
        wd = self.app.wd
        self.open_contacts_page()
        self.add_new_contact_page()
        # fill contacts fields
        self.fill_contacts_form(contacts)
        # save new contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.open_contacts_page()
        self.contacts_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.open_contacts_page()
        self.contacts_cache = None

    def fill_contacts_form(self, contacts):
        wd = self.app.wd
        self.change_field_value("firstname", contacts.firstname)
        self.change_field_value("middlename", contacts.middlename)
        self.change_field_value("lastname", contacts.lastname)
        self.change_field_value("nickname", contacts.nickname)
        self.change_field_value("title", contacts.title)
        self.change_field_value("company", contacts.company)
        self.change_field_value("address", contacts.address)
        self.change_field_value("home", contacts.home)
        self.change_field_value("mobile", contacts.mobile)
        self.change_field_value("work", contacts.work)
        self.change_field_value("fax", contacts.fax)
        self.change_field_value("email", contacts.email)
        self.change_field_value("email2", contacts.email2)
        self.change_field_value("email3", contacts.email3)
        self.change_field_value("homepage", contacts.homepage)
        self.change_date_value("bday", contacts.bday)
        self.change_date_value("bmonth", contacts.bmonth)
        self.change_field_value("byear", contacts.byear)
        self.change_date_value("aday", contacts.aday)
        self.change_date_value("amonth", contacts.amonth)
        self.change_field_value("ayear", contacts.ayear)

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_date_value(self, date_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(date_name).click()
            Select(wd.find_element_by_name(date_name)).select_by_visible_text(text)

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # open modification form
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # fill group form
        self.fill_contacts_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.open_contacts_page()
        self.contacts_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name('selected[]'))

    contacts_cache = None

    def get_contact_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                column = element.find_elements_by_tag_name("td")
                self.contacts_cache.append(Contacts(lastname=column[1].text, firstname=column[2].text, id=id))
        return list(self.contacts_cache)
