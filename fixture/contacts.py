from selenium.webdriver.support.select import Select
from model.contacts import Contacts
import re


class ContactsHelper:

    def __init__(self, app):
        self.app = app

    contacts_cache = None

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

    def get_contact_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contacts_cache = []
            for element in wd.find_elements_by_css_selector("table tr[name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                firstname_text = element.find_element_by_css_selector("td:nth-child(3)").text
                lastname_text = element.find_element_by_css_selector("td:nth-child(2)").text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contacts_cache.append(Contacts(id=id, firstname=firstname_text, lastname=lastname_text,
                                                    address=address, all_emails_from_home_page=all_emails,
                                                    all_phones_from_home_page=all_phones))
        return list(self.contacts_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        fax = wd.find_element_by_name("fax").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contacts(firstname=firstname, lastname=lastname, id=id, address=address,
                        home=home, mobile=mobile, work=work, fax=fax,
                        email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        return Contacts(home=home, work=work, mobile=mobile, fax=fax)

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.home, contact.work, contact.mobile]))))

    def merge_emails_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))
