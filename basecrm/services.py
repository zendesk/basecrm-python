#  WARNING: This code is auto-generated from the BaseCRM API Discovery JSON Schema

from decimal import *
from coercion import Coercion

class AccountsService(object):
    """
    :class:`basecrm.AccountsService` is used by :class:`basecrm.Client` to make
    actions related to Account resource.

    Normally you won't instantiate this class directly.
    """


    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def self(self):
        """
        Retrieve account details

        Returns detailed information about your account

        :calls: ``get /accounts/self``
        :rtype: dict
        """

        _, _, resource = self.http_client.get("/accounts/self")
        return resource

class AssociatedContactsService(object):
    """
    :class:`basecrm.AssociatedContactsService` is used by :class:`basecrm.Client` to make
    actions related to AssociatedContact resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for AssociatedContact to send to Base CRM backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['contact_id', 'role']

    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, deal_id, **params):
        """
        Retrieve deal's associated contacts

        Returns all deal associated contacts

        :calls: ``get /deals/{deal_id}/associated_contacts``
        :param int deal_id: Unique identifier of a Deal.
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of AssociatedContacts.
        :rtype: list
        """

        _, _, associated_contacts = self.http_client.get("/deals/{deal_id}/associated_contacts".format(deal_id=deal_id), params=params)
        return associated_contacts

    def create(self, deal_id, *args, **kwargs):
        """
        Create an associated contact

        Creates a deal's associated contact and its role
        If the specified deal or contact does not exist, the request will return an error

        :calls: ``post /deals/{deal_id}/associated_contacts``
        :param int deal_id: Unique identifier of a Deal.
        :param tuple *args: (optional) Single object representing AssociatedContact resource.
        :param dict **kwargs: (optional) AssociatedContact attributes.
        :return: Dictionary that support attriubte-style access and represents newely created AssociatedContact resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for AssociatedContact are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, associated_contact = self.http_client.post("/deals/{deal_id}/associated_contacts".format(deal_id=deal_id), body=attributes)
        return associated_contact

    def destroy(self, deal_id, contact_id) :
        """
        Remove an associated contact

        Remove a deal's associated contact
        If a deal with the supplied unique identifier does not exist, it returns an error
        This operation cannot be undone

        :calls: ``delete /deals/{deal_id}/associated_contacts/{contact_id}``
        :param int deal_id: Unique identifier of a Deal.
        :param int contact_id: Unique identifier of a Contact.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/deals/{deal_id}/associated_contacts/{contact_id}".format(deal_id=deal_id, contact_id=contact_id))
        return status_code == 204

class ContactsService(object):
    """
    :class:`basecrm.ContactsService` is used by :class:`basecrm.Client` to make
    actions related to Contact resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Contact to send to Base CRM backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['address', 'contact_id', 'custom_fields', 'customer_status', 'description', 'email', 'facebook', 'fax', 'first_name', 'industry', 'is_organization', 'last_name', 'linkedin', 'mobile', 'name', 'owner_id', 'phone', 'prospect_status', 'skype', 'tags', 'title', 'twitter', 'website']

    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all contacts

        Returns all contacts available to the user according to the parameters provided

        :calls: ``get /contacts``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Contacts.
        :rtype: list
        """

        _, _, contacts = self.http_client.get("/contacts", params=params)
        return contacts

    def create(self, *args, **kwargs):
        """
        Create a contact

        Create a new contact
        A contact may represent a single individual or an organization

        :calls: ``post /contacts``
        :param tuple *args: (optional) Single object representing Contact resource.
        :param dict **kwargs: (optional) Contact attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Contact resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Contact are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, contact = self.http_client.post("/contacts", body=attributes)
        return contact

    def retrieve(self, id) :
        """
        Retrieve a single contact

        Returns a single contact available to the user, according to the unique contact ID provided
        If the specified contact does not exist, the request will return an error

        :calls: ``get /contacts/{id}``
        :param int id: Unique identifier of a Contact.
        :return: Dictionary that support attriubte-style access and represent Contact resource.
        :rtype: dict
        """

        _, _, contact = self.http_client.get("/contacts/{id}".format(id=id))
        return contact

    def update(self, id, *args, **kwargs):
        """
        Update a contact

        Updates contact information
        If the specified contact does not exist, the request will return an error
        **Notice** When updating contact tags, you need to provide all tags
        Any missing tag will be removed from a contact's tags

        :calls: ``put /contacts/{id}``
        :param int id: Unique identifier of a Contact.
        :param tuple *args: (optional) Single object representing Contact resource which attributes should be updated.
        :param dict **kwargs: (optional) Contact attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Contact resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Contact are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, contact = self.http_client.put("/contacts/{id}".format(id=id), body=attributes)
        return contact

    def destroy(self, id) :
        """
        Delete a contact

        Delete an existing contact
        If the specified contact does not exist, the request will return an error
        This operation cannot be undone

        :calls: ``delete /contacts/{id}``
        :param int id: Unique identifier of a Contact.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/contacts/{id}".format(id=id))
        return status_code == 204

