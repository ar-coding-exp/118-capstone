from django.shortcuts import render, redirect
from .forms import TempConversionForm
from .forms import WeightConversionForm
from .forms import VolumeConversionForm
from .forms import DistanceConversionForm
from .models import ConversionHistory

# Create your views here.

def home_view(request):
    history = ConversionHistory.objects.all() #get conversion history
    return render(request, 'pages/home.html', {'history': history})

def about_view(request):
    return render(request, 'pages/about.html')

#def temperature_view(request):
    #return render(request, 'pages/temperature.html')

def distance_view(request):
    return render(request, 'pages/distance.html')

def volume_view(request):
    return render(request, 'pages/volume.html')

def weight_view(request):
    return render(request, 'pages/weight.html')

def perform_temp_conversion(amount,targetUnit,convertUnit):
    if targetUnit == convertUnit:
        return amount

    converted_value = None
    if targetUnit == 'kelvin':
        if convertUnit == 'celsius':
            converted_value = amount - 273.15 #kel to cel
        elif convertUnit == 'fahrenheit':
            converted_value = (amount - 273.15) * 9/5 + 32 #kel to fah
    elif targetUnit == 'celsius':
        if convertUnit == 'kelvin':
            converted_value = amount + 273.15 #kel to cel
        elif convertUnit == 'fahrenheit':
            converted_value = (amount * 9/5) + 32 #kel to fah
    elif targetUnit == 'fahrenheit':
        if convertUnit == 'kelvin':
            converted_value = (amount - 32) * 5/9 + 273.15 #kel to cel
        elif convertUnit == 'celsius':
            converted_value = (amount - 32) * 5/9 #kel to fah
    return converted_value #return converted value

def perform_weight_conversion(amount,targetUnit,convertUnit):
    if targetUnit == convertUnit:
        return amount
    
    converted_value = None
    if targetUnit == 'lbs':
        if convertUnit == 'kg':
            converted_value = amount * 0.45359237
        elif convertUnit == 'stone':
            converted_value = amount / 14
    elif targetUnit == 'kg':
        if convertUnit == 'lbs':
            converted_value = amount / 0.45359237
        elif convertUnit == 'stone':
            converted_value = amount / 6.3502932
    elif targetUnit == 'stone':
        if convertUnit == 'lbs':
            converted_value = amount * 14
        elif convertUnit == 'kg':
            converted_value = amount * 6.35029318

    return converted_value

def perform_distance_conversion(amount,targetUnit,convertUnit):
    if targetUnit == convertUnit:
        return amount
    
    converted_value = None
    if targetUnit == 'mile':
        if convertUnit == 'kilometer':
            converted_value = amount * 1.609
        elif convertUnit == 'yard':
            converted_value = amount * 1760
        elif convertUnit == 'feet':
            converted_value = amount * 5280
        elif convertUnit == 'meter':
            converted_value = amount * 1609.34
    if targetUnit == 'kilometer':
        if convertUnit == 'mile':
            converted_value = amount / 1.609
        elif convertUnit == 'yard':
            converted_value = amount * 1094
        elif convertUnit == 'feet':
            converted_value = amount * 3280.84
        elif convertUnit == 'meter':
            converted_value = amount * 1000
    if targetUnit == 'yard':
        if convertUnit == 'kilometer':
            converted_value = amount / 1094
        elif convertUnit == 'mile':
            converted_value = amount / 1760
        elif convertUnit == 'feet':
            converted_value = amount * 3280.84
        elif convertUnit == 'meter':
            converted_value = amount * 0.9144
    if targetUnit == 'feet':
        if convertUnit == 'kilometer':
            converted_value = amount / 3280.84
        elif convertUnit == 'yard':
            converted_value = amount / 3
        elif convertUnit == 'mile':
            converted_value = amount / 5280
        elif convertUnit == 'meter':
            converted_value = amount * 0.3048
    if targetUnit == 'meter':
        if convertUnit == 'kilometer':
            converted_value = amount / 1000
        elif convertUnit == 'yard':
            converted_value = amount / 0.9144
        elif convertUnit == 'mile':
            converted_value = amount / 1609.34
        elif convertUnit == 'feet':
            converted_value = amount / 0.3048

    return converted_value

def perform_volume_conversion(amount,targetUnit,convertUnit):
    if targetUnit == convertUnit:
        return amount

    converted_value = None
    if targetUnit == 'gallon' and convertUnit == 'liter':
        converted_value = amount * 3.785
    if targetUnit == 'liter' and convertUnit == 'gallon':
        converted_value = amount / 3.785

    return converted_value


def temperature_view(request):
    form = TempConversionForm()
    converted_value = None
    category = "temperature"

    if request.method == 'POST':
        form = TempConversionForm(request.POST)
        if form.is_valid():
            print("form is valid") #check if code works
            #process conversion here
            amount = form.cleaned_data['amount']
            targetUnit = form.cleaned_data['targetUnit']
            convertUnit = form.cleaned_data['convertUnit']
            #category = form.cleaned_data['category']

            print(f"Amount: {amount}, Target Unit: {targetUnit}, Convert Unit: {convertUnit}, Category: {category}")

            #implement logic here
            converted_value = perform_temp_conversion(amount, targetUnit, convertUnit)

            #create instance
            conversion_record = ConversionHistory(
                amount = amount,
                targetUnit = targetUnit,
                convertUnit = convertUnit,
                category = category,
                result = converted_value 
            )
            conversion_record.save()
            #return redirect('temperature')
    else:
        print(form.errors) # log error
        form = TempConversionForm()

    form.fields['category'].initial = category
    history = ConversionHistory.objects.filter(category='temperature') #get conversion history
    return render(request, 'pages/temperature.html', {'form': form, 'history': history, 'converted_value':converted_value})

def weight_view(request):
    form = WeightConversionForm()
    converted_value = None
    category = "weight"

    if request.method == 'POST':
        form = WeightConversionForm(request.POST)
        if form.is_valid():
            print("form is valid") #check if code works
            #process conversion here
            amount = form.cleaned_data['amount']
            targetUnit = form.cleaned_data['targetUnit']
            convertUnit = form.cleaned_data['convertUnit']
            #category = form.cleaned_data['category']

            print(f"Amount: {amount}, Target Unit: {targetUnit}, Convert Unit: {convertUnit}, Category: {category}")

            #implement logic here
            converted_value = perform_weight_conversion(amount, targetUnit, convertUnit)

            #create instance
            conversion_record = ConversionHistory(
                amount = amount,
                targetUnit = targetUnit,
                convertUnit = convertUnit,
                category = category,
                result = converted_value 
            )
            conversion_record.save()

    else:
        print(form.errors) # log error
        form = WeightConversionForm()

    form.fields['category'].initial = category
    history = ConversionHistory.objects.filter(category='weight') #get conversion history
    return render(request, 'pages/weight.html', {'form': form, 'history': history, 'converted_value':converted_value})

def volume_view(request):
    form = VolumeConversionForm()
    converted_value = None
    category = "volume"

    if request.method == 'POST':
        form = VolumeConversionForm(request.POST)
        if form.is_valid():
            print("form is valid") #check if code works
            #process conversion here
            amount = form.cleaned_data['amount']
            targetUnit = form.cleaned_data['targetUnit']
            convertUnit = form.cleaned_data['convertUnit']
            #category = form.cleaned_data['category']

            print(f"Amount: {amount}, Target Unit: {targetUnit}, Convert Unit: {convertUnit}, Category: {category}")

            #implement logic here
            converted_value = perform_volume_conversion(amount, targetUnit, convertUnit)

            #create instance
            conversion_record = ConversionHistory(
                amount = amount,
                targetUnit = targetUnit,
                convertUnit = convertUnit,
                category = category,
                result = converted_value 
            )
            conversion_record.save()

    else:
        print(form.errors) # log error
        form = VolumeConversionForm()

    form.fields['category'].initial = category
    history = ConversionHistory.objects.filter(category='volume') #get conversion history
    return render(request, 'pages/volume.html', {'form': form, 'history': history, 'converted_value':converted_value})

def distance_view(request):
    form = VolumeConversionForm()
    converted_value = None
    category = "distance"

    if request.method == 'POST':
        form = DistanceConversionForm(request.POST)
        if form.is_valid():
            print("form is valid") #check if code works
            #process conversion here
            amount = form.cleaned_data['amount']
            targetUnit = form.cleaned_data['targetUnit']
            convertUnit = form.cleaned_data['convertUnit']
            #category = form.cleaned_data['category']

            print(f"Amount: {amount}, Target Unit: {targetUnit}, Convert Unit: {convertUnit}, Category: {category}")

            #implement logic here
            converted_value = perform_distance_conversion(amount, targetUnit, convertUnit)

            #create instance
            conversion_record = ConversionHistory(
                amount = amount,
                targetUnit = targetUnit,
                convertUnit = convertUnit,
                category = category,
                result = converted_value 
            )
            conversion_record.save()

    else:
        print(form.errors) # log error
        form = DistanceConversionForm()

    form.fields['category'].initial = category
    history = ConversionHistory.objects.filter(category='distance') #get conversion history
    return render(request, 'pages/distance.html', {'form': form, 'history': history, 'converted_value':converted_value})
