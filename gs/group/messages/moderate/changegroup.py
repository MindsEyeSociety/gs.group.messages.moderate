# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013, 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import absolute_import, unicode_literals
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.group.base import GroupForm
from gs.content.form import radio_widget
from .interfaces import IGSModerateGroup


class ChangeGroup(GroupForm):
    label = 'Change Group Moderation'
    pageTemplateFileName = 'browser/templates/changegroup.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
    form_fields = form.Fields(IGSModerateGroup, render_context=False)

    def __init__(self, context, request):
        GroupForm.__init__(self, context, request)
        self.form_fields['moderation'].custom_widget = radio_widget

    @Lazy
    def mailingList(self):
        retval = createObject('groupserver.MailingListInfo', self.context)
        assert retval
        return retval

    def get_mod(self):
        #TODO: Make a IModeratedGroup interface that adapts a group
        #   and tells you the group moderation settings, and allows you
        #   to change it.
        if self.mailingList.is_moderated and self.mailingList.is_moderate_new:
            retval = 'specifiedAndNew'
        elif self.mailingList.is_moderated:
            retval = 'specifiedMembers'
        else:
            retval = 'noModeration'
        assert retval in ('noModeration', 'specifiedAndNew',
            'specifiedMembers')
        return retval

    def setUpWidgets(self, ignore_request=False):
        mod = self.get_mod()
        data = {'moderation': mod}
        self.widgets = form.setUpWidgets(
            self.form_fields, self.prefix, self.context,
            self.request, form=self, data=data,
            ignore_request=ignore_request)

    @form.action(label='Change', failure='handle_change_action_failure')
    def handle_change(self, action, data):
        if (data['moderation'] == 'noModeration'):
            self.set_moderated(False)
            self.set_moderate_new(False)
            self.status = 'Moderation is off: no new posts will be moderated.'
        elif (data['moderation'] == 'specifiedAndNew'):
            self.set_moderated(True)
            self.set_moderate_new(True)
            # Place the mailinlist_members script into the group
            self.status = 'Moderation is on: posts from specified '\
                'members will be moderated, and any new members will '\
                'automatically moderated.'
        elif (data['moderation'] == 'specifiedMembers'):
            self.set_moderated(True)
            self.set_moderate_new(False)
            # Place the mailinlist_members script into the group
            self.status = 'Moderation is on: posts from specified '\
                'members will be moderated.'
        assert type(self.status) == unicode

    def set_moderated(self, val):
        assert type(val) == bool
        groupList = self.mailingList.mlist
        if (not groupList.hasProperty('moderated')):
            groupList.manage_addProperty('moderated', False, 'boolean')
        groupList.manage_changeProperties(moderated=val)

    def set_moderate_new(self, val):
        assert type(val) == bool
        groupList = self.mailingList.mlist
        if (not groupList.hasProperty('moderate_new_members')):
            groupList.manage_addProperty('moderate_new_members', False,
                                            'boolean')
        groupList.manage_changeProperties(moderate_new_members=val)

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = '<p>There is an error:</p>'
        else:
            self.status = '<p>There are errors:</p>'