class DealsService(object):
    """
    :class:`basecrm.DealsService` is used by :class:`basecrm.Client` to make
    actions related to Deal resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Deal to send to Base CRM backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['contact_id', 'currency', 'custom_fields', 'hot', 'loss_reason_id', 'name', 'owner_id', 'source_id', 'stage_id', 'last_stage_change_at', 'tags', 'value', 'estimated_close_date', 'customized_win_likelihood', 'added_on']

    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all deals

        Returns all deals available to the user according to the parameters provided

        :calls: ``get /deals``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Deals.
        :rtype: list
        """

        _, _, deals = self.http_client.get("/deals", params=params)
        for deal in deals:
            deal['value'] = Coercion.to_decimal(deal['value'])

        return deals

    def create(self, *args, **kwargs):
        """
        Create a deal

        Create a new deal

        :calls: ``post /deals``
        :param tuple *args: (optional) Single object representing Deal resource.
        :param dict **kwargs: (optional) Deal attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Deal resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Deal are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        if "value" in attributes:
            attributes["value"] = Coercion.to_string(attributes["value"])
        _, _, deal = self.http_client.post("/deals", body=attributes)
        deal["value"] = Coercion.to_decimal(deal["value"])
        return deal

    def retrieve(self, id) :
        """
        Retrieve a single deal

        Returns a single deal available to the user, according to the unique deal ID provided
        If the specified deal does not exist, the request will return an error

        :calls: ``get /deals/{id}``
        :param int id: Unique identifier of a Deal.
        :return: Dictionary that support attriubte-style access and represent Deal resource.
        :rtype: dict
        """

        _, _, deal = self.http_client.get("/deals/{id}".format(id=id))
        deal["value"] = Coercion.to_decimal(deal["value"])
        return deal

    def update(self, id, *args, **kwargs):
        """
        Update a deal

        Updates deal information
        If the specified deal does not exist, the request will return an error
        <figure class="notice">
        In order to modify tags used on a record, you need to supply the entire set
        `tags` are replaced every time they are used in a request
        </figure>

        :calls: ``put /deals/{id}``
        :param int id: Unique identifier of a Deal.
        :param tuple *args: (optional) Single object representing Deal resource which attributes should be updated.
        :param dict **kwargs: (optional) Deal attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Deal resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Deal are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)
        if "value" in attributes:
            attributes["value"] = Coercion.to_string(attributes["value"])

        _, _, deal = self.http_client.put("/deals/{id}".format(id=id), body=attributes)
        deal["value"] = Coercion.to_decimal(deal["value"])
        return deal

    def destroy(self, id) :
        """
        Delete a deal

        Delete an existing deal and remove all of the associated contacts from the deal in a single call
        If the specified deal does not exist, the request will return an error
        This operation cannot be undone

        :calls: ``delete /deals/{id}``
        :param int id: Unique identifier of a Deal.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/deals/{id}".format(id=id))
        return status_code == 204

class DealSourcesService(object):
    """
    :class:`basecrm.DealSourcesService` is used by :class:`basecrm.Client` to make
    actions related to DealSource resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for DealSource to send to Base CRM backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['name', 'resource_type']

    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all sources

        Returns all deal sources available to the user according to the parameters provided

        :calls: ``get /deal_sources``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of DealSources.
        :rtype: list
        """

        _, _, deal_sources = self.http_client.get("/deal_sources", params=params)
        return deal_sources

    def create(self, *args, **kwargs):
        """
        Create a new source

        Creates a new source
        <figure class="notice">
        Source's name **must** be unique
        </figure>

        :calls: ``post /deal_sources``
        :param tuple *args: (optional) Single object representing DealSource resource.
        :param dict **kwargs: (optional) DealSource attributes.
        :return: Dictionary that support attriubte-style access and represents newely created DealSource resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for DealSource are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, deal_source = self.http_client.post("/deal_sources", body=attributes)
        return deal_source

    def retrieve(self, id) :
        """
        Retrieve a single source

        Returns a single source available to the user by the provided id
        If a source with the supplied unique identifier does not exist it returns an error

        :calls: ``get /deal_sources/{id}``
        :param int id: Unique identifier of a DealSource.
        :return: Dictionary that support attriubte-style access and represent DealSource resource.
        :rtype: dict
        """

        _, _, deal_source = self.http_client.get("/deal_sources/{id}".format(id=id))
        return deal_source

    def update(self, id, *args, **kwargs):
        """
        Update a source

        Updates source information
        If the specified source does not exist, the request will return an error
        <figure class="notice">
        If you want to update a source, you **must** make sure source's name is unique
        </figure>

        :calls: ``put /deal_sources/{id}``
        :param int id: Unique identifier of a DealSource.
        :param tuple *args: (optional) Single object representing DealSource resource which attributes should be updated.
        :param dict **kwargs: (optional) DealSource attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated DealSource resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for DealSource are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, deal_source = self.http_client.put("/deal_sources/{id}".format(id=id), body=attributes)
        return deal_source

    def destroy(self, id) :
        """
        Delete a source

        Delete an existing source
        If the specified source does not exist, the request will return an error
        This operation cannot be undone

        :calls: ``delete /deal_sources/{id}``
        :param int id: Unique identifier of a DealSource.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/deal_sources/{id}".format(id=id))
        return status_code == 204

