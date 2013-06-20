#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from tornado.web import RequestHandler

class HomeHandler(RequestHandler):
    def get(self):
        test = random.randint(0, 100)
        if test % 10 == 0:
            raise Exception
        self.write(self.application.config.TESTCONF)

