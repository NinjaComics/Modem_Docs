#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#Basic details
AUTHOR = u'Ravi Sharan'
SITENAME = u'Ravi Sharan\'s /radio/bin/io'
SITEURL = 'http://ninjacomics.github.io/radioblogr'

#Configuration
TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = u'en'
DELETE_OUTPUT_DIRECTORY = True
THEME = "random-theme"
PATH = "content"

#URL Settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS ='{date:%Y}/{date:%m}/{slug}.html'

# Feed generation is usually not desired when developing
FEED_DOMAIN = 'http://feeds.feedburner.com'
FEED_ALL_ATOM = 'radioblogrfeeds'

#STATIC Path settings

STATIC_PATHS = ['images', 'pdfs', 'contents/2016/08/images']
