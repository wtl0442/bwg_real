from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'hashtag', 'file', 'photo',]
        widgets = {
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].required = False
        self.fields['photo'].required = False


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

# class UploadFileForm(forms.ModelForm):
# 	class Meta:
# 		model = UploadFile
# 		fields = '__all__'

# 	def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.fields['file'].required = False
# file 값이 없더라도 view에서 유효성 검사에서 오류를 발생시키지 않도록 해준다.
