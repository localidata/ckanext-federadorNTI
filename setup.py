from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-federadorNTI',
	version=version,
	description="Federador contra http://datos.gob.es/catalogo",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Localidata',
	author_email='info@localidata.com',
	url='http://www.localidata.com',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.malaga'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points='''	
	[paste.paster_command]
	federadorNTI = ckanext.malaga.commands:malagae
        [ckan.plugins]
        federadorNTI=ckanext.malaga.plugin:malagae
	''',
)

