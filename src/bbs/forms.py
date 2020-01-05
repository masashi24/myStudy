from django import forms
from .models import Article, Racer

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