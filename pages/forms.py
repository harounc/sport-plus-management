from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(label="Nom *", max_length=150, error_messages={"required": "Le nom est requis."})
    email = forms.EmailField(label="E-mail *", error_messages={"required": "L’e-mail est requis.", "invalid": "Format d’e-mail invalide."})
    sujet = forms.CharField(label="Sujet", max_length=200, required=False)
    message = forms.CharField(label="Message *", widget=forms.Textarea(attrs={"rows": 5}), error_messages={"required": "Le message est requis."})
    website = forms.CharField(required=False, widget=forms.HiddenInput)
    def clean_website(self):
        value = self.cleaned_data.get("website")
        if value: raise forms.ValidationError("Envoi indésirable détecté.")
        return value
