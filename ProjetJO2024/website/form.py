from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User

class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fiedls = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Mot de passe'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Votre mot de passe ne doit pas être trop similaire à vos informations personnelles.</li><li>Votre mot de passe doit contenir au moins 8 caractères contenant des lettres, des chiffres et des @/./+/-/_ seulement.</li><li>Votre mot de passe ne doit pas être un mot de passe commun (ex: maman).</li></ul>'

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirmer le mot de passe'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Entrer le mot de passe précédent, pour vérification.</small></span>'

class UpdateUserForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adresse mail'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prénom'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom de famille'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nom utilisateur'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requis: votre nom utilisateur doit être votre nom de famille suivi de votre prénom.</small></span>'

       
class CustomUserCreationForm (UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adresse mail'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Prénom'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom de famille'}))
    #password1 = forms.CharField(
       #label ="Password",
       #strip=False,
       #widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
   #)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nom utilisateur'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requis: votre nom utilisateur doit être votre nom de famille suivi de votre prénom.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Mot de passe'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Votre mot de passe ne doit pas être trop similaire à vos informations personnelles.</li><li>Votre mot de passe doit contenir au moins 8 caractères contenant des lettres, des chiffres et des @/./+/-/_ seulement.</li><li>Votre mot de passe ne doit pas être un mot de passe commun (ex: maman).</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmer le mot de passe'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Entrer le mot de passe précédent, pour vérification.</small></span>'
#    password1 = forms.CharField(
       # label ="Password",
       # strip=False,
       # widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
   # )
   # password2 = forms.CharField(
       # label="Password confirmation",
       # widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
       # strip=False,
   # )

   # class Meta(UserCreationForm.Meta):
        #fields = UserCreationForm.Meta.fields + ("password1", "password2") 




