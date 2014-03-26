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
from __future__ import unicode_literals
from zope.interface import Interface
from zope.schema import Choice
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

noModeration = SimpleTerm('noModeration', 'noModeration', 'No moderation.')
specifiedMembers = SimpleTerm('specifiedMembers', 'specifiedMembers',
                              'Moderate specified members only.')
specifiedAndNew = SimpleTerm('specifiedAndNew', 'specifiedAndNew',
      'Moderate specified members, and all new members that join this group.')
moderationLevels = SimpleVocabulary([noModeration, specifiedMembers,
                                      specifiedAndNew])


class IGSModerateGroup(Interface):
    moderation = Choice(title='Group Moderation',
      description='The group moderation settings.',
      vocabulary=moderationLevels,
      default='noModeration')
