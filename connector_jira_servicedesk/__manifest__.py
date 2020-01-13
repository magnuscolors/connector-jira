# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'JIRA Connector - Service Desk Extension',
    'version': '10.0',
    'author': 'Magnus - Willem Hulshof',
    'license': 'AGPL-3',
    'category': 'Connector',
    'depends': [
        'connector_jira',
    ],
    'website': 'https://github.com/camptocamp/connector-jira',
    'data': [
        'views/jira_backend_views.xml',
        'views/project_project_views.xml',
        'views/project_link_jira_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}
