#!/usr/bin/python2.7
# Forms used in the project
# Author: Auto created by Texas
# Date: 2011-06-20
# License:  This  program  is  free  software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the  Free Software Foundation; either version 3 of the License, or (at your
# option)  any later version. This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.

import models

from django import forms
from django.forms import ModelForm
from django.forms.widgets import PasswordInput 

class SignInForm(ModelForm):
  class Meta:
    model= models.HwUser
    widgets = {
      'password': PasswordInput()
      }

class SignUpForm(ModelForm):
  skill_name = forms.CharField( max_length=100 )

  class Meta:
    model= models.HwUser
    exclude = ( 
	'show_profile_reminder', 'bio_text', 'phone', 'skills',
	'skype_name', 'website', 'profile_picture', 'screen_name',
	'messenger_service', 'education', 'classes', 'user_id',
	'location_interests', 'roles', 'hunches', 'invited_users', 'groups'
	)
    widgets = {
      'password': PasswordInput()
      }

class AddHunchForm(ModelForm):
  class Meta:
    model = models.HwHunch
    exclude = (
      'hunch_id','creator_id','time_created','status','privacy',
      'strength','language','location','skills','groups','users',
      'invited_users',)

class HomepageForm(ModelForm):
  class Meta:
    model = models.HwUser
