from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Post, Comment  ,Story


class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=150, required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES, required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'email', 'password1', 'password2', 'bio', 'gender', 'profile_picture')




    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['name']
        user.bio = self.cleaned_data['bio']
        user.gender = self.cleaned_data['gender']
        
        if self.cleaned_data['profile_picture']:
            user.profile_picture = self.cleaned_data['profile_picture']
        
        if commit:
            user.save()
        return user


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'name', 'email', 'bio', 'gender', 'profile_picture']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'video', 'caption']
        widgets = {
            'caption': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a caption...'})
        }
    
    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        video = cleaned_data.get('video')
        
        
        if not image and not video:
            raise forms.ValidationError("Either image or video is required.")
        

        if image and video:
            if 'image' in self.files:
                cleaned_data['video'] = None
            else:
                cleaned_data['image'] = None
        
        return cleaned_data
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'placeholder': 'Add a comment...', 
                'class': 'w-full rounded p-1 text-black'
            })
        }
        
        
        
class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['image', 'video', 'caption']
        widgets = {
            'caption': forms.Textarea(attrs={
                'rows': 3, 
                'placeholder': 'Add a caption to your story...',
                'class': 'w-full p-2 bg-gray-700 rounded text-white'
            })
        }
    
    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        video = cleaned_data.get('video')
        
        if not image and not video:
            raise forms.ValidationError("Either image or video is required.")
        
        if image and video:
            raise forms.ValidationError("You can only upload either image or video, not both.")
        
        return cleaned_data
    
    
class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['image', 'video', 'caption']
        widgets = {
            'caption': forms.Textarea(attrs={
                'rows': 3, 
                'placeholder': 'Add a caption to your story...',
                'class': 'w-full p-2 bg-gray-700 rounded text-white'
            })
        }
    
    def clean(self):
        cleaned_data = super().clean()
        image = cleaned_data.get('image')
        video = cleaned_data.get('video')
        
        if not image and not video:
            raise forms.ValidationError("Either image or video is required.")
        
        if image and video:
            raise forms.ValidationError("You can only upload either image or video, not both.")
        
        return cleaned_data