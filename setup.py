# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='django-add-get-parameters',
    version='0.3',
    description='Template tag to add get parameter to the current url.',
    long_description='Template tag to add get parameter to the current url.',
    author='Robin Ramael',
    author_email='robin.ramael@gmail.com',
    url='http://github.com/RobinRamael/django-add-get-parameters',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)