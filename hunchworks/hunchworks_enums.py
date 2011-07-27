#!/usr/bin/python2.7

"""Enums used throughout Hunchworks."""

__author__ = ('Leah',)
__license__ = 'GPLv3'

import inspect

class Error(Exception):
  pass


class EnumException(Error):
  pass


class Enum(object):
  """Class representing an enum in Python."""
  MAP = {}
  VALUE_LOOKUP = {}

  @classmethod
  def GetChoices(cls):
    """Returns a tuple representing the enum.

    Returns:
      A nested tuple, where each child tuple contains:
        (enum_value, user_facing_enum_value,)
    """
    enum_values = cls.GetEnumValues().items()
    return [(x[1], cls.GetValue(x[0]),) for x in enum_values]

  @classmethod
  def GetValue(cls, lookup):
    """Returns the user facing representation of an enum value.

    Args:
      lookup: The enum value to lookup.

    Returns:
      The user facing representation of the enum value.

    Raises:
      EnumException: Raised if the supplied value doesn't exist on the enum.
    """
    try:
      assert(lookup in cls.GetEnumValues().keys())
    except AssertionError:
      raise EnumException(
          'The supplied lookup value does not exist on the Enum')

    try:
      return cls.VALUE_LOOKUP[lookup]
    except KeyError:
      return lookup.title()

  @classmethod
  def GetEnumValues(cls):
    """Get's the Enum values as a dictionary.

    Returns:
      A dictionary wrapping the Enum values.
    """
    if not cls.MAP:
      # This is a bit of a hack - if the enum is defined in a module called
      # directly from the command line, it also has a __module__ attribute,
      # which the dummy object won't have.
      standard_attrs = ['__module__'] + dir(type('dummy', (object,), {}))
      class_attrs = inspect.getmembers(cls)
      for item in class_attrs:
        if (item[0] not in standard_attrs and
            not inspect.isroutine(item[1]) and
            not isinstance(item[1], (list, dict,))):
          cls.MAP[item[0]] = item[1]

    return cls.MAP


class ConnectionStatus(Enum):
  """Enum representing the possible statuses a user connection can take."""
  BLOCKED = 0
  FRIEND = 1
  ACCEPTED = 2


class UserTitle(Enum):
  """Enum representing the possible titles users can use."""
  MR = 0
  MRS = 1
  MS = 2
  
  FIELD_LOOKUP = {
    MR: 'Mr.',
    MRS: 'Mrs.',
    MS: 'Ms.',
    }


class PrivacyLevel(Enum):
  """Enum representing the various privacy levels available to users."""
  HIDDEN = 0
  CLOSED = 1
  OPEN = 2
  
  FIELD_LOOKUP = {
  	HIDDEN: 'Hidden',
  	CLOSED: 'Closed',
  	OPEN: 'Open',
  	}


class SkillLevel(Enum):
  """Enum representing the various skill levels a user can have in a subject."""
  EXPERT = 0
  SKILLED = 1


class HunchStatus(Enum):
  """Enum representing the statuses a Hunch can take."""
  CONFIRMED = 0
  DENIED = 1
  UNDETERMINED = 2


class Group(Enum):
  """Enum representing the types of groups that can be made"""
  AD_HOC = 0
  ALUMNI = 1
  COMPLEMENT = 2
  CORPORATE = 3
  INTEREST = 4
  NON_PROFIT = 5

  FIELD_LOOKUP = {
    AD_HOC: 'Ad-Hoc',
    ALUMNI: 'Alumni',
    COMPLEMENT: 'Complement',
    CORPORATE: 'Corporate',
    INTEREST: 'Interest',
    NON_PROFIT: 'Non-Profit',
    }

class GroupPrivilege(Enum):
  ADMIN = 0
  MEMBER = 1


ATTACHMENT_TYPES = (
  ('Photo', 'Photo'),
  ('Link', 'Link'),
  ('Video', 'Video'),
)