from django import forms
from .models import Article, Racer, Book, Schedule

class SearchForm(forms.Form):
    keyword = forms.CharField(label='検索', max_length=100)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('content','user_name')

class RacerForm(forms.ModelForm):
    class Meta:
        model = Racer
        fields = ('__all__')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'link', 'image')

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ("__all__")