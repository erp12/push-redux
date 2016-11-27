#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
sys.path.append('.')

AUTHOR = u'Eddie'
SITENAME = u'Push Redux'
SITEURL = 'erp12.github.io/push-redux'

PATH = 'content'
OUTPUT_PATH = 'docs/'
#THEME = 'themes/push-redux-theme'
THEME = 'themes/push-redux-theme'

TIMEZONE = 'EST'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Push Discourse', 'https://push-language.hampshire.edu/'),
         ('Push Homepage', 'http://faculty.hampshire.edu/lspector/push.html'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

INDEX_SAVE_AS = 'blog_index.html'

# Plugin stuff
PLUGIN_PATHS = ['plugins']
PLUGINS = ['page-hierarchy']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'