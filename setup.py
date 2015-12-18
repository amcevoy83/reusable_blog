import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'reusable-blog-app',
    version='1.0.0',
    packages = ['reusable_blog'],
    include_package_data = True,
    description="A simple Django app to create blogs",
    long_description=README,
    url='http://www.github.com/amcevoy83',
    author='Aoife McEvoy',
    author_email='aoifemcevoy@gmail.com',
    ##the below describe whate categories the app can be catalogued under
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django'
        'Intended Audience :: Developers',
        'Licence :: OSI Approved :: BSD Licence',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    ##the below will be installed when we install the package/app via pip
    install_requires = [
        'Pillow',
        'django_forms_bootstrap',
        'Disqus'
    ],
)