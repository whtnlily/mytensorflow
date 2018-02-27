#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
网络爬虫教程
"""
import urllib.request as req
import requests
import selenium
from selenium import webdriver
import aiohttp
import aiodns
import lxml
from bs4 import BeautifulSoup
import pyquery
import tesserocr
from PIL import Image
import pymysql
import pymongo
import redis
import flask
import tornado.ioloop
import tornado.web

brower = webdriver.PhantomJS()
brower.get('https://www.baidu.com')
print(brower.current_url)
response = req.urlopen("http://www.baidu.com")
print(response.read())
soup = BeautifulSoup('<p>Hello</p>','lxml')
print(soup.p.string)

image = Image.open('D:\\temp\\image.png')
print(tesserocr.image_to_text(image))













