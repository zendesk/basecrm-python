import pkgutil
import unittest


def all():
    names = [
        'http_client',
        'accounts_service',
        'associated_contacts_service',
        'contacts_service',
        'deals_service',
        'deal_sources_service',
        'deal_unqualified_reasons_service',
        'leads_service',
        'lead_sources_service',
        'lead_unqualified_reasons_service',
        'line_items_service',
        'loss_reasons_service',
        'notes_service',
        'orders_service',
        'pipelines_service',
        'products_service',
        'sources_service',
        'stages_service',
        'tags_service',
        'tasks_service',
        'text_messages_service',
        'users_service',
        'visits_service',
        'visit_outcomes_service',
        'sync',
        'sync_service',
        'coercion'
    ]
    module_names = ['basecrm.test.test_' + name for name in names]
    loader = unittest.TestLoader()
    return loader.loadTestsFromNames(module_names)
