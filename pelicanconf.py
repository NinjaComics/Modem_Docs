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
THEME = "pelican-sober-master"
DEFAULT_PAGINATION = 5
DISPLAY_PAGES_ON_MENU = True
SUMMARY_MAX_LENGTH = None

#URL Settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS ='{date:%Y}/{date:%m}/{slug}.html'

# Feed generation is usually not desired when developing
FEED_DOMAIN = 'http://feeds.feedburner.com'
FEED_ALL_ATOM = 'radioblogrfeeds/main.xml'
#FEED_RSS = 'feeds/feeds.rss'
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('DDG', 'http://www.duckduckgo.com'),)

#Github, Googleplus, Mail
GITHUB = 'https://github.com/NinjaComics'
GPLUS = 'https://plus.google.com/u/0/+RaviSharan/'
MAIL = 'mailto:bhagavathula.ravisharan@gmail.com'

# Social widget
#SOCIAL = (('Github', 'https://github.com/NinjaComics'),)

