from django.forms import ModelForm
from django.db import models
from django import forms
from datetime import *
from Registration.models import *
# from django.utils.translation import gettext_lazy as _

from django.utils import timezone


class DateInput(forms.DateInput):
    input_type = 'date'
class Userform(ModelForm):
    class Meta:
        model=udtl


        fields=['name','tel','email','username','password',
                ]
        def clean(self):
            cleaned_data = super().clean()  # mandatory

            username = cleaned_data.get("username")
            password = cleaned_data.get("password")

class Userlform(ModelForm):
    class Meta:
        model=udtl


        fields=['username','password',
                ]

class Entryccddform(ModelForm):
    # sdate=forms.CharField()
    # edate=forms.CharField()

    class Meta:
        model=Entry


        #
        # widgets = {
        #     'sdate': DateInput(),
        #     'edate': DateInput(),
        # }
        fields = ['category' ]



class Essentialform(ModelForm):
    class Meta:
        model=Essential
        fields=['category',]

        def clean(self):
            cleaned_data = super().clean()
            # id = cleaned_data.get("cat_id")
            category = cleaned_data.get("category")
            # print("cat:",category)

            # if id <= 0:
            #     msg = "Pls enter a valid id"
            #     self.add_error("id", msg)



class Accountform(ModelForm):
    class Meta:
        model=Account
        fields=['paymode','user']



        # def clean(self):
        #     cleaned_data = super().clean()  # mandatory
        #
        #     price = cleaned_data.get("prod_price")
        #     qty = cleaned_data.get("prod_qty")
        #
        #     if price < 10:
        #         msg = "Pls enter a valid price"
        #         self.add_error("price", msg)
        #     if qty < 10:
        #         msg = "Pls enter a quantity"
        #         self.add_error("qty", msg)

# class Registrationform(ModelForm):
#     class Meta:
#         model=Registration
#         fields=['uid']


class Entryform(ModelForm):

    class Meta:
        model=Entry

        fields=['username','paymode','category','amount','dfield']
        widgets = {
            'dfield': DateInput(),
        }