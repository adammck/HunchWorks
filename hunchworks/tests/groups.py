#!/usr/bin/env python

from hunchworks.models import Group
from hunchworks.utils.tests import FunctionalTest


class GroupViewsTest(FunctionalTest):
  fixtures = ["test_users", "test_groups"]

  def test_get_index(self):
    self.GET("/groups")
    self.assertCss("div.group", 3)

  def test_get_show(self):
    self.GET("/groups/1")
    self.assertCss("div.group")

  def test_get_edit(self):
    self.GET("/groups/1/edit")
    self.assertCss("form.group")

  def test_post_edit(self):
    self._post_form("/groups/1/edit", {
      "abbreviation": "Z",
      "members": "2, 3"
    })

    group = Group.objects.get(pk=1)
    self.assertEqual(group.name, "Alpha")     # unchanged
    self.assertEqual(group.abbreviation, "Z") # changed

    m_pks = set(group.members.values_list("pk", flat=True))
    self.assertEqual(m_pks, set([2, 3]))

  def test_get_new(self):
    self.GET("/groups/create")
    self.assertCss("form.group")