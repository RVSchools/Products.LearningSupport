# -*- coding: utf-8 -*-
#
# File: LearningFolder.py
#
# Copyright (c) 2010 by unknown <unknown>
# Generator: ArchGenXML Version 2.5
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.folder import ATFolderSchema
from Products.LearningSupport.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

LearningFolder_schema = ATFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class LearningFolder(ATFolder):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ILearningFolder)

    meta_type = 'LearningFolder'
    _at_rename_after_creation = True

    schema = LearningFolder_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(LearningFolder, PROJECTNAME)
# end of class LearningFolder

##code-section module-footer #fill in your manual code here
##/code-section module-footer

