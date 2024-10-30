from django import forms
from .models import formmodel

class  userform(forms.ModelForm):
    class Meta:
        model = formmodel
        fields = '__all__'

from .models import UserProfile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
    
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content']
        