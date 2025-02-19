from django import forms
from app.models import *


def check_for_q(data):
    if 'q' in data.lower():
        raise forms.ValidationError('the given input is starts with q😎😎😎😎😎')
    

def check_for_len(value):
    if len(value)<=3:
        raise forms.ValidationError('the length of giveen data is lessthan 3 🫢🫢🫢🫢🫢 ')

class TopicForm(forms.Form):
    tname=forms.CharField(validators=[check_for_q,check_for_len])
    





class WebpageForm(forms.Form):
    tname=forms.ModelChoiceField(queryset=Topic.objects.all())
    wname=forms.CharField(validators=[check_for_q,check_for_len])
    url=forms.URLField()
    email=forms.EmailField()
    re_email=forms.EmailField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)#hidden filed it is used to cstch the bots ...it shouldnot show in fe and but should be visible in sourse code


    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot has beed catched')

    def clean(self):
        em=self.cleaned_data['email']
        re_em=self.cleaned_data['re_email']

        if em!=re_em:
            raise forms.ValidationError('email doesnot matched')