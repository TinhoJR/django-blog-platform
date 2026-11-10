from django import forms
from . models import MarketList


class MarketListForm(forms.ModelForm):

    class Meta:
        model = MarketList
        fields = ["item","qty","price"]