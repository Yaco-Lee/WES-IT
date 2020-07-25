import datetime
from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm
from dateutil.relativedelta import relativedelta


def home_view(request):
    form = PersonaForm()
    if request.method == "POST":
        form = PersonaForm(request.POST or None)
        if form.is_valid():
            Persona.objects.create(**form.cleaned_data)
            form = PersonaForm()
        else:
            print(form.errors)
    context = {"form": form}
    return render(request, "personas_home.html", context)


def list_view(request):
    fecha_ref_25 = datetime.datetime.now() - relativedelta(years=25)
    fecha_ref_35 = datetime.datetime.now() - relativedelta(years=35)
    personas_en_db = Persona.objects.filter(fecha_nac__lte=fecha_ref_25).filter(fecha_nac__gte=fecha_ref_35)
    context = {"personas": personas_en_db}
    return render(request, "personas_listado.html", context)





