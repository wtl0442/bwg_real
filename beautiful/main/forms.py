from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'content', 'hashtag', 'file', 'photo',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].required = False
        self.fields['photo'].required = False

# def clean_tag(self):
# 	tag_name = self.cleaned_data.get('tag')
# 	if tag_name is not None:
# 		try:
# 			tag = Tag.objects.get(name=tag_name)
# 		except Tag.DoesNotExist:
# 			tag = Tag.objects.create(name=tag_name)
# 	else:
# 		tag = None

# 	return tag

# def save(self, commit=True):
# 	instance = super().save(commit=False)
# 	if commit:
# 		instance.save()
# 		tag = self.cleaned_data.get('tag')
# 		if tag:
# 			instance.tag.add(tag)

# 	return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'content']

# class UploadFileForm(forms.ModelForm):
# 	class Meta:
# 		model = UploadFile
# 		fields = '__all__'

# 	def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.fields['file'].required = False 
# file 값이 없더라도 view에서 유효성 검사에서 오류를 발생시키지 않도록 해준다.
