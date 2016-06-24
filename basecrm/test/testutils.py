import unittest
import os
import random
import munch

import basecrm

def rand():
    return str(random.randint(1, 1000000000))

def lazyproperty(function):
    attribute = '__lazy__' + function.__name__
    @property
    def __lazyproperty(self):
        if not hasattr(self.__class__, attribute):
            setattr(self.__class__, attribute, function(self))
        return getattr(self.__class__, attribute) 
    return __lazyproperty

if hasattr(unittest.TestCase, 'assertIsInstance'):
    class UnittestCompat:
        pass
else:
    class UnittestCompat:
        def assertIsInstance(self, obj, cls):
            if not isinstance(obj, cls):
                self.fail("%s is not an instance of %r" % (safe_repr(obj), cls))

        def assertGreaterEqual(self, given, expected):
            if not (given >= expected):
                self.fail("%s given mut be greater than or equal to %s" % (given, expected))
                
class BaseTestCase(unittest.TestCase, UnittestCompat):
    
    @lazyproperty
    def client(self):
        return basecrm.Client(access_token=self.access_token,
                              base_url=self.base_url,
                              user_agent=self.user_agent,
                              verbose=True)

    @property
    def user_agent(self):
        return "BaseCRM/V2 Python/{version}+tests".format(version=basecrm.VERSION)

    @property
    def access_token(self):
        token = os.environ.get('BASECRM_ACCESS_TOKEN')
        if token is None:
            raise Exception("'BASECRM_ACCESS_TOKEN' environment variable has not been found.")
        return token

    @property
    def base_url(self):
        url = os.environ.get('BASECRM_BASE_URL')
        return url or "https://api.getbase.com"

    @lazyproperty
    def account(self):
        return self.client.accounts.self()


    @lazyproperty
    def associated_contact(self):
        return self.create_associated_contact()

    @lazyproperty
    def contact(self):
        return self.create_contact()

    @lazyproperty
    def deal(self):
        return self.create_deal()

    @lazyproperty
    def lead(self):
        return self.create_lead()

    @lazyproperty
    def loss_reason(self):
        return self.create_loss_reason()

    @lazyproperty
    def note(self):
        return self.create_note()


    @lazyproperty
    def source(self):
        return self.create_source()


    @lazyproperty
    def tag(self):
        return self.create_tag()

    @lazyproperty
    def task(self):
        return self.create_task()

    @lazyproperty
    def user(self):
        return self.client.users.self()


    def create_associated_contact(self, **attributes):
        deal_id = self.create_deal().id;
        associated_contact = {
            'role': "involved",
            'contact_id': self.create_contact().id,
        }
        associated_contact.update(attributes)
        associated_contact = self.client.associated_contacts.create(deal_id, **associated_contact);

        associated_contact['deal_id'] = deal_id;
        return associated_contact;


    def create_contact(self, **attributes):
        contact = {
            'description': "I know him via Tom",
            'email': "mark@designservices.com",
            'facebook': "mjohnson",
            'fax': "+44-208-1234567",
            'first_name': 'Mark' +  rand(),
            'industry': "Design Services",
            'is_organization': False,
            'last_name': 'Johnson' +  rand(),
            'linkedin': "mjohnson",
            'mobile': "508-778-6516",
            'name': 'Design Services Company' +  rand(),
            'phone': "508-778-6516",
            'skype': "mjohnson",
            'tags': ["important"],
            'title': "CEO",
            'twitter': "mjohnson",
            'website': "www.designservices.com",
        }
        contact.update(attributes)
        contact = self.client.contacts.create(**contact);

        return contact;


    def create_deal(self, **attributes):
        deal = {
            'currency': "EUR",
            'dropbox_email': "dropbox@4e627bcd.deals.futuresimple.com",
            'hot': True,
            'name': 'Website Redesign' +  rand(),
            'tags': ["important"],
            'value': 1000,
            'contact_id': self.create_contact().id,
        }
        deal.update(attributes)
        deal = self.client.deals.create(**deal);

        return deal;


    def create_lead(self, **attributes):
        lead = {
            'description': "I know him via Tom",
            'email': "mark@designservices.com",
            'facebook': "mjohnson",
            'fax': "+44-208-1234567",
            'first_name': 'Mark' +  rand(),
            'industry': "Design Services",
            'last_name': 'Johnson' +  rand(),
            'linkedin': "mjohnson",
            'mobile': "508-778-6516",
            'phone': "508-778-6516",
            'skype': "mjohnson",
            'status': "Unqualified",
            'tags': ["important"],
            'title': "CEO",
            'twitter': "mjohnson",
            'website': "www.designservices.com",
        }
        lead.update(attributes)
        lead = self.client.leads.create(**lead);

        return lead;


    def create_loss_reason(self, **attributes):
        loss_reason = {
            'name': 'We were too expensive' +  rand(),
        }
        loss_reason.update(attributes)
        loss_reason = self.client.loss_reasons.create(**loss_reason);

        return loss_reason;


    def create_note(self, **attributes):
        note = {
            'content': "Highly important.",
            'resource_id': self.create_contact().id,
            'resource_type': 'contact',
        }
        note.update(attributes)
        note = self.client.notes.create(**note);

        return note;


    def create_source(self, **attributes):
        source = {
            'name': 'Word of mouth' +  rand(),
        }
        source.update(attributes)
        source = self.client.sources.create(**source);

        return source;


    def create_tag(self, **attributes):
        tag = {
            'name': 'publisher' +  rand(),
            'resource_type': 'contact',
        }
        tag.update(attributes)
        tag = self.client.tags.create(**tag);

        return tag;


    def create_task(self, **attributes):
        task = {
            'content': "Contact Tom",
            'due_date': "2014-09-27T16:32:56+00:00",
            'remind_at': "2014-09-29T15:32:56+00:00",
            'resource_id': self.create_contact().id,
            'resource_type': 'contact',
        }
        task.update(attributes)
        task = self.client.tasks.create(**task);

        return task;

    def create_deal_with_decimal_value(self, **attributes):
        deal = {
            'id': rand(),
            'currency': "EUR",
            'hot': True,
            'name': 'Website Redesign' +  rand(),
            'tags': ["important"],
            'value': '11.12',
            'contact_id': self.create_contact().id,
        }
        deal.update(attributes)

        client = self.client
        original_request_func = client.http_client.request
        client.http_client.request = lambda *args, **kwargs: (200, {}, munch.Munch(deal))

        deal = self.client.deals.create(**deal);

        client.http_client.request = original_request_func

        return deal;
