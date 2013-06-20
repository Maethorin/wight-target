#!/usr/bin/python
# -*- coding: utf-8 -*-

from cow.server import Server
from handlers.home import HomeHandler


class WightTargetServer(Server):
    def get_handlers(self):
        return (
            ('/', HomeHandler),
        )

if __name__ == '__main__':
    WightTargetServer.run()

