from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(
        max_length=55,
        widget=forms.TextInput(attrs={
            "size": "40",
            "class": "wpcf7-form-control wpcf7-text wpcf7-validates-as-required",
            "placeholder": "Name *"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "size": "40",
                "class": "wpcf7-form-control wpcf7-text wpcf7-email",
                "placeholder": "Email"
            })
        )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "size": "40",
                "class": "wpcf7-form-control wpcf7-text wpcf7-phone",
                "placeholder": "Phone *"
            })
        )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "cols": "40",
                "rows": "10,",
                "class": "wpcf7-form-control wpcf7-textarea",
                "placeholder": "Message"
            })
        )
