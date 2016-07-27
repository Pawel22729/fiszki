from django.shortcuts import render_to_response, RequestContext, redirect, render
from django.db.models import Q
from textblob import TextBlob
from random import randint, sample
from .models import Words

def index(request):
    words = Words.objects.all().order_by('-id')
    output = []
    for word in words:
        output.append(u': '.join([word.word, word.trans]))
    return render_to_response('templates/index.html', {'data': output}, RequestContext(request))

def dodaj_slowo(request):
    if request.method == "GET":
        if 'add_word' in request.GET:
            if request.GET.get('slowo') != None and request.GET.get('slowo') != 'None':
                data = request.GET.get('slowo')
                if not Words.objects.filter(Q(word__contains=str(data)) | Q(trans__contains=str(data))):
                    try:
                        text = TextBlob(str(data))
                        translation = text.translate(from_lang='pl', to='es')
                        words = Words(word=text, trans=translation)
                        words.save()
                    except Exception as e:
                        exeption_text = 'Nie mozna przetlumaczyc:<br>'
                        return render_to_response('templates/add_word.html', {'err': e}, RequestContext(request))

                return redirect('index')
        elif 'del_word' in request.GET:
            if request.GET.get('slowo') != None and request.GET.get('slowo') != 'None':
                word_to_delete = request.GET.get('slowo')
                Words.objects.filter(Q(word__contains=str(word_to_delete)) | Q(trans__contains=str(word_to_delete))).delete()
                return redirect('index')

    return render_to_response('templates/add_word.html', RequestContext(request))

def nauka(request):
    selected_words = []
    all_words = []
    rand_words = []
    if request.method == "GET":
        if request.GET.get('losuj_ile'):
            how_much = int(request.GET.get('losuj_ile'))
            all_objects = list(Words.objects.all())
            for i in all_objects:
                all_words.append(i.id)
            if how_much > len(all_words):
                how_much = len(all_words)
            rand_words = sample(all_words, how_much)
        for i in rand_words:
            selected_words.append(Words.objects.filter(id=i)[0])

    return render_to_response('templates/nauka.html', {'wylosowane': selected_words}, RequestContext(request))

def zapisz_odp(reqest):
    if reqest.GET:
        answer = {}
        values = {'_can': 0, '_cant': 3, '_maybe': 1}
        for i in reqest.GET:
            word = Words.objects.filter(id=i)
            counter = word.values()[0]['counter']
            counter = int(counter) + values[reqest.GET[i]]
            word.update(counter=str(counter))
    return redirect('index')

def welcome(reqest):
    linki = {'Zapisane slowa': '/fiszki/', 'Admin page': '/admin/'}
    return render(reqest, 'templates/welcome.html', {'data': linki})