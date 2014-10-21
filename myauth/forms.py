from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm, UserChangeForm as AuthUserChangeForm
from django import forms
 
from myauth.models import User
 
class UserCreationForm(AuthUserCreationForm):
 
  receive_newsletter = forms.BooleanField(required=False)
 
  class Meta:
    model = User
 
  ## This method is defined in django.contrib.auth.form.UserCreationForm and explicitly links to auth.models.User so we need to override it
  def clean_username(self):
    username = self.cleaned_data["username"]
    try:
      User._default_manager.get(username=username)
    except User.DoesNotExist:
      return username
    raise forms.ValidationError(
      self.error_messages['duplicate_username'],
      code='duplicate_username',
    )
 
 
class UserChangeForm(AuthUserChangeForm):
 
  receive_newsletter = forms.BooleanField(required=False)
 
  class Meta:
    model = User