from django import forms

class ArticleHeader(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type' : "input", 
                'class':"form-control mb-2 mr-sm-2", 
                'id':"inlineFormInputName2", 
                'style' : "width: 600px;",
                'placeholder':"Название статьи",
            }
        ), 
        max_length = 200
    )

    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'type' : "file", 
                'class':"",
                'id':"inlineFormInputName2", 
                'placeholder':"Изображение"
            }
        )
    )

    preview_text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'type' : "text", 
                'class':"form-control", 
                'id':"inlineFormInputName2", 
                'placeholder':"Описание",
                'style' : "resize: none;",
                'cols':"180",
                'rows':"10",
            }
        ), 
        max_length = 1000,
    )

class Header(forms.Form):
    header = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type' : "input", 
                'class':"form-control mb-2 mr-sm-2", 
                'id':"inlineFormInputName2", 
                'style' : "width: 600px;",
                'placeholder':"Заголовок",
            }
        ), 
        max_length = 200
    )

class Paragraph(forms.Form):
    paragraph = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'type' : "text", 
                'class':"form-control mb-2 mr-sm-2", 
                'id':"inlineFormInputName2", 
                'style' : "resize: none;",
                'placeholder':"Абзац",
            }
        ), 
        max_length = 200
    )

class Image(forms.Form):
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'type' : "file", 
                'class':"",
                'id':"inlineFormInputName2", 
                'placeholder':"Изображение"
            }
        )
    )

class Quote(forms.Form):
    quote = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type' : "input", 
                'class':"form-control mb-2 mr-sm-2", 
                'id':"inlineFormInputName2", 
                'style' : "width: 1000px;",
                'placeholder':"Цитата",
            }
        ), 
        max_length = 200
    )