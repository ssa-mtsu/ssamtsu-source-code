#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'المشرف'
SITENAME = 'النادي السعودي بجامعة وسط تينيسي'
SITEURL = 'http://www.ssamtsu.com'

PATH = 'content'

######################
DELETE_OUTPUT_DIRECTORY = True

THEME = 'theme/notmyidea'

STATIC_PATHS = ['.']

AUTHOR_SAVE_AS = False
TAG_SAVE_AS = False

CATEGORY_SAVE_AS = False
USE_FOLDER_AS_CATEGORY = False

DIRECT_TEMPLATES = ['index']

PAGINATED_DIRECT_TEMPLATES = ['']
DEFAULT_PAGINATION = False

DEFAULT_CATEGORY = 'misc'

OUTPUT_RETENTION = [".hg", ".git", ".bzr", "CNAME"]

THEME_STATIC_PATHS = ['static']

DISQUS_SITENAME = 'ssamtsu'

# "directory/dcare/kisd_r_kids" to "directory/dcare"
def go_parent(inStr):
    num = 0
    string = ""
    for x in inStr.split('/')[0:-1]:
        if num != 0:
            string = string + "/"
        string = string + x
        num += 1
    return string

JINJA_FILTERS = {
    'go_parent': go_parent,
}

######################

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
