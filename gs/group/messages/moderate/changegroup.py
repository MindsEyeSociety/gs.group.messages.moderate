# coding=utf-8
from zope.component import createObject
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.group.base.form import GroupForm
from gs.content.form.radio import radio_widget
from interfaces import IGSModerateGroup

class ChangeGroup(GroupForm):
    label = u'Change Group Moderation'
    pageTemplateFileName = 'browser/templates/changegroup.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
    form_fields = form.Fields(IGSModerateGroup, render_context=False)

    def __init__(self, context, request):
        GroupForm.__init__(self, context, request)
        self.form_fields['moderation'].custom_widget = radio_widget
        
    @form.action(label=u'Change', failure='handle_change_action_failure')
    def handle_change(self, action, data):
        self.status = u'I cannot handle change!'
        assert type(self.status) == unicode
        
    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = u'<p>There is an error:</p>'
        else:
            self.status = u'<p>There are errors:</p>'

