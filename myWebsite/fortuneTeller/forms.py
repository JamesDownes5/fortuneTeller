from django import forms

class BirthdayForm(forms.Form):
    usersBirthday = forms.CharField(label='Please enter your Birthday day. (Example 9 December)')

class OptionForm(forms.Form):
    btn = forms.CharField()