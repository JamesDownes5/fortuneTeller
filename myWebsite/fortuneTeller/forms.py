from django import forms

class BirthdayForm(forms.Form):
    usersBirthday = forms.CharField(label='')
    auto_id = False

class OptionForm(forms.Form):
    btn = forms.CharField()