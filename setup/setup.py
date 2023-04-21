from setuptools import setup

setup(
    name='odoo-addons-design-themes',
    setup_requires=['setuptools-odoo'],
    odoo_addons={
        'odoo_version_override': '12.0',
    },
)

