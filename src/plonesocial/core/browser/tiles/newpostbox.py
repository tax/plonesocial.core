# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.tiles import Tile
from plonesocial.core.browser.stream import StreamBase


class NewPostBoxTile(Tile, StreamBase):

    index = ViewPageTemplateFile('templates/new-post-box-tile.pt')

