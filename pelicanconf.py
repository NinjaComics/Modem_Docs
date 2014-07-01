#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#Basic details
AUTHOR = u'Ravi Sharan'
SITENAME = u'/radio/bin/io'
SITEURL = 'http://ninjacomics.github.io/radioblogr'

#Configuration
TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = u'en'
DELETE_OUTPUT_DIRECTORY = True
THEME = "theme-fdc"
DEFAULT_PAGINATION = 5
DISPLAY_PAGES_ON_MENU = True
SUMMARY_MAX_LENGTH = None

#URL Settings
ARTICLE_URLS = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS ='{date:%Y}/{date:%m}/{slug}.html'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'
FEED_RSS = 'feeds/feeds.rss'
#CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('DDG', 'https://duckduckgo.com/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/NinjaComics'),)

#Theme-related-config
FOUNDATION_FRONT_PAGE_FULL_ARTICLES = True
FOUNDATION_ALTERNATE_FONTS = True
FOUNDATION_TAGS_IN_MOBILE_SIDEBAR = False
FOUNDATION_NEW_ANALYTICS = False
FOUNDATION_ANALYTICS_DOMAIN = ''
FOUNDATION_FOOTER_TEXT = 'Currently blah blah blah'
FOUNDATION_PYGMENT_THEME = 'monokai'