class DealUnqualifiedReasonsService(object):
    """
    :class:`basecrm.DealUnqualifiedReasonsService` is used by :class:`basecrm.Client` to make
    actions related to DealUnqualifiedReason resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for DealUnqualifiedReason to send to Base CRM backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['name']

    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all deal unqualified reasons

        Returns all deal unqualified reasons available to the user according to the parameters provided

        :calls: ``get /deal_unqualified_reasons``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of DealUnqualifiedReasons.
        :rtype: list
        """

        _, _, deal_unqualified_reasons = self.http_client.get("/deal_unqualified_reasons", params=params)
        return deal_unqualified_reasons

    def create(self, *args, **kwargs):
        """
        Create a deal unqualified reason

        Create a new deal unqualified reason
        <figure class="notice">
        Deal unqualified reason's name **must** be unique
        </figure>

        :calls: ``post /deal_unqualified_reasons``
        :param tuple *args: (optional) Single object representing DealUnqualifiedReason resource.
        :param dict **kwargs: (optional) DealUnqualifiedReason attributes.
        :return: Dictionary that support attriubte-style access and represents newely created DealUnqualifiedReason resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for DealUnqualifiedReason are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, deal_unqualified_reason = self.http_client.post("/deal_unqualified_reasons", body=attributes)
        return deal_unqualified_reason

    def retrieve(self, id) :
        """
        Retrieve a single deal unqualified reason

        Returns a single deal unqualified reason available to the user by the provided id
        If a loss reason with the supplied unique identifier does not exist, it returns an error

        :calls: ``get /deal_unqualified_reasons/{id}``
        :param int id: Unique identifier of a DealUnqualifiedReason.
        :return: Dictionary that support attriubte-style access and represent DealUnqualifiedReason resource.
        :rtype: dict
        """

        _, _, deal_unqualified_reason = self.http_client.get("/deal_unqualified_reasons/{id}".format(id=id))
        return deal_unqualified_reason

    def update(self, id, *args, **kwargs):
        """
        Update a deal unqualified reason

        Updates a deal unqualified reason information
        If the specified deal unqualified reason does not exist, the request will return an error
        <figure class="notice">
        If you want to update deal unqualified reason you **must** make sure name of the reason is unique
        </figure>

        :calls: ``put /deal_unqualified_reasons/{id}``
        :param int id: Unique identifier of a DealUnqualifiedReason.
        :param tuple *args: (optional) Single object representing DealUnqualifiedReason resource which attributes should be updated.
        :param dict **kwargs: (optional) DealUnqualifiedReason attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated DealUnqualifiedReason resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for DealUnqualifiedReason are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, deal_unqualified_reason = self.http_client.put("/deal_unqualified_reasons/{id}".format(id=id), body=attributes)
        return deal_unqualified_reason

    def destroy(self, id) :
        """
        Delete a deal unqualified reason

        Delete an existing deal unqualified reason
        If the reason with supplied unique identifier does not exist it returns an error
        This operation cannot be undone

        :calls: ``delete /deal_unqualified_reasons/{id}``
        :param int id: Unique identifier of a DealUnqualifiedReason.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/deal_unqualified_reasons/{id}".format(id=id))
        return status_code == 204

class LeadsService(object):
    """
    :class:`basecrm.LeadsService` is used by :class:`basecrm.Client` to make
    actions related to Lead resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Lead to send to Base CRM backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['address', 'custom_fields', 'description', 'email', 'facebook', 'fax', 'first_name', 'industry', 'last_name', 'linkedin', 'mobile', 'organization_name', 'owner_id', 'phone', 'skype', 'source_id', 'status', 'tags', 'title', 'twitter', 'website']

    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all leads

        Returns all leads available to the user, according to the parameters provided

        :calls: ``get /leads``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Leads.
        :rtype: list
        """

        _, _, leads = self.http_client.get("/leads", params=params)
        return leads

    def create(self, *args, **kwargs):
        """
        Create a lead

        Creates a new lead
        A lead may represent a single individual or an organization

        :calls: ``post /leads``
        :param tuple *args: (optional) Single object representing Lead resource.
        :param dict **kwargs: (optional) Lead attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Lead resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Lead are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, lead = self.http_client.post("/leads", body=attributes)
        return lead

    def retrieve(self, id) :
        """
        Retrieve a single lead

        Returns a single lead available to the user, according to the unique lead ID provided
        If the specified lead does not exist, this query returns an error

        :calls: ``get /leads/{id}``
        :param int id: Unique identifier of a Lead.
        :return: Dictionary that support attriubte-style access and represent Lead resource.
        :rtype: dict
        """

        _, _, lead = self.http_client.get("/leads/{id}".format(id=id))
        return lead

    def update(self, id, *args, **kwargs):
        """
        Update a lead

        Updates lead information
        If the specified lead does not exist, this query returns an error
        <figure class="notice">
        In order to modify tags, you need to supply the entire set of tags
        `tags` are replaced every time they are used in a request
        </figure>

        :calls: ``put /leads/{id}``
        :param int id: Unique identifier of a Lead.
        :param tuple *args: (optional) Single object representing Lead resource which attributes should be updated.
        :param dict **kwargs: (optional) Lead attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Lead resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Lead are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, lead = self.http_client.put("/leads/{id}".format(id=id), body=attributes)
        return lead

    def destroy(self, id) :
        """
        Delete a lead

        Delete an existing lead
        If the specified lead does not exist, this query returns an error
        This operation cannot be undone

        :calls: ``delete /leads/{id}``
        :param int id: Unique identifier of a Lead.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/leads/{id}".format(id=id))
        return status_code == 204

