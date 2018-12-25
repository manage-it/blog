#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'TienTN & DinhNV'
SITENAME = 'Manage IT'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Ho_Chi_Minh'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
LINKS = ()

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
SOCIAL = ()

DEFAULT_PAGINATION = 100

THEME = 'pelican-bootstrap3'
PLUGINS = [ "i18n_subsites" ]
# PLUGIN_PATHS = [ "\site-packages\pelican\plugins" ]
PLUGIN_PATHS = [ "./pelican-plugins/i18n_subsites" ]
JINJA_ENVIRONMENT = { "extensions" : [ "jinja2.ext.i18n"] }

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
