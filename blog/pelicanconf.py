#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'The AOSA Editors'
SITENAME = u'The Architecture of Open Source Applications: The Blog'
SITEURL = ''


TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = ()

THEME = 'bootlex'

SUMMARY_MAX_LENGTH = None

STATIC_PATHS = ["pictures", ]

# Take advantage of the following defaults
STATIC_SAVE_AS = 'static/'

STATIC_URL = 'static/'
STATIC_PATHS = [
    'pictures/',
    ]

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

DEFAULT_PAGINATION = 50
