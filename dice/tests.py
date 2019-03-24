# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from prompt_toolkit.keys import Keys
from selenium import webdriver
import os
import socket
from django.contrib.staticfiles import finders


# Create your tests here.
def login(self):
    self.browser.get(self.live_server_url + '/admin/')

    # Types username and password
    username_field = self.browser.find_element_by_name('username')
    username_field.send_keys('admin')

    password_field = self.browser.find_element_by_name('password')
    password_field.send_keys('admin')
    password_field.send_keys(Keys.RETURN)


def user_login(self):
    # Types username and password
    username_field = self.browser.find_element_by_name('username')
    username_field.send_keys('admin')

    password_field = self.browser.find_element_by_name('password')
    password_field.send_keys('admin')
    password_field.send_keys(Keys.RETURN)