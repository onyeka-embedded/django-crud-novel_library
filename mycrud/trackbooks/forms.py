from django.forms import ModelForm
from .models import Novel

class NovelForm(ModelForm):
    class Meta:
        model = Novel
        fields = '__all__'