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

from .models import Registration
class userregistrationform(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
    def clean_user_name(self):
        user_name=self.cleaned_data.get('user_name')
        if " " in user_name:
            raise forms.ValidationError("Name shouldnot contain space.")
        return user_name
    def clean(self):
        cleaned_data=super().clean()
        print(cleaned_data)
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("password and confirm password must be same!")
        return cleaned_data
    
from .models import Image
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title','image']        