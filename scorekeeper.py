#!/usr/bin/python2


from red.app import Red
from models.model import initSchema

initSchema()
Red().start()


