# -*- coding: utf-8 -*-
#
# File: RequestView.py
#
# Copyright (c) 2010 by unknown <unknown>
# Generator: ArchGenXML Version 2.5
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

##code-section module-header #fill in your manual code here
##/code-section module-header

from zope import interface
from zope import component
from Products.CMFPlone import utils
from Products.Five import BrowserView
from zope.interface import implements
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.LearningSupport.content.Request import Request


class RequestView(BrowserView):
    """
    """

    ##code-section class-header_RequestView #fill in your manual code here
    ##/code-section class-header_RequestView



##code-section module-footer #fill in your manual code here
##/code-section module-footer
