from django import forms

class PostForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={'class' : "form-control" , 'aria-describedby' :"basic-addon1"}), max_length = 100) # с контектом приводим в представление, далее в шаблонизатор 
    # тут можно указывать аттрибуты, можно вставить классы бутстрапа