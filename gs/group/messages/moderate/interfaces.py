# coding=utf-8
from zope.interface import Interface
from zope.schema import Choice
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

noModeration = SimpleTerm(
  'noModeration', 'noModeration',
  u'No moderation.')
specifiedMembers = SimpleTerm(
  'specifiedMembers', 'specifiedMembers',
  u'Moderate specified members only.')
specifiedAndNew = SimpleTerm(
  'specifiedAndNew', 'specifiedAndNew',
  u'Moderate specified members, and all new members that join this group.'
)
moderationLevels = SimpleVocabulary([noModeration, specifiedMembers,
  specifiedAndNew])

class IGSModerateGroup(Interface):
    moderation = Choice(title=u'Group Moderation',
      description=u'The group moderation settings.',
      vocabulary=moderationLevels,
      default='noModeration')

