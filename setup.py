from distutils.core import setup

from ripwrap import __VERSION__

setup(
    name = 'ripwrap',
    version = __VERSION__,
    description = 'A wrapper for ReSTinPeace, for Django applications.',
    long_description = open('README').read()
    author = 'P.C. Shyamshankar',

    packages = ['ripwrap'],

    url = 'http://github.com/sykora/django-ripwrap/',
    license = 'GNU General Public License v3.0',

    classifiers = (
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
    )
)