class LeadSourcesService(object):
    """
    :class:`basecrm.LeadSourcesService` is used by :class:`basecrm.Client` to make
    actions related to LeadSource resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for LeadSource to send to Base CRM backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['name', 'resource_type']

    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all sources

        Returns all lead sources available to the user according to the parameters provided

        :calls: ``get /lead_sources``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of LeadSources.
        :rtype: list
        """

        _, _, lead_sources = self.http_client.get("/lead_sources", params=params)
        return lead_sources

    def create(self, *args, **kwargs):
        """
        Create a new source

        Creates a new source
        <figure class="notice">
        Source's name **must** be unique
        </figure>

        :calls: ``post /lead_sources``
        :param tuple *args: (optional) Single object representing LeadSource resource.
        :param dict **kwargs: (optional) LeadSource attributes.
        :return: Dictionary that support attriubte-style access and represents newely created LeadSource resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for LeadSource are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, lead_source = self.http_client.post("/lead_sources", body=attributes)
        return lead_source

    def retrieve(self, id) :
        """
        Retrieve a single source

        Returns a single source available to the user by the provided id
        If a source with the supplied unique identifier does not exist it returns an error

        :calls: ``get /lead_sources/{id}``
        :param int id: Unique identifier of a LeadSource.
        :return: Dictionary that support attriubte-style access and represent LeadSource resource.
        :rtype: dict
        """

        _, _, lead_source = self.http_client.get("/lead_sources/{id}".format(id=id))
        return lead_source

    def update(self, id, *args, **kwargs):
        """
        Update a source

        Updates source information
        If the specified source does not exist, the request will return an error
        <figure class="notice">
        If you want to update a source, you **must** make sure source's name is unique
        </figure>

        :calls: ``put /lead_sources/{id}``
        :param int id: Unique identifier of a LeadSource.
        :param tuple *args: (optional) Single object representing LeadSource resource which attributes should be updated.
        :param dict **kwargs: (optional) LeadSource attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated LeadSource resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for LeadSource are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, lead_source = self.http_client.put("/lead_sources/{id}".format(id=id), body=attributes)
        return lead_source

    def destroy(self, id) :
        """
        Delete a source

        Delete an existing source
        If the specified source does not exist, the request will return an error
        This operation cannot be undone

        :calls: ``delete /lead_sources/{id}``
        :param int id: Unique identifier of a LeadSource.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/lead_sources/{id}".format(id=id))
        return status_code == 204

class LeadUnqualifiedReasonsService(object):
    """
    :class:`basecrm.LeadUnqualifiedReasonsService` is used by :class:`basecrm.Client` to make
    actions related to LeadUnqualifiedReason resource.

    Normally you won't instantiate this class directly.
    """


    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all lead unqualified reasons

        Returns all lead unqualified reasons available to the user according to the parameters provided

        :calls: ``get /lead_unqualified_reasons``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of LeadUnqualifiedReasons.
        :rtype: list
        """

        _, _, lead_unqualified_reasons = self.http_client.get("/lead_unqualified_reasons", params=params)
        return lead_unqualified_reasons

