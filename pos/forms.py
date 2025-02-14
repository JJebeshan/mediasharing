from django import forms
from .models import video

class upload_form(forms.ModelForm):
    class Meta:
        model = video
        fields=['video_name','description','file','thumbnail','user','category']