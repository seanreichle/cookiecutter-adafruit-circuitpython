{# create list of requirements #}
{%- set list = namespace(items=["Adafruit-Blinka"]) -%}
{%- if cookiecutter.requires_bus_device in ["y", "yes"] -%}
    {%- do list.items.append("adafruit-circuitpython-busdevice") -%}
{%- endif %}
{%- if cookiecutter.requires_register in ["y", "yes"] %}
    {%- do list.items.append("adafruit-circuitpython-register") -%}
{%- endif %}
{%- if cookiecutter.other_requirements != "" %}
    {%- set tests = cookiecutter.other_requirements -%}
    {%- do list.items.extend(tests.replace(" ", "").split(",")) -%}
{%- endif -%}
{# put keywords into an iterable list, based on word wrapping #}
{%- set kw_list = namespace(kw_list=[]) -%}
{%- set wrapped = cookiecutter.library_keywords|wordwrap(break_long_words=False) -%}
{%- do kw_list.kw_list.extend(wrapped.split("\n")) -%}
"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='adafruit-circuitpython-{{ cookiecutter.library_name|lower }}',

    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    description='{{ cookiecutter.library_description }}',
    long_description=long_description,
    long_description_content_type='text/x-rst',

    # The project's main homepage.
    url='https://github.com/adafruit/Adafruit_CircuitPython_{{ cookiecutter.library_name|capitalize }}',

    # Author details
    author='Adafruit Industries',
    author_email='circuitpython@adafruit.com',

    install_requires=[
{{ list.items|unique|join(",\n")|indent(width=8,first=True) }}
    ],

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Hardware',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='{{ kw_list.kw_list|join("'\n'")|indent(width=13) }}',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # TODO: IF LIBRARY FILES ARE A PACKAGE FOLDER,
    #       CHANGE `py_modules=['...']` TO `packages=['...']`
    py_modules=['{%- if cookiecutter.library_prefix != "" -%}{{ cookiecutter.library_prefix|lower }}_{%- endif -%}{{- cookiecutter.library_name|lower -}}'],
)
