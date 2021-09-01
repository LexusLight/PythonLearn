from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,HttpResponsePermanentRedirect, HttpRequest
from .forms import ArticleHeader,Header,Quote,Image,Paragraph
from .models import Article,Paragraph,Header,Quote,Image
from django.conf import settings
from django.core.files.storage import FileSystemStorage #В конфигурации добавили кое что
from django.template.defaulttags import register


PICTURE_URL = "media/images/article_img/"

@register.filter #добавляем фильтр для шаблонизатора
def get_range(value):
    return list(range(value))

def article_list(request):
    articles = Article.objects.all()
    template = "article_list.html"
    context = {
        "articles" : articles,
        "MEDIA_URL": settings.MEDIA_URL,
    }
    return render(request, template, context)
    
def article_detail(request,id):
    article = Article.objects.get(id=id)
    headers = Header.objects.filter(id_article = id)
    paragraphs = Paragraph.objects.filter(id_article = id)
    images = Image.objects.filter(id_article = id)
    quotes = Quote.objects.filter(id_article = id)

    template = "article_detail.html"
    context = {
        "article"   : article,
        "headers"    : headers,
        "paragraphs" : paragraphs,
        "images"     : images,
        "quotes"     : quotes,
        "MEDIA_URL" : settings.MEDIA_URL,
    }
    return render(request, template, context)

##################

def render_form(request):
    case = 0
    position = 0
    try:   
        case = int(request.GET.get("upload"))
        position = int(request.GET.get("position"))

        if(case == 1):
            form = Header()
            position = position + 1
            template = "form_add.html"
        elif(case == 2):
            form = Paragraph()
            position = position + 1
            template = "form_add.html"
        elif(case == 3):
            form = Image()
            position = position + 1
            template = "form_add.html"
        elif(case == 4):
            form = Quote()
            position = position + 1
            template = "form_add.html"
        else:
            form = ArticleHeader()
            template = "form.html"           

    except:
        form = ArticleHeader()
        template = "form.html"
    
    context = {
        "form" : form,
        "case" : case,
        "position" : position,
    }   
    return render(request, template, context)

# def exit(request):

#     resp = HttpResponsePermanentRedirect('/C')
#     # resp.set_cookie('x',2)
#     del request.session['x']
#     request.session['x'] = 2
#     del request.session['username']
#     return resp

def post(request):   

    title = request.POST.get("title") #Название статьи
    preview_text = request.POST.get("preview_text") #Описание статьи

    image = request.FILES['image'] #Главное изображение. Просто жуть, достаём через реквест файл
    fs = FileSystemStorage(PICTURE_URL)
    filename = fs.save(image.name, image) #Сохраняем файл и берём линк
    # image_url = fs.url(filename)

    article = Article()
    article.preview_image = "images/article_img/" + filename
    article.title = title
    article.preview_text = preview_text
    article.save()
    article.parts = 1

    for index in range(20):

        if(str(index) + ".header" in request.POST):
            text = request.POST.get(str(index) + ".header")
            header = Header()
            header.id_article = article
            header.text = text
            header.position = index
            header.save()
            article.parts = article.parts + 1
            

        if(str(index) + ".paragraph" in request.POST):
            text = request.POST.get(str(index) + ".paragraph")
            paragraph = Paragraph()
            paragraph.id_article = article
            paragraph.text = text
            paragraph.position = index
            paragraph.save()
            article.parts = article.parts + 1

        if(str(index) + ".quote" in request.POST):
            text = request.POST.get(str(index) + ".quote")
            quote = Quote()
            quote.id_article = article
            quote.quote = text
            quote.position = index
            quote.save()
            article.parts = article.parts + 1

        if(str(index) + ".image" in request.FILES):
            img = request.FILES[str(index) + ".image"]
            fs = FileSystemStorage(PICTURE_URL)
            filename = fs.save(img.name, img) 
            #image_url = fs.url(filename)
            
            image = Image()
            image.image = "images/article_img/" + filename
            image.id_article = article
            image.position = index
            image.save()
            article.parts = article.parts + 1

    article.save()
    return HttpResponseRedirect('/D/')







    # user = User(username = form.cleaned_data['username'],realname = form.cleaned_data['realname'])
    # user.save()
    

