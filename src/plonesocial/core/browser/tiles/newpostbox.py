# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.tiles import Tile
from plonesocial.core.browser.stream import StreamBase
from plonesocial.core.integration import PLONESOCIAL
from zope.component import getMultiAdapter


class NewPostBoxTile(Tile, StreamBase):

    index = ViewPageTemplateFile('templates/new-post-box-tile.pt')

