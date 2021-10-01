# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['profanity_filter', 'profanity_filter.analysis']

package_data = \
{'': ['*'], 'profanity_filter': ['data/*']}

install_requires = \
['cached-property>=1.5,<2.0',
 'more-itertools>=8.0,<9.0',
 'ordered-set-stubs>=0.1.3,<0.2.0',
 'ordered-set>=3.0,<4.0',
 'poetry-version>=0.1.3,<0.2.0',
 'pydantic>=1.3,<2.0',
 'redis>=3.2,<4.0',
 'ruamel.yaml>=0.15.89,<0.16.0',
 'spacy>=3.0,<4.0']

extras_require = \
{':python_version >= "3.7" and python_version < "3.9"': ['dataclasses>=0.6.0,<0.7.0'],
 'deep-analysis': ['hunspell>=0.5.5,<0.6.0',
                   'python-Levenshtein>=0.12.0,<0.13.0',
                   'regex>=2020.0.20,<2022.0.0'],
 'multilingual': ['polyglot>=16.7,<17.0', 'pycld2==0.31', 'PyICU>=2.4,<3.0'],
 'pymorphy2-ru': ['pymorphy2-dicts-ru>=2.4.404381,<3.0.0'],
 'pymorphy2-uk': ['pymorphy2-dicts-uk>=2.4.1,<3.0.0'],
 'web': ['appdirs>=1.4.3,<2.0.0',
         'fastapi>=0.45.0,<0.46.0',
         'uvicorn>=0.11.1,<0.12.0']}

entry_points = \
{'console_scripts': ['profanity_filter = profanity_filter.console:main']}

setup_kwargs = {
    'name': 'profanity-filter2',
    'version': '1.4.3',
    'description': 'A Python library for detecting and filtering profanity',
    'long_description': open('README.md').read(),
    'long_description_content_type': 'text/markdown; charset=UTF-8; variant=GFM',
    'license': 'https://www.gnu.org/licenses/gpl-3.0.en.html',
    'author': 'Roman Inflianskas',
    'author_email': 'infroma@gmail.com',
    'maintainer': 'Ruslan Gareev',
    'maintainer_email': 'mail@ruslangareev.ru',
    'url': 'https://github.com/neorusa/profanity-filter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
