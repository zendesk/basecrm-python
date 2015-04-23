

class AccountsService(object):

    def __init__(self, http_client):
        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def self(self):
        _, _, resource = self.http_client.get("/accounts/self")
        return resource


class AssociatedContactsService(object):
    OPTS_KEYS_TO_PERSIST = ['contact_id', 'role']

    def __init__(self, http_client):
        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, deal_id, **params):
        _, _, associated_contacts = self.http_client.get("/deals/{deal_id}/associated_contacts".format(deal_id=deal_id), params=params)
        return associated_contacts

    def create(self, deal_id, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for AssociatedContact are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, associated_contact = self.http_client.post("/deals/{deal_id}/associated_contacts".format(deal_id=deal_id), body=attributes)
        return associated_contact

    def destroy(self, deal_id, contact_id) :
        status_code, _, _ = self.http_client.delete("/deals/{deal_id}/associated_contacts/{contact_id}".format(deal_id=deal_id, contact_id=contact_id))
        return status_code == 204


class ContactsService(object):
    OPTS_KEYS_TO_PERSIST = ['address', 'contact_id', 'custom_fields', 'customer_status', 'description', 'email', 'facebook', 'fax', 'first_name', 'industry', 'is_organization', 'last_name', 'linkedin', 'mobile', 'name', 'owner_id', 'phone', 'prospect_status', 'skype', 'tags', 'title', 'twitter', 'website']

    def __init__(self, http_client):
        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        _, _, contacts = self.http_client.get("/contacts", params=params)
        return contacts

    def create(self, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for Contact are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, contact = self.http_client.post("/contacts", body=attributes)
        return contact

    def retrieve(self, id) :
        _, _, contact = self.http_client.get("/contacts/{id}".format(id=id))
        return contact

    def update(self, id, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for Contact are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, contact = self.http_client.put("/contacts/{id}".format(id=id), body=attributes)
        return contact

    def destroy(self, id) :
        status_code, _, _ = self.http_client.delete("/contacts/{id}".format(id=id))
        return status_code == 204


class DealsService(object):
    OPTS_KEYS_TO_PERSIST = ['contact_id', 'currency', 'custom_fields', 'hot', 'loss_reason_id', 'name', 'owner_id', 'source_id', 'stage_id', 'tags', 'value']

    def __init__(self, http_client):
        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        _, _, deals = self.http_client.get("/deals", params=params)
        return deals

    def create(self, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for Deal are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, deal = self.http_client.post("/deals", body=attributes)
        return deal

    def retrieve(self, id) :
        _, _, deal = self.http_client.get("/deals/{id}".format(id=id))
        return deal

    def update(self, id, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for Deal are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, deal = self.http_client.put("/deals/{id}".format(id=id), body=attributes)
        return deal

    def destroy(self, id) :
        status_code, _, _ = self.http_client.delete("/deals/{id}".format(id=id))
        return status_code == 204


class LeadsService(object):
    OPTS_KEYS_TO_PERSIST = ['address', 'custom_fields', 'description', 'email', 'facebook', 'fax', 'first_name', 'industry', 'last_name', 'linkedin', 'mobile', 'organization_name', 'owner_id', 'phone', 'skype', 'status', 'tags', 'title', 'twitter', 'website']

    def __init__(self, http_client):
        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        _, _, leads = self.http_client.get("/leads", params=params)
        return leads

    def create(self, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for Lead are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, lead = self.http_client.post("/leads", body=attributes)
        return lead

    def retrieve(self, id) :
        _, _, lead = self.http_client.get("/leads/{id}".format(id=id))
        return lead

    def update(self, id, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for Lead are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, lead = self.http_client.put("/leads/{id}".format(id=id), body=attributes)
        return lead

    def destroy(self, id) :
        status_code, _, _ = self.http_client.delete("/leads/{id}".format(id=id))
        return status_code == 204


class LossReasonsService(object):
    OPTS_KEYS_TO_PERSIST = ['name']

    def __init__(self, http_client):
        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        _, _, loss_reasons = self.http_client.get("/loss_reasons", params=params)
        return loss_reasons

    def create(self, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for LossReason are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, loss_reason = self.http_client.post("/loss_reasons", body=attributes)
        return loss_reason

    def retrieve(self, id) :
        _, _, loss_reason = self.http_client.get("/loss_reasons/{id}".format(id=id))
        return loss_reason

    def update(self, id, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for LossReason are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, loss_reason = self.http_client.put("/loss_reasons/{id}".format(id=id), body=attributes)
        return loss_reason

    def destroy(self, id) :
        status_code, _, _ = self.http_client.delete("/loss_reasons/{id}".format(id=id))
        return status_code == 204


class NotesService(object):
    OPTS_KEYS_TO_PERSIST = ['content', 'resource_id', 'resource_type']

    def __init__(self, http_client):
        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        _, _, notes = self.http_client.get("/notes", params=params)
        return notes

    def create(self, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for Note are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, note = self.http_client.post("/notes", body=attributes)
        return note

    def retrieve(self, id) :
        _, _, note = self.http_client.get("/notes/{id}".format(id=id))
        return note

    def update(self, id, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for Note are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, note = self.http_client.put("/notes/{id}".format(id=id), body=attributes)
        return note

    def destroy(self, id) :
        status_code, _, _ = self.http_client.delete("/notes/{id}".format(id=id))
        return status_code == 204


class PipelinesService(object):

    def __init__(self, http_client):
        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        _, _, pipelines = self.http_client.get("/pipelines", params=params)
        return pipelines


class SourcesService(object):
    OPTS_KEYS_TO_PERSIST = ['name']

    def __init__(self, http_client):
        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        _, _, sources = self.http_client.get("/sources", params=params)
        return sources

    def create(self, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for Source are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, source = self.http_client.post("/sources", body=attributes)
        return source

    def retrieve(self, id) :
        _, _, source = self.http_client.get("/sources/{id}".format(id=id))
        return source

    def update(self, id, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for Source are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, source = self.http_client.put("/sources/{id}".format(id=id), body=attributes)
        return source

    def destroy(self, id) :
        status_code, _, _ = self.http_client.delete("/sources/{id}".format(id=id))
        return status_code == 204


class StagesService(object):

    def __init__(self, http_client):
        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        _, _, stages = self.http_client.get("/stages", params=params)
        return stages


class TagsService(object):
    OPTS_KEYS_TO_PERSIST = ['name', 'resource_type']

    def __init__(self, http_client):
        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        _, _, tags = self.http_client.get("/tags", params=params)
        return tags

    def create(self, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for Tag are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, tag = self.http_client.post("/tags", body=attributes)
        return tag

    def retrieve(self, id) :
        _, _, tag = self.http_client.get("/tags/{id}".format(id=id))
        return tag

    def update(self, id, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for Tag are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, tag = self.http_client.put("/tags/{id}".format(id=id), body=attributes)
        return tag

    def destroy(self, id) :
        status_code, _, _ = self.http_client.delete("/tags/{id}".format(id=id))
        return status_code == 204


class TasksService(object):
    OPTS_KEYS_TO_PERSIST = ['completed', 'content', 'due_date', 'owner_id', 'remind_at', 'resource_id', 'resource_type']

    def __init__(self, http_client):
        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        _, _, tasks = self.http_client.get("/tasks", params=params)
        return tasks

    def create(self, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for Task are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, task = self.http_client.post("/tasks", body=attributes)
        return task

    def retrieve(self, id) :
        _, _, task = self.http_client.get("/tasks/{id}".format(id=id))
        return task

    def update(self, id, *args, **kwargs):
        if not args and not kwargs:
            raise Exception('attributes for Task are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, task = self.http_client.put("/tasks/{id}".format(id=id), body=attributes)
        return task

    def destroy(self, id) :
        status_code, _, _ = self.http_client.delete("/tasks/{id}".format(id=id))
        return status_code == 204


class UsersService(object):

    def __init__(self, http_client):
        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        _, _, users = self.http_client.get("/users", params=params)
        return users

    def retrieve(self, id) :
        _, _, user = self.http_client.get("/users/{id}".format(id=id))
        return user

    def self(self):
        _, _, resource = self.http_client.get("/users/self")
        return resource
