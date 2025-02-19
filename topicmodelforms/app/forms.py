from django import forms
from app.models import *


#validators using normal functions

# def check_len(value):
#     if len(value)<=3:
#         raise forms.ValidationError('given value is too short')       



class TopicModelForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'


 

class WebpageModelForm(forms.ModelForm):
    re_email=forms.EmailField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)
    class Meta:
        model=Webpage
        fields='__all__'  
        # wname=check_len
        # exclude=['url']


    

    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('bot has been catched')

class AccessModelForm(forms.ModelForm):
    class Meta:
        model=Access_record
        fields='__all__'