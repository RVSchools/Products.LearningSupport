# -*- coding: utf-8 -*-
#
# File: setuphandlers.py
#
# Copyright (c) 2010 by unknown <unknown>
# Generator: ArchGenXML Version 2.5
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


import logging
logger = logging.getLogger('LearningSupport: setuphandlers')
# from Products.LearningSupport.config import PROJECTNAME
# from Products.LearningSupport.config import DEPENDENCIES
# import os
from Products.CMFCore.utils import getToolByName
# import transaction
##code-section HEAD
##/code-section HEAD

def isNotLearningSupportProfile(context):
    return context.readDataFile("LearningSupport_marker.txt") is None



def updateRoleMappings(context):
    """after workflow changed update the roles mapping. this is like pressing
    the button 'Update Security Setting' and portal_workflow"""
    if isNotLearningSupportProfile(context): return 
    wft = getToolByName(context.getSite(), 'portal_workflow')
    wft.updateRoleMappings()


def postInstall(context):
    """Called as at the end of the setup process. """
    # the right place for your custom code
    if isNotLearningSupportProfile(context): return 
    site = context.getSite()


##code-section FOOT
##/code-section FOOT
