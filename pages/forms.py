from django import forms
from .models import ConversionHistory

class TempConversionForm(forms.Form):
    model = ConversionHistory
    amount = forms.FloatField(label='Amount', min_value=0)
    targetUnit = forms.ChoiceField(
        label='Target Unit',
        choices=[
            ('celsius', 'Celcius'),
            ('fahrenheit', 'Fahrenheit'),
            ('kelvin', 'Kelvin'),
        ])
    convertUnit = forms.ChoiceField(
        label='Convert Unit',
        choices=[
            ('celsius', 'Celcius'),
            ('fahrenheit', 'Fahrenheit'),
            ('kelvin', 'Kelvin'),
        ])
    category = forms.CharField(widget=forms.HiddenInput())
    fields = ['targetUnit','amount','convertUnit','category','result']

class WeightConversionForm(forms.Form):
    model = ConversionHistory
    amount = forms.FloatField(label='Amount', min_value=0)
    targetUnit = forms.ChoiceField(
        label='Target Unit',
        choices=[
            ('lbs', 'Pounds'),
            ('kg', 'Kilograms'),
            ('stone', 'Stone'),
        ])
    convertUnit = forms.ChoiceField(
        label='Convert Unit',
        choices=[
            ('lbs', 'Pounds'),
            ('kg', 'Kilograms'),
            ('stone', 'Stone'),
        ])
    category = forms.CharField(widget=forms.HiddenInput())
    fields = ['targetUnit','amount','convertUnit','category','result']

class VolumeConversionForm(forms.Form):
    model = ConversionHistory
    amount = forms.FloatField(label='Amount', min_value=0)
    targetUnit = forms.ChoiceField(
        label='Target Unit',
        choices=[
            ('gallon', 'Gallons'),
            ('liter', 'Liters'),
        ])
    convertUnit = forms.ChoiceField(
        label='Convert Unit',
        choices=[
            ('gallon', 'Gallons'),
            ('liter', 'Liters'),
        ])
    category = forms.CharField(widget=forms.HiddenInput())
    fields = ['targetUnit','amount','convertUnit','category','result']

class DistanceConversionForm(forms.Form):
    model = ConversionHistory
    amount = forms.FloatField(label='Amount', min_value=0)
    targetUnit = forms.ChoiceField(
        label='Target Unit',
        choices=[
            ('mile', 'Miles'),
            ('meter', 'Meters'),
            ('kilometer', 'Kilometers'),
            ('feet', 'Feet'),
            ('yard', 'Yards'),
        ])
    convertUnit = forms.ChoiceField(
        label='Convert Unit',
        choices=[
            ('mile', 'Miles'),
            ('meter', 'Meters'),
            ('kilometer', 'Kilometers'),
            ('feet', 'Feet'),
            ('yard', 'Yards'),
        ])
    category = forms.CharField(widget=forms.HiddenInput())
    fields = ['targetUnit','amount','convertUnit','category','result']