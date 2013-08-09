# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.group.messages.moderate',
    version=version,
    description="Moderate messages in a GroupServer group",
    long_description=open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: Zope Public License',
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux"
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='groupserver member moderate moderation administration',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='http://groupserver.org/',
    license='ZPL 2.1',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.group', 'gs.group.messages'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'zope.cachedescriptors',
        'zope.formlib',
        'zope.interface',
        'zope.schema',
        'Zope2',
        'gs.content.layout',
        'gs.content.form',
        'gs.group.base',
        'gs.group.home',
        'gs.group.member.base',
        'gs.group.messages.base',
        'Products.GSGroup',
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)
