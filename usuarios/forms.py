""" from typing import Any
from django import forms


class appUsarioForm(forms.ModelForm):

    #widgets forms

    def clean_email(self):
        super().clean_email()

        self.username = self.email

        return self

    def save(self):

        self.username = self.email """