class LineItemsService(object):
    """
    :class:`basecrm.LineItemsService` is used by :class:`basecrm.Client` to make
    actions related to LineItem resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for LineItem to send to Base CRM backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['product_id', 'value', 'variation', 'currency', 'quantity']

    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, order_id, **params):
        """
        Retrieve order's line items

        Returns all line items associated to order

        :calls: ``get /orders/{order_id}/line_items``
        :param int order_id: Unique identifier of a Order.
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of LineItems.
        :rtype: list
        """

        _, _, line_items = self.http_client.get("/orders/{order_id}/line_items".format(order_id=order_id), params=params)
        return line_items

    def create(self, order_id, *args, **kwargs):
        """
        Create a line item

        Adds a new line item to an existing order
        Line items correspond to products in the catalog, so first you must create products
        Because products allow defining different prices in different currencies, when creating a line item, the parameter currency is required

        :calls: ``post /orders/{order_id}/line_items``
        :param int order_id: Unique identifier of a Order.
        :param tuple *args: (optional) Single object representing LineItem resource.
        :param dict **kwargs: (optional) LineItem attributes.
        :return: Dictionary that support attriubte-style access and represents newely created LineItem resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for LineItem are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, line_item = self.http_client.post("/orders/{order_id}/line_items".format(order_id=order_id), body=attributes)
        return line_item

    def retrieve(self, order_id, id) :
        """
        Retrieve a single line item

        Returns a single line item of an order, according to the unique line item ID provided

        :calls: ``get /orders/{order_id}/line_items/{id}``
        :param int order_id: Unique identifier of a Order.
        :param int id: Unique identifier of a LineItem.
        :return: Dictionary that support attriubte-style access and represent LineItem resource.
        :rtype: dict
        """

        _, _, line_item = self.http_client.get("/orders/{order_id}/line_items/{id}".format(order_id=order_id, id=id))
        return line_item

    def destroy(self, order_id, id) :
        """
        Delete a line item

        Remove an order's line item
        This operation cannot be undone

        :calls: ``delete /orders/{order_id}/line_items/{id}``
        :param int order_id: Unique identifier of a Order.
        :param int id: Unique identifier of a LineItem.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/orders/{order_id}/line_items/{id}".format(order_id=order_id, id=id))
        return status_code == 204

class LossReasonsService(object):
    """
    :class:`basecrm.LossReasonsService` is used by :class:`basecrm.Client` to make
    actions related to LossReason resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for LossReason to send to Base CRM backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['name']

    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all reasons

        Returns all deal loss reasons available to the user according to the parameters provided

        :calls: ``get /loss_reasons``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of LossReasons.
        :rtype: list
        """

        _, _, loss_reasons = self.http_client.get("/loss_reasons", params=params)
        return loss_reasons

    def create(self, *args, **kwargs):
        """
        Create a loss reason

        Create a new loss reason
        <figure class="notice">
        Loss reason's name **must** be unique
        </figure>

        :calls: ``post /loss_reasons``
        :param tuple *args: (optional) Single object representing LossReason resource.
        :param dict **kwargs: (optional) LossReason attributes.
        :return: Dictionary that support attriubte-style access and represents newely created LossReason resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for LossReason are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, loss_reason = self.http_client.post("/loss_reasons", body=attributes)
        return loss_reason

    def retrieve(self, id) :
        """
        Retrieve a single reason

        Returns a single loss reason available to the user by the provided id
        If a loss reason with the supplied unique identifier does not exist, it returns an error

        :calls: ``get /loss_reasons/{id}``
        :param int id: Unique identifier of a LossReason.
        :return: Dictionary that support attriubte-style access and represent LossReason resource.
        :rtype: dict
        """

        _, _, loss_reason = self.http_client.get("/loss_reasons/{id}".format(id=id))
        return loss_reason

    def update(self, id, *args, **kwargs):
        """
        Update a loss reason

        Updates a loss reason information
        If the specified loss reason does not exist, the request will return an error
        <figure class="notice">
        If you want to update loss reason you **must** make sure name of the reason is unique
        </figure>

        :calls: ``put /loss_reasons/{id}``
        :param int id: Unique identifier of a LossReason.
        :param tuple *args: (optional) Single object representing LossReason resource which attributes should be updated.
        :param dict **kwargs: (optional) LossReason attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated LossReason resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for LossReason are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, loss_reason = self.http_client.put("/loss_reasons/{id}".format(id=id), body=attributes)
        return loss_reason

    def destroy(self, id) :
        """
        Delete a reason

        Delete an existing loss reason
        If the reason with supplied unique identifier does not exist it returns an error
        This operation cannot be undone

        :calls: ``delete /loss_reasons/{id}``
        :param int id: Unique identifier of a LossReason.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/loss_reasons/{id}".format(id=id))
        return status_code == 204

class NotesService(object):
    """
    :class:`basecrm.NotesService` is used by :class:`basecrm.Client` to make
    actions related to Note resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Note to send to Base CRM backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['content', 'resource_id', 'resource_type']

    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all notes

        Returns all notes available to the user, according to the parameters provided

        :calls: ``get /notes``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Notes.
        :rtype: list
        """

        _, _, notes = self.http_client.get("/notes", params=params)
        return notes

    def create(self, *args, **kwargs):
        """
        Create a note

        Create a new note and associate it with one of the resources listed below:
        * [Leads](/docs/rest/reference/leads)
        * [Contacts](/docs/rest/reference/contacts)
        * [Deals](/docs/rest/reference/deals)

        :calls: ``post /notes``
        :param tuple *args: (optional) Single object representing Note resource.
        :param dict **kwargs: (optional) Note attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Note resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Note are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, note = self.http_client.post("/notes", body=attributes)
        return note

    def retrieve(self, id) :
        """
        Retrieve a single note

        Returns a single note available to the user, according to the unique note ID provided
        If the note ID does not exist, this request will return an error

        :calls: ``get /notes/{id}``
        :param int id: Unique identifier of a Note.
        :return: Dictionary that support attriubte-style access and represent Note resource.
        :rtype: dict
        """

        _, _, note = self.http_client.get("/notes/{id}".format(id=id))
        return note

    def update(self, id, *args, **kwargs):
        """
        Update a note

        Updates note information
        If the note ID does not exist, this request will return an error

        :calls: ``put /notes/{id}``
        :param int id: Unique identifier of a Note.
        :param tuple *args: (optional) Single object representing Note resource which attributes should be updated.
        :param dict **kwargs: (optional) Note attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Note resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Note are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, note = self.http_client.put("/notes/{id}".format(id=id), body=attributes)
        return note

    def destroy(self, id) :
        """
        Delete a note

        Delete an existing note
        If the note ID does not exist, this request will return an error
        This operation cannot be undone

        :calls: ``delete /notes/{id}``
        :param int id: Unique identifier of a Note.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/notes/{id}".format(id=id))
        return status_code == 204

class OrdersService(object):
    """
    :class:`basecrm.OrdersService` is used by :class:`basecrm.Client` to make
    actions related to Order resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Order to send to Base CRM backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['deal_id', 'discount']

    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all orders

        Returns all orders available to the user according to the parameters provided

        :calls: ``get /orders``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Orders.
        :rtype: list
        """

        _, _, orders = self.http_client.get("/orders", params=params)
        return orders

    def create(self, *args, **kwargs):
        """
        Create an order

        Create a new order for a deal
        User needs to have access to the deal to create an order
        Each deal can have at most one order and error is returned when attempting to create more

        :calls: ``post /orders``
        :param tuple *args: (optional) Single object representing Order resource.
        :param dict **kwargs: (optional) Order attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Order resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Order are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, order = self.http_client.post("/orders", body=attributes)
        return order

    def retrieve(self, id) :
        """
        Retrieve a single order

        Returns a single order available to the user, according to the unique order ID provided
        If the specified order does not exist, the request will return an error

        :calls: ``get /orders/{id}``
        :param int id: Unique identifier of a Order.
        :return: Dictionary that support attriubte-style access and represent Order resource.
        :rtype: dict
        """

        _, _, order = self.http_client.get("/orders/{id}".format(id=id))
        return order

    def update(self, id, *args, **kwargs):
        """
        Update an order

        Updates order information
        If the specified order does not exist, the request will return an error

        :calls: ``put /orders/{id}``
        :param int id: Unique identifier of a Order.
        :param tuple *args: (optional) Single object representing Order resource which attributes should be updated.
        :param dict **kwargs: (optional) Order attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Order resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Order are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, order = self.http_client.put("/orders/{id}".format(id=id), body=attributes)
        return order

    def destroy(self, id) :
        """
        Delete an order

        Delete an existing order and remove all of the associated line items in a single call
        If the specified order does not exist, the request will return an error
        This operation cannot be undone

        :calls: ``delete /orders/{id}``
        :param int id: Unique identifier of a Order.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/orders/{id}".format(id=id))
        return status_code == 204

