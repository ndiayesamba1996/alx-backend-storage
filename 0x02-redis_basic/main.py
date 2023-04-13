#!/usr/bin/env python3
""" Main file """

get_page = __import__('web').get_page

print(get_page('https://colordesigner.io/random-color-generator'))
