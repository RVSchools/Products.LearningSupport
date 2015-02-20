# -*- coding: utf-8 -*-
#
# File: LearningSupport.py
#
# Copyright (c) 2010 by unknown <unknown>
# Generator: ArchGenXML Version 2.5
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


# Product configuration.
#
# The contents of this module will be imported into __init__.py, the
# workflow configuration and every content type module.
#
# If you wish to perform custom configuration, you may put a file
# AppConfig.py in your product's root directory. The items in there
# will be included (by importing) in this file if found.

from Products.CMFCore.permissions import setDefaultRoles
##code-section config-head #fill in your manual code here
##/code-section config-head


PROJECTNAME = "LearningSupport"


# Permissions
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner', 'Contributor'))
ADD_CONTENT_PERMISSIONS = {
    'LearningFolder': 'LearningSupport: Add LearningFolder',
    'Request': 'LearningSupport: Add Request',
}


setDefaultRoles('LearningSupport: Add LearningFolder', ('Manager','Owner'))
setDefaultRoles('LearningSupport: Add Request', ('Manager','Owner'))


product_globals = globals()


DEPENDENCIES = []


PRODUCT_DEPENDENCIES = []
