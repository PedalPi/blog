#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# https://github.com/arulrajnet/attila-demo/blob/master/pelicanconf.py

AUTHOR = 'SrMouraSilva'
SITENAME = 'Pedal Pi - Blog'
SITEURL = 'http://pedalpi.github.com/blog'
#SITEURL = ''
#DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = ['images']
HEADER_COVER = 'images/guitar-tiny.jpg'
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
THEME = "./themes/attila-1.1"
OUTPUT_PATH = 'docs/'
GOOGLE_ANALYTICS = 'UA-105440758-1'

#THEME = "/home/paulo/git/pedalpi-blog/output"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('You can add links in your config file', '#'),
    ('Another social link', '#'),
)

DEFAULT_PAGINATION = 3

MENUITEMS = (
    ('Home', './'),
    ('Site', 'http://pedalpi.github.io/'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
