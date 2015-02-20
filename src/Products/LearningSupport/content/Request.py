# -*- coding: utf-8 -*-
#
# File: Request.py
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
import interfaces, DateTime

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.LearningSupport.config import *

PROV_LIST = ['Alberta','British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrador', 'Northwest Territories', 'Nova Scotia', 'Nunavut', 'Ontario', 'Prince Edward Island', 'Québec', 'Saskatchewan', 'Yukon']

SCHOOLS = ['', 'A.E. Bowers Elementary School', 'Airdrie Middle School', 'Banded Peak School', 'Bearspaw School', 'Beiseker Community School', 'Bert Church High School', 'Bow Valley High School', 'Chestermere High School', 'Chestermere Lake Middle School', 'Cochrane High School', 'Crossfield Elementary School', 'Ecole Manachaban Middle School', 'Edge School', 'Edwards Elementary School', 'Elbow Valley Elementary School', 'Elizabeth Barrett Elementary School', 'George McDougall High School', 'Glenbow Elementary School', 'Indus Elementary School', 'Kathyrn School', 'Langdon School', 'Meadowbrook Middle School', 'Mitford Middle School', 'Muriel Clayton Middle School', 'Nose Creek Elementary School', 'Prairie Waters Elementary School', 'Prince of Peace Lutheran School', 'R.J. Hawkey Elementary School', 'Rainbow Creek Elementary School', 'Ralph McCall School', 'Rocky View Learning Connections', 'South Beiseker Colony', 'Springbank Community High', 'Springbank Middle School', 'W.G. Murdoch School', 'West Haven Colony', 'Westbrook School']

