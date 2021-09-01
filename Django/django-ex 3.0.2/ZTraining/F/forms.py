from django import forms

class UserForm(forms.Form):
    realname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type' : "text", 
                'class':"form-control mb-2 mr-sm-2", 
                'id':"inlineFormInputName2", 
                'placeholder':"Имя"}), 
        max_length = 24)

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'type' : "text", 
                'class':"form-control", 
                'id':"inlineFormInputName2", 
                'placeholder':"Никнейм"}), 
        max_length = 12)
    # тут можно указывать аттрибуты, можно вставить классы бутстрапа