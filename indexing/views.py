from django.shortcuts import render
from django.views.generic import ListView
import telebot
from indexing.forms import PostForm
from indexing.models import Meeting, Event, Profile, Trust, Deca1, Deca2


# Файл в котором хранится обработчик отвечающий за выдачу страниц и обработку форм

class Index(ListView):
    """ Просмотр главной страницы """
    template_name = 'index/index.html'
    models = Meeting, Event, Profile, Trust, Deca1, Deca2
    context_object_name = 'meeting'

    def get(self, request):
        meeting = Meeting.objects.all()
        event = Event.objects.all()
        profile = Profile.objects.all()
        trust = Trust.objects.all()
        deca1 = Deca1.objects.all()
        deca2 = Deca2.objects.all()
        return render(request, self.template_name, {'meeting': meeting,
                                                    'event': event,
                                                    'profile': profile,
                                                    'Trust': trust,
                                                    'Deca1': deca1,
                                                    'Deca2': deca2})

    def post(self, request):
        if request.method == 'POST':  # If the form has been submitted...
            form = PostForm(request.POST)  # A form bound to the POST data
            if form.is_valid():  # All validation rules pass
                # Process the data in form.cleaned_data
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                message = form.cleaned_data['message']

                text = """
                Приветствую вас, хозяин, я принес вам заявку:
                👤Ф.И.О: {}
                📪Почта: {}
                📱Телефон: {}
                📜Описание: {}
                """.format(name, email, phone, message)
                bot = telebot.TeleBot('2142701285:AAF_aneeUuXoR5fkH-tD9Fl1HmEZoYAXDO4')
                bot.send_message(chat_id=333613450, text=text)
        return render(request, self.template_name)
