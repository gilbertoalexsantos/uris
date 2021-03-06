===
URI
===

uris[pider] is a command line tool made in python to interact with the Uri_ Online Judge.

Currently, it supports the commands:

- Get submissions (with filter options)
- Get last submissions
- Submit a solution

=======
Install
=======

First, you need to instal the Scrapy package (more information in install_)

.. code-block:: python
   
   pip install Scrapy

I hope that everything will be fine with Scrapy... If not, consult the manual: install_

Finally, to install the uris package, just use:

.. code-block:: python
   
   pip install git+https://github.com/gilbertoalexsantos/uris.git

I particularly recommend to install in a virtual environment (virtualenvwrapper_)

========
Examples
========

.. code-block:: python
   
   uris last 3

It'll get the last 3 submissions

.. code-block:: python
   
   uris subs -lang=java

It'll get the last submissions (20) with the filters:

- Language: Java

.. code-block:: python
   
   uris subs -lang=py3 --answer=tle --code=1899

It'll get the last submissons with the filters:

- Language: Python 3
- Answer: Time Limit Exceed
- Problem Code: 1899

The same command could be rewritten:

.. code-block:: python
   
   uris subs --language=py3 -a=tle -c=1899

.. code-block:: python
   
   uris sub -lang=c++ -code=1788 -sc="source_code.cpp"

It'll submit the problem with the filters:

- Language: C++
- Problem Code: 1788
- Source Code: "source_code.cpp". It's the relative path (you can use absolute path too)

For more information, use the command:

.. code-block:: python
   
   uris help

Or use the help command flag:

.. code-block:: python
   
   uris subs --help

============                
Requirements
============

- Python 2.7

=========
Uninstall
=========

Just use:

.. code-block:: python
   
   pip uninstall uris

I really recommend to use virtualenvwrapper_. With that, you just need to create a new virtualenv

.. code-block:: python
   
   mkvirtualenv uris

And, in the virtualenv, install the uri package. If you want to uninstall, just remove the virtualenv

.. code-block:: python
   
   rmvirtualenv uris

Simple!

You'll probably want to remove the settings file. It lays in the user directory

.. code-block:: python
   
   ~/.uris_settings.json

====
TODO
====

- Use an insurance prompt when typing the password
- Encrypt the password in the settings file




.. _Uri: https://www.urionlinejudge.com.br
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.org/en/latest/
.. _install: http://doc.scrapy.org/en/latest/intro/install.html
