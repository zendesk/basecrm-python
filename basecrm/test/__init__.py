import pkgutil
import unittest


def all():
    names = [
        'http_client',
        'accounts_service',
        'associated_contacts_service',
        'contacts_service',
        'deals_service',
        'leads_service',
        'loss_reasons_service',
        'notes_service',
        'pipelines_service',
        'sources_service',
        'stages_service',
        'tags_service',
        'tasks_service',
        'users_service',
        'sync',
        'sync_service',
        'coercion'
    ]
    module_names = ['basecrm.test.test_' + name for name in names]
    loader = unittest.TestLoader()
    return loader.loadTestsFromNames(module_names)