class PipelinesService(object):
    """
    :class:`basecrm.PipelinesService` is used by :class:`basecrm.Client` to make
    actions related to Pipeline resource.

    Normally you won't instantiate this class directly.
    """


    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all pipelines

        Returns all pipelines available to the user, according to the parameters provided

        :calls: ``get /pipelines``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Pipelines.
        :rtype: list
        """

        _, _, pipelines = self.http_client.get("/pipelines", params=params)
        return pipelines

class ProductsService(object):
    """
    :class:`basecrm.ProductsService` is used by :class:`basecrm.Client` to make
    actions related to Product resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Product to send to Base CRM backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['name', 'description', 'sku', 'active', 'cost', 'cost_currency', 'prices', 'max_discount', 'max_markup']

    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all products

        Returns all products available to the user according to the parameters provided

        :calls: ``get /products``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Products.
        :rtype: list
        """

        _, _, products = self.http_client.get("/products", params=params)
        return products

    def create(self, *args, **kwargs):
        """
        Create a product

        Create a new product

        :calls: ``post /products``
        :param tuple *args: (optional) Single object representing Product resource.
        :param dict **kwargs: (optional) Product attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Product resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Product are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, product = self.http_client.post("/products", body=attributes)
        return product

    def retrieve(self, id) :
        """
        Retrieve a single product

        Returns a single product, according to the unique product ID provided
        If the specified product does not exist, the request will return an error

        :calls: ``get /products/{id}``
        :param int id: Unique identifier of a Product.
        :return: Dictionary that support attriubte-style access and represent Product resource.
        :rtype: dict
        """

        _, _, product = self.http_client.get("/products/{id}".format(id=id))
        return product

    def update(self, id, *args, **kwargs):
        """
        Update a product

        Updates product information
        If the specified product does not exist, the request will return an error
        <figure class="notice"><p>In order to modify prices used on a record, you need to supply the entire set
        <code>prices</code> are replaced every time they are used in a request
        </p></figure>

        :calls: ``put /products/{id}``
        :param int id: Unique identifier of a Product.
        :param tuple *args: (optional) Single object representing Product resource which attributes should be updated.
        :param dict **kwargs: (optional) Product attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Product resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Product are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, product = self.http_client.put("/products/{id}".format(id=id), body=attributes)
        return product

    def destroy(self, id) :
        """
        Delete a product

        Delete an existing product from the catalog
        Existing orders and line items are not affected
        If the specified product does not exist, the request will return an error
        This operation cannot be undone
        Products can be removed only by an account administrator

        :calls: ``delete /products/{id}``
        :param int id: Unique identifier of a Product.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/products/{id}".format(id=id))
        return status_code == 204

class SourcesService(object):
    """
    :class:`basecrm.SourcesService` is used by :class:`basecrm.Client` to make
    actions related to Source resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Source to send to Base CRM backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['name']

    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all sources

        Returns all deal sources available to the user according to the parameters provided

        :calls: ``get /sources``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Sources.
        :rtype: list
        """

        _, _, sources = self.http_client.get("/sources", params=params)
        return sources

    def create(self, *args, **kwargs):
        """
        Create a source

        Creates a new source
        <figure class="notice">
        Source's name **must** be unique
        </figure>

        :calls: ``post /sources``
        :param tuple *args: (optional) Single object representing Source resource.
        :param dict **kwargs: (optional) Source attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Source resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Source are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, source = self.http_client.post("/sources", body=attributes)
        return source

    def retrieve(self, id) :
        """
        Retrieve a single source

        Returns a single source available to the user by the provided id
        If a source with the supplied unique identifier does not exist it returns an error

        :calls: ``get /sources/{id}``
        :param int id: Unique identifier of a Source.
        :return: Dictionary that support attriubte-style access and represent Source resource.
        :rtype: dict
        """

        _, _, source = self.http_client.get("/sources/{id}".format(id=id))
        return source

    def update(self, id, *args, **kwargs):
        """
        Update a source

        Updates source information
        If the specified source does not exist, the request will return an error
        <figure class="notice">
        If you want to update a source, you **must** make sure source's name is unique
        </figure>

        :calls: ``put /sources/{id}``
        :param int id: Unique identifier of a Source.
        :param tuple *args: (optional) Single object representing Source resource which attributes should be updated.
        :param dict **kwargs: (optional) Source attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Source resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Source are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, source = self.http_client.put("/sources/{id}".format(id=id), body=attributes)
        return source

    def destroy(self, id) :
        """
        Delete a source

        Delete an existing source
        If the specified source does not exist, the request will return an error
        This operation cannot be undone

        :calls: ``delete /sources/{id}``
        :param int id: Unique identifier of a Source.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/sources/{id}".format(id=id))
        return status_code == 204

class StagesService(object):
    """
    :class:`basecrm.StagesService` is used by :class:`basecrm.Client` to make
    actions related to Stage resource.

    Normally you won't instantiate this class directly.
    """


    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all stages

        Returns all stages available to the user, according to the parameters provided

        :calls: ``get /stages``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Stages.
        :rtype: list
        """

        _, _, stages = self.http_client.get("/stages", params=params)
        return stages

class TagsService(object):
    """
    :class:`basecrm.TagsService` is used by :class:`basecrm.Client` to make
    actions related to Tag resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Tag to send to Base CRM backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['name', 'resource_type']

    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all tags

        Returns all tags available to the user, according to the parameters provided

        :calls: ``get /tags``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Tags.
        :rtype: list
        """

        _, _, tags = self.http_client.get("/tags", params=params)
        return tags

    def create(self, *args, **kwargs):
        """
        Create a tag

        Creates a new tag
        **Notice** the tag's name **must** be unique within the scope of the resource_type

        :calls: ``post /tags``
        :param tuple *args: (optional) Single object representing Tag resource.
        :param dict **kwargs: (optional) Tag attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Tag resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Tag are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, tag = self.http_client.post("/tags", body=attributes)
        return tag

    def retrieve(self, id) :
        """
        Retrieve a single tag

        Returns a single tag available to the user according to the unique ID provided
        If the specified tag does not exist, this query will return an error

        :calls: ``get /tags/{id}``
        :param int id: Unique identifier of a Tag.
        :return: Dictionary that support attriubte-style access and represent Tag resource.
        :rtype: dict
        """

        _, _, tag = self.http_client.get("/tags/{id}".format(id=id))
        return tag

    def update(self, id, *args, **kwargs):
        """
        Update a tag

        Updates a tag's information
        If the specified tag does not exist, this query will return an error
        **Notice** if you want to update a tag, you **must** make sure the tag's name is unique within the scope of the specified resource

        :calls: ``put /tags/{id}``
        :param int id: Unique identifier of a Tag.
        :param tuple *args: (optional) Single object representing Tag resource which attributes should be updated.
        :param dict **kwargs: (optional) Tag attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Tag resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Tag are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, tag = self.http_client.put("/tags/{id}".format(id=id), body=attributes)
        return tag

    def destroy(self, id) :
        """
        Delete a tag

        Deletes an existing tag
        If the specified tag is assigned to any resource, we will remove this tag from all such resources
        If the specified tag does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /tags/{id}``
        :param int id: Unique identifier of a Tag.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/tags/{id}".format(id=id))
        return status_code == 204

class TasksService(object):
    """
    :class:`basecrm.TasksService` is used by :class:`basecrm.Client` to make
    actions related to Task resource.

    Normally you won't instantiate this class directly.
    """

    """
    Allowed attributes for Task to send to Base CRM backend servers.
    """
    OPTS_KEYS_TO_PERSIST = ['completed', 'content', 'due_date', 'owner_id', 'remind_at', 'resource_id', 'resource_type']

    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all tasks

        Returns all tasks available to the user, according to the parameters provided
        If you ask for tasks without any parameter provided Base API will return you both **floating** and **related** tasks
        Although you can narrow the search set to either of them via query parameters

        :calls: ``get /tasks``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Tasks.
        :rtype: list
        """

        _, _, tasks = self.http_client.get("/tasks", params=params)
        return tasks

    def create(self, *args, **kwargs):
        """
        Create a task

        Creates a new task
        You can create either a **floating** task or create a **related** task and associate it with one of the resource types below:
        * [Leads](/docs/rest/reference/leads)
        * [Contacts](/docs/rest/reference/contacts)
        * [Deals](/docs/rest/reference/deals)

        :calls: ``post /tasks``
        :param tuple *args: (optional) Single object representing Task resource.
        :param dict **kwargs: (optional) Task attributes.
        :return: Dictionary that support attriubte-style access and represents newely created Task resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Task are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, task = self.http_client.post("/tasks", body=attributes)
        return task

    def retrieve(self, id) :
        """
        Retrieve a single task

        Returns a single task available to the user according to the unique task ID provided
        If the specified task does not exist, this query will return an error

        :calls: ``get /tasks/{id}``
        :param int id: Unique identifier of a Task.
        :return: Dictionary that support attriubte-style access and represent Task resource.
        :rtype: dict
        """

        _, _, task = self.http_client.get("/tasks/{id}".format(id=id))
        return task

    def update(self, id, *args, **kwargs):
        """
        Update a task

        Updates task information
        If the specified task does not exist, this query will return an error

        :calls: ``put /tasks/{id}``
        :param int id: Unique identifier of a Task.
        :param tuple *args: (optional) Single object representing Task resource which attributes should be updated.
        :param dict **kwargs: (optional) Task attributes to update.
        :return: Dictionary that support attriubte-style access and represents updated Task resource.
        :rtype: dict
        """

        if not args and not kwargs:
            raise Exception('attributes for Task are missing')

        attributes = args[0] if args else kwargs
        attributes = dict((k, v) for k, v in attributes.iteritems() if k in self.OPTS_KEYS_TO_PERSIST)

        _, _, task = self.http_client.put("/tasks/{id}".format(id=id), body=attributes)
        return task

    def destroy(self, id) :
        """
        Delete a task

        Delete an existing task
        If the specified task does not exist, this query will return an error
        This operation cannot be undone

        :calls: ``delete /tasks/{id}``
        :param int id: Unique identifier of a Task.
        :return: True if the operation succeeded.
        :rtype: bool
        """

        status_code, _, _ = self.http_client.delete("/tasks/{id}".format(id=id))
        return status_code == 204

class TextMessagesService(object):
    """
    :class:`basecrm.TextMessagesService` is used by :class:`basecrm.Client` to make
    actions related to TextMessage resource.

    Normally you won't instantiate this class directly.
    """


    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve text messages

        Returns Text Messages, according to the parameters provided

        :calls: ``get /text_messages``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of TextMessages.
        :rtype: list
        """

        _, _, text_messages = self.http_client.get("/text_messages", params=params)
        return text_messages

    def retrieve(self, id) :
        """
        Retrieve a single text message

        Returns a single text message according to the unique  ID provided
        If the specified user does not exist, this query returns an error

        :calls: ``get /text_messages/{id}``
        :param int id: Unique identifier of a TextMessage.
        :return: Dictionary that support attriubte-style access and represent TextMessage resource.
        :rtype: dict
        """

        _, _, text_message = self.http_client.get("/text_messages/{id}".format(id=id))
        return text_message

class UsersService(object):
    """
    :class:`basecrm.UsersService` is used by :class:`basecrm.Client` to make
    actions related to User resource.

    Normally you won't instantiate this class directly.
    """


    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve all users

        Returns all users, according to the parameters provided

        :calls: ``get /users``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Users.
        :rtype: list
        """

        _, _, users = self.http_client.get("/users", params=params)
        return users

    def retrieve(self, id) :
        """
        Retrieve a single user

        Returns a single user according to the unique user ID provided
        If the specified user does not exist, this query returns an error

        :calls: ``get /users/{id}``
        :param int id: Unique identifier of a User.
        :return: Dictionary that support attriubte-style access and represent User resource.
        :rtype: dict
        """

        _, _, user = self.http_client.get("/users/{id}".format(id=id))
        return user

    def self(self):
        """
        Retrieve an authenticating user

        Returns a single authenticating user, according to the authentication credentials provided

        :calls: ``get /users/self``
        :rtype: dict
        """

        _, _, resource = self.http_client.get("/users/self")
        return resource

class VisitsService(object):
    """
    :class:`basecrm.VisitsService` is used by :class:`basecrm.Client` to make
    actions related to Visit resource.

    Normally you won't instantiate this class directly.
    """


    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve visits

        Returns Visits, according to the parameters provided

        :calls: ``get /visits``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of Visits.
        :rtype: list
        """

        _, _, visits = self.http_client.get("/visits", params=params)
        return visits

class VisitOutcomesService(object):
    """
    :class:`basecrm.VisitOutcomesService` is used by :class:`basecrm.Client` to make
    actions related to VisitOutcome resource.

    Normally you won't instantiate this class directly.
    """


    def __init__(self, http_client):
        """
        :param :class:`basecrm.HttpClient` http_client: Pre configured high-level http client.
        """

        self.__http_client = http_client

    @property
    def http_client(self):
        return self.__http_client


    def list(self, **params):
        """
        Retrieve visit outcomes

        Returns Visit Outcomes, according to the parameters provided

        :calls: ``get /visit_outcomes``
        :param dict params: (optional) Search options.
        :return: List of dictionaries that support attriubte-style access, which represent collection of VisitOutcomes.
        :rtype: list
        """

        _, _, visit_outcomes = self.http_client.get("/visit_outcomes", params=params)
        return visit_outcomes
