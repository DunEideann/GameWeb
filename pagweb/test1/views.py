import os
from django.shortcuts import render
from django.core.mail import send_mail
from .models import Info_Home
from .models import News
from .models import Developer_Team_Information
from .models import SoulAndSpirit
from .models import CoronaWars
from datetime import datetime, date, time
from .function import make_round_image, make_tall_image


# Create your views here.
def index(request):
    
    information_home = Info_Home.objects.all()
    spirits = SoulAndSpirit.objects.all()
    wars = CoronaWars.objects.all()
    dev_info = Developer_Team_Information.objects.all()
    all_news = News.objects.all()
    lista_imagenes = []
    for info in information_home:
        imagen = info.image_home
        lista_imagenes.append(imagen)

    # Configure the list to pass on to index.html
    news_lista = []
    for new in all_news:
        
        # do the timestamp thing
        fecha = new.news_auto_date
        año = fecha.year
        mes = fecha.month
        dia = fecha.day
        datestamp = date(año, mes, dia)
        date_dmy = datestamp.strftime("%A %d of %B, %Y")

        # add all the characteristics of the new to the list
        lista = [fecha.year, fecha.month, fecha.day, new.news_headline, new.news_body, new.news_image, date_dmy, new.news_image_big, new.news_title_big, new.news_subtitle_big, new.news_body_big]
        news_lista.append(lista)
    
    news_lista.sort(reverse=True)

    spirits = SoulAndSpirit.objects.all()
    wars = CoronaWars.objects.all()
    dev_info = Developer_Team_Information.objects.all()
    

    return render(request, "index.html", {'information_home': information_home, 'all_news': news_lista,
                                          'developers_data': dev_info, 'souls': spirits, 'coronas': wars, 'img': lista_imagenes})

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print("HOLA")
        print(f"Entre a esta wea con estos datos {name} {email} {subject} {message}")

        send_mail(
            email + ' ('+name+'): '+subject,
            message,
            email,
            [os.environ.get('company_mail')],
            fail_silently=False,
        )


    return render(request, 'index.html', {'name': name})