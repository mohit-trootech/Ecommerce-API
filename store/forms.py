from django import forms
from django_ui_forms.forms import TailwindBaseUiForms
from utils.constants import FormLabel
from utils.utils import get_choices


class CreateProductForm(TailwindBaseUiForms, forms.Form):
    title = forms.CharField(
        max_length=64, widget=forms.TextInput(), label=FormLabel.TITLE.value
    )
    description = forms.CharField(
        widget=forms.Textarea(), label=FormLabel.DESCRIPTION.value
    )
    price = forms.FloatField(
        label=FormLabel.PRICE.value, widget=forms.NumberInput(attrs={"steps": "0.01"})
    )
    stock = forms.IntegerField(label=FormLabel.STOCK.value, widget=forms.NumberInput())
    category = forms.ChoiceField(
        choices=(), label=FormLabel.CATEGORY.value, widget=forms.Select()
    )
    image_1 = forms.CharField(label=FormLabel.IMAGE_1.value, widget=forms.TextInput())
    image_2 = forms.CharField(label=FormLabel.IMAGE_2.value, widget=forms.TextInput())
    image_3 = forms.CharField(label=FormLabel.IMAGE_3.value, widget=forms.TextInput())
    image_4 = forms.CharField(label=FormLabel.IMAGE_4.value, widget=forms.TextInput())