# Prepare the vocabulary for Year dropdowns
now = DateTime.DateTime()
year = now.year()+0
prev = year-20
YEARS = range(year, prev, -1)
YEARS.insert(0, '')
# string field vocabulary should consist of strings, not integers
YEARS = [str(y) for y in YEARS]

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='title',
        widget=StringField._properties['widget'](
            label="Alberta Ed. ID #",
            label_msgid='LearningSupport_label_title',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Student Identification Information",
        validators=('isABID',),
        accessor="Title",
    ),
    StringField(
        name='surname',
        widget=StringField._properties['widget'](
            label="Legal Surname",
            label_msgid='LearningSupport_label_surname',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Student Identification Information",
    ),
    StringField(
        name='altSurname',
        widget=StringField._properties['widget'](
            label="Alternate Surname (AKA)",
            label_msgid='LearningSupport_label_altSurname',
            i18n_domain='LearningSupport',
        ),
        schemata="Student Identification Information",
    ),
    StringField(
        name='givenName',
        widget=StringField._properties['widget'](
            label="Given Name(s)",
            label_msgid='LearningSupport_label_givenName',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Student Identification Information",
    ),
    StringField(
        name='altGivenName',
        widget=StringField._properties['widget'](
            label="Alternate Given Name(s) (AKA)",
            label_msgid='LearningSupport_label_altGivenName',
            i18n_domain='LearningSupport',
        ),
        schemata="Student Identification Information",
    ),
    DateTimeField(
        name='dob',
        widget=DateTimeField._properties['widget'](
            label="Date of Birth",
            show_hm=False,
            label_msgid='LearningSupport_label_dob',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Student Identification Information",
    ),
    IntegerField(
        name='age',
        widget=IntegerField._properties['widget'](
            label='Age',
            label_msgid='LearningSupport_label_age',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Student Identification Information",
    ),
    StringField(
        name='gender',
        widget=SelectionWidget(
            label='Gender',
            label_msgid='LearningSupport_label_gender',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Student Identification Information",
        vocabulary= ['Male', 'Female'],
    ),
    StringField(
        name='school',
        widget=SelectionWidget(
            label='School',
            label_msgid='LearningSupport_label_school',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Student Identification Information",
        vocabulary= SCHOOLS,
    ),
    StringField(
        name='grade',
        widget=SelectionWidget(
            label='Grade',
            label_msgid='LearningSupport_label_grade',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Student Identification Information",
        vocabulary= ['', 'Kindergarten', 'Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade 5', 'Grade 6', 'Grade 7', 'Grade 8', 'Grade 9', 'Grade 10', 'Grade 11', 'Grade 12'],
    ),
    StringField(
        name='exceptionCode',
        widget=StringField._properties['widget'](
            label="Special Education Exception Code",
            label_msgid='LearningSupport_label_exceptionCode',
            i18n_domain='LearningSupport',
        ),
        schemata="Student Identification Information",
    ),
    BooleanField(
        name='native',
        widget=BooleanField._properties['widget'](
            label="Aboriginal Student?",
            label_msgid='LearningSupport_label_native',
            i18n_domain='LearningSupport',
        ),
        schemata="Student Identification Information",
    ),
    StringField(
        name='treaty',
        widget=StringField._properties['widget'](
            label="Treaty Number",
            label_msgid='LearningSupport_label_treaty',
            i18n_domain='LearningSupport',
        ),
        schemata="Student Identification Information",
    ),
    StringField(
        name='custody',
        widget=SelectionWidget(
            label="Parental Custody/Access Order",
            description="In some instances a student may be the subject of a parental custody or access order.  Does such an order exist?",
            label_msgid='LearningSupport_label_custody',
            description_msgid='LearningSupport_help_custody',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Parent / Guardian Information",
        vocabulary= ['Yes', 'No'],
    ),
    StringField(
        name='g1Custody',
        widget=SelectionWidget(
            label="Custodial Parent?",
            label_msgid='LearningSupport_label_g1Custody',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Parent / Guardian Information",
        vocabulary= ['Custodial', 'Non-Custodial'],
    ),
    StringField(
        name='g1Surname',
        widget=StringField._properties['widget'](
            label="Surname",
            label_msgid='LearningSupport_label_g1Surname',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Parent / Guardian Information",
    ),
    StringField(
        name='g1GivenName',
        widget=StringField._properties['widget'](
            label="Given Name(s)",
            label_msgid='LearningSupport_label_g1GivenName',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Parent / Guardian Information",
    ),
    StringField(
        name='g1Street',
        widget=StringField._properties['widget'](
            label="Street Address",
            label_msgid='LearningSupport_label_g1Street',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Parent / Guardian Information",
    ),
    StringField(
        name='g1City',
        widget=StringField._properties['widget'](
            label="City",
            label_msgid='LearningSupport_label_g1City',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Parent / Guardian Information",
    ),
    StringField(
        name='g1Province',
        widget=SelectionWidget(
            label="Province",
            label_msgid='LearningSupport_label_g1Province',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Parent / Guardian Information",
        vocabulary= PROV_LIST,
    ),
    StringField(
        name='g1Postal',
        widget=StringField._properties['widget'](
            label="Parent 1 Postal Code",
            label_msgid='LearningSupport_label_g1Postal',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Parent / Guardian Information",
        validators=('isPostalCode',),
    ),
    StringField(
        name='g1Phone',
        widget=StringField._properties['widget'](
            label="Home Phone",
            label_msgid='LearningSupport_label_g1Phone',
            i18n_domain='LearningSupport',
        ),
        schemata="Parent / Guardian Information",
        validators=('isUSPhoneNumber',),
    ),
    StringField(
        name='g1PhoneWork',
        widget=StringField._properties['widget'](
            label="Work Phone",
            label_msgid='LearningSupport_label_g1PhoneWork',
            i18n_domain='LearningSupport',
        ),
        schemata="Parent / Guardian Information",
        validators=('isUSPhoneNumber',),
    ),
    StringField(
        name='g1PhoneCell',
        widget=StringField._properties['widget'](
            label="Parent 1 Cell Phone",
            label_msgid='LearningSupport_label_g1PhoneCell',
            i18n_domain='LearningSupport',
        ),
        schemata="Parent / Guardian Information",
        validators=('isUSPhoneNumber',),
    ),
    StringField(
        name='g2Custody',
        widget=SelectionWidget(
            label="Custodial Parent?",
            label_msgid='LearningSupport_label_g2Custody',
            i18n_domain='LearningSupport',
        ),
        schemata="Parent / Guardian Information",
        vocabulary= ['Custodial', 'Non-Custodial'],
    ),
    StringField(
        name='g2Surname',
        widget=StringField._properties['widget'](
            label="Surname",
            label_msgid='LearningSupport_label_g2Surname',
            i18n_domain='LearningSupport',
        ),
        schemata="Parent / Guardian Information",
    ),
    StringField(
        name='g2GivenName',
        widget=StringField._properties['widget'](
            label="Given Name(s)",
            label_msgid='LearningSupport_label_g2GivenName',
            i18n_domain='LearningSupport',
        ),
        schemata="Parent / Guardian Information",
    ),
    StringField(
        name='g2Street',
        widget=StringField._properties['widget'](
            label="Street Address",
            label_msgid='LearningSupport_label_g2Street',
            i18n_domain='LearningSupport',
        ),
        schemata="Parent / Guardian Information",
    ),
    StringField(
        name='g2City',
        widget=StringField._properties['widget'](
            label="City",
            label_msgid='LearningSupport_label_g2City',
            i18n_domain='LearningSupport',
        ),
        schemata="Parent / Guardian Information",
    ),
    StringField(
        name='g2Province',
        widget=SelectionWidget(
            label="Province",
            label_msgid='LearningSupport_label_g2Province',
            i18n_domain='LearningSupport',
        ),
        schemata="Parent / Guardian Information",
        vocabulary= PROV_LIST,
    ),
    StringField(
        name='g2Postal',
        widget=StringField._properties['widget'](
            label="Postal Code",
            label_msgid='LearningSupport_label_g2Postal',
            i18n_domain='LearningSupport',
        ),
        schemata="Parent / Guardian Information",
        validators=('isPostalCode',),
    ),
    StringField(
        name='g2Phone',
        widget=StringField._properties['widget'](
            label="Home Phone",
            label_msgid='LearningSupport_label_g2Phone',
            i18n_domain='LearningSupport',
        ),
        schemata="Parent / Guardian Information",
        validators=('isUSPhoneNumber',),
    ),
    StringField(
        name='g2PhoneWork',
        widget=StringField._properties['widget'](
            label="Work Phone",
            label_msgid='LearningSupport_label_g2PhoneWork',
            i18n_domain='LearningSupport',
        ),
        schemata="Parent / Guardian Information",
        validators=('isUSPhoneNumber',),
    ),
    StringField(
        name='g2PhoneCell',
        widget=StringField._properties['widget'](
            label="Cell Phone",
            label_msgid='LearningSupport_label_g2PhoneCell',
            i18n_domain='LearningSupport',
        ),
        schemata="Parent / Guardian Information",
        validators=('isUSPhoneNumber',),
    ),
    StringField(
        name='cfsaCare',
        widget=SelectionWidget(
            label="Under CFSA (Child & Family Services Authority) Care?",
            description="In some instances a student may be under the care of Child & Family Services Authority.  Does this authority exist?",
            label_msgid='LearningSupport_label_cfsaCare',
            description_msgid='LearningSupport_help_cfsaCare',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Child & Family Services Authority",
        vocabulary= ['Yes', 'No'],
    ),
    StringField(
        name='cfsaName',
        widget=StringField._properties['widget'](
            label="Social Worker's Name",
            label_msgid='LearningSupport_label_cfsaName',
            i18n_domain='LearningSupport',
        ),
        schemata="Child & Family Services Authority",
    ),
    StringField(
        name='cfsaEmail',
        widget=StringField._properties['widget'](
            label="Social Worker's Email",
            label_msgid='LearningSupport_label_cfsaEmail',
            i18n_domain='LearningSupport',
        ),
        schemata="Child & Family Services Authority",
        validators=('isEmail',),
    ),
    StringField(
        name='cfsaPhone',
        widget=StringField._properties['widget'](
            label="Social Worker's Phone",
            label_msgid='LearningSupport_label_cfsaPhone',
            i18n_domain='LearningSupport',
        ),
        schemata="Child & Family Services Authority",
        validators=('isUSPhoneNumber',),
    ),
    LinesField(
        name='resources',
        widget=MultiSelectionWidget(
            label="Requested Resources",
            format="checkbox",
            label_msgid='LearningSupport_label_resources',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Learning Support Team Request",
        multiValued=1,
        vocabulary= ['Psychologist', 'Learning Specialist', 'Family School Liaison', 'Mental Health', 'Occupational Therapist', 'SLP (Grades 5-12 only)', 'COPE (Kindergarten-Grade 8 only)', 'Other (please specify below)'],
    ),
    TextField(
        name='resources_other',
        widget=TextAreaWidget(
            label="Other Requested Resources",
            description="*ONLY* fill in this field if 'Other' is checked off above.",
            label_msgid='LearningSupport_label_resources_other',
            i18n_domain='LearningSupport',
            rows=2,
        ),
        schemata="Learning Support Team Request",
    ),
    TextField(
        name='reasons',
        widget=TextAreaWidget(
            label="Please provide the reason for this request",
            label_msgid='LearningSupport_label_reasons',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Learning Support Team Request",
    ),
    TextField(
        name='outcomes',
        widget=TextAreaWidget(
            label="Please provide the intended outcome of this request",
            label_msgid='LearningSupport_label_outcomes',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Learning Support Team Request",
    ),
    StringField(
        name='ext1Name',
        widget=StringField._properties['widget'](
            label='Agency',
            label_msgid='LearningSupport_label_ext1Name',
            i18n_domain='LearningSupport',
        ),
        schemata="Other External Agencies / Professionals Involved",
    ),
    StringField(
        name='ext2Name',
        widget=StringField._properties['widget'](
            label='Agency',
            label_msgid='LearningSupport_label_ext2Name',
            i18n_domain='LearningSupport',
        ),
        schemata="Other External Agencies / Professionals Involved",
    ),
    StringField(
        name='ext3Name',
        widget=StringField._properties['widget'](
            label='Agency',
            label_msgid='LearningSupport_label_ext3Name',
            i18n_domain='LearningSupport',
        ),
        schemata="Other External Agencies / Professionals Involved",
    ),
    StringField(
        name='ext4Name',
        widget=StringField._properties['widget'](
            label='Agency',
            label_msgid='LearningSupport_label_ext3Name',
            i18n_domain='LearningSupport',
        ),
        schemata="Other External Agencies / Professionals Involved",
    ),
    StringField(
        name='ext5Name',
        widget=StringField._properties['widget'](
            label='Agency',
            label_msgid='LearningSupport_label_ext3Name',
            i18n_domain='LearningSupport',
        ),
        schemata="Other External Agencies / Professionals Involved",
    ),
    StringField(
        name='ext1Date',
        widget=SelectionWidget(
            label='Date of Involvement',
            label_msgid='LearningSupport_label_ext1Date',
            i18n_domain='LearningSupport',
        ),
        schemata="Other External Agencies / Professionals Involved",
        vocabulary=YEARS,
    ),
    StringField(
        name='ext2Date',
        widget=SelectionWidget(
            label='Date of Involvement',
            label_msgid='LearningSupport_label_ext2Date',
            i18n_domain='LearningSupport',
        ),
        schemata="Other External Agencies / Professionals Involved",
        vocabulary=YEARS,
    ),
    StringField(
        name='ext3Date',
        widget=SelectionWidget(
            label='Date of Involvement',
            label_msgid='LearningSupport_label_ext3Date',
            i18n_domain='LearningSupport',
        ),
        schemata="Other External Agencies / Professionals Involved",
        vocabulary=YEARS,
    ),
    StringField(
        name='ext4Date',
        widget=SelectionWidget(
            label='Date of Involvement',
            label_msgid='LearningSupport_label_ext3Date',
            i18n_domain='LearningSupport',
        ),
        schemata="Other External Agencies / Professionals Involved",
        vocabulary=YEARS,
    ),
    StringField(
        name='ext5Date',
        widget=SelectionWidget(
            label='Date of Involvement',
            label_msgid='LearningSupport_label_ext3Date',
            i18n_domain='LearningSupport',
        ),
        schemata="Other External Agencies / Professionals Involved",
        vocabulary=YEARS,
    ),                                                                                                                                                                
    TextField(
        name='supportInfo',
        widget=TextAreaWidget(
            label="Summary of Relevant Information",
            description='Please provide a summary of any RELEVANT information to support this request.  This could include family background, student history, precipitating events, previous professional involvement, previous assessments (including hearing/vision assessment), other referrals (e.g. attendance), diagnoses, medication, or other pertinent information',
            label_msgid='LearningSupport_label_supportInfo',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Supporting Information",
    ),
    TextField(
        name='schoolInfo',
        widget=TextAreaWidget(
            label="School Programs and Strategies in Place",
            description='Please list school-based strategies, accommodations, and interventions currently in place.',
            label_msgid='LearningSupport_label_schoolInfo',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="Supporting Information",
    ),
    StringField(
        name='assessment1',
        widget=StringField._properties['widget'](
            label="Assessment 1",
            description='Please provide the type of formalized assessment.',
            label_msgid='LearningSupport_label_assessment1',
            i18n_domain='LearningSupport',
        ),
        schemata="Supporting Information",
    ),

    StringField(
        name='assessment2',
        widget=StringField._properties['widget'](
            label="Assessment 2",
            description='Please provide the type of formalized assessment.',
            label_msgid='LearningSupport_label_assessment2',
            i18n_domain='LearningSupport',
        ),
        schemata="Supporting Information",
    ),
    StringField(
        name='assessment3',
        widget=StringField._properties['widget'](
            label="Assessment 3",
            description='Please provide the type of formalized assessment.',
            label_msgid='LearningSupport_label_assessment3',
            i18n_domain='LearningSupport',
        ),
        schemata="Supporting Information",
    ),
    StringField(
        name='assessment4',
        widget=StringField._properties['widget'](
            label="Assessment 4",
            description='Please provide the type of formalized assessment.',
            label_msgid='LearningSupport_label_assessment4',
            i18n_domain='LearningSupport',
        ),
        schemata="Supporting Information",
    ),
    StringField(
        name='assessment5',
        widget=StringField._properties['widget'](
            label="Assessment 5",
            description='Please provide the type of formalized assessment.',
            label_msgid='LearningSupport_label_assessment5',
            i18n_domain='LearningSupport',
        ),
        schemata="Supporting Information",
    ),
    BooleanField(
        name='screenVision',
        widget=BooleanField._properties['widget'](
            label="Vision Screen",
            description='Check this field if this student has been screened for vision.',
            label_msgid='LearningSupport_label_screenVision',
            i18n_domain='LearningSupport',
        ),
        schemata="Supporting Information",
    ),
    BooleanField(
        name='screenHearing',
        widget=BooleanField._properties['widget'](
            label="Hearing Screen",
            description='Check this field if this student has been screened for hearing.',
            label_msgid='LearningSupport_label_screenHearing',
            i18n_domain='LearningSupport',
        ),
        schemata="Supporting Information",
    ),
    StringField(
        name='ass1date',
        widget=SelectionWidget(
            label='Year of Assessment',
            description='Please provide the date of this assessment.',
            label_msgid='LearningSupport_label_ass1date',
            i18n_domain='LearningSupport',
        ),
        schemata="Supporting Information",
        vocabulary=YEARS,
    ),
    StringField(
        name='ass2date',
        widget=SelectionWidget(
            label='Year of Assessment',
            description='Please provide the date of this assessment.',
            label_msgid='LearningSupport_label_ass2date',
            i18n_domain='LearningSupport',
        ),
        schemata="Supporting Information",
        vocabulary=YEARS,
    ),
    StringField(
        name='ass3date',
        widget=SelectionWidget(
            label='Year of Assessment',
            description='Please provide the date of this assessment.',
            label_msgid='LearningSupport_label_ass3date',
            i18n_domain='LearningSupport',
        ),
        schemata="Supporting Information",
        vocabulary=YEARS,
    ),
    StringField(
        name='ass4date',
        widget=SelectionWidget(
            label='Year of Assessment',
            description='Please provide the date of this assessment.',
            label_msgid='LearningSupport_label_ass4date',
            i18n_domain='LearningSupport',
        ),
        schemata="Supporting Information",
        vocabulary=YEARS,
    ),
    StringField(
        name='ass5date',
        widget=SelectionWidget(
            label='Year of Assessment',
            description='Please provide the date of this assessment.',
            label_msgid='LearningSupport_label_ass5date',
            i18n_domain='LearningSupport',
        ),
        schemata="Supporting Information",
        vocabulary=YEARS,
    ),
    StringField(
        name='screenVisionDate',
        widget=SelectionWidget(
            label="Year of Assessment",
            description='Please provide the date of this assessment.',
            label_msgid='LearningSupport_screenVisionDate',
            i18n_domain='LearningSupport',
        ),
        schemata="Supporting Information",
        vocabulary=YEARS,
    ),
    StringField(
        name='screenHearingDate',
        widget=SelectionWidget(
            label="Year of Assessment",
            description='Please provide the date of this assessment.',
            label_msgid='LearningSupport_screenHearingDate',
            i18n_domain='LearningSupport',
        ),
        schemata="Supporting Information",
        vocabulary=YEARS,
    ),
    StringField(
        name='pscName',
        widget=StringField._properties['widget'](
            label="Primary School Contact's (PSC) Name",
            label_msgid='LearningSupport_label_pscName',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="School Contact Information",
    ),
    StringField(
        name='pscTitle',
        widget=StringField._properties['widget'](
            label="PSC's Title",
            label_msgid='LearningSupport_label_pscTitle',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="School Contact Information",
    ),
    StringField(
        name='pscEmail',
        widget=StringField._properties['widget'](
            label="PSC's Email",
            label_msgid='LearningSupport_label_pscEmail',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="School Contact Information",
        validators=('isEmail',),
    ),
    StringField(
        name='pscPhone',
        widget=StringField._properties['widget'](
            label="PSC's Phone",
            label_msgid='LearningSupport_label_pscPhone',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="School Contact Information",
        validators=('isUSPhoneNumber',),
    ),
    StringField(
        name='pscAdminName',
        widget=StringField._properties['widget'](
            label="School Administrator",
            label_msgid='LearningSupport_label_pscAdminName',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="School Contact Information",
    ),
    BooleanField(
        name='pscAdminAware',
        widget=BooleanField._properties['widget'](
            label="School Administrator is aware of and agrees with this request",
            label_msgid='LearningSupport_label_pscAdminAware',
            i18n_domain='LearningSupport',
        ),
        required=1,
        schemata="School Contact Information",
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Request_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
Request_schema['id'].schemata = 'Student Identification Information'
##/code-section after-schema

class Request(BaseFolder, BrowserDefaultMixin):
    """Texting the object type docstring...
    """
    typeDescription="Rocky View staff completing this form are seeking additional services and supports to complement those provided directly by their school resources.  Parental permission for a specific learning support service is NOT TO BE SOUGHT at this stage; however, parents as members of the Learning Team for their child, should be made aware of this request for additional support.  Parental permission will be required following review of the request and determination of service status."
    
    security = ClassSecurityInfo()

    implements(interfaces.IRequest)

    meta_type = 'Request'
    _at_rename_after_creation = True

    schema = Request_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Request, PROJECTNAME)
# end of class Request

##code-section module-footer #fill in your manual code here
##/code-section module-footer

