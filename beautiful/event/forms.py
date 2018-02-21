from django import forms
from .models import Event, Tag


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag_name']



class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        title = forms.CharField(max_length=30, label='제목')
        place = forms.CharField(max_length=30, label='행사 장소')
        date = forms.DateField(label='행사 날짜')
        time = forms.TimeField(label='행사 시간')
        content = forms.CharField(label ='행사 설명')
        tag2 = forms.CharField(max_length=10, label ='행사 성격 태그')
