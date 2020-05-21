from django.shortcuts import  *
from Registration.models import *
from django.views.generic import *
from Registration.forms import *
# from django.shortcuts import  *
from django import forms
from datetime import *
from django.db.models import *
# from django.http import HttpResponse, HttpResponseNotFound
from django.db.models.functions import *
from plotly.offline import plot
import plotly.graph_objs as go
class Usercr(TemplateView):
    form_class=Userform

    model_name=udtl

    template_name = "Registration/Usercr.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        # context["stu"]="aa"
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            isActive=1
            # acdate=datetime.date.today()


            # Registration.save()
            form.save()

            return redirect("User_l")
        else:
            return render(request, self.template_name,{"form":form})


class Userl(TemplateView):
    form_class=Userlform

    model_name=udtl

    template_name = "Registration/usercr.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        # context["stu"]="aa"
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            qs=udtl.objects.get(username=username)
            if((qs.username==username)&(qs.password==password)):
                request.session['username']=username
                return redirect("Entry_v")
                # return HttpResponseNotFound('<h1>Page not found</h1>')
            else:
                return redirect("User_l")
                # return HttpResponse('<h1>Page was not found</h1>')

        else:
            return render(request, self.template_name,{"form":form})
class Entrycr(TemplateView):
    form_class=Entryform

    model_name=Entry

    template_name = "Registration/entrycr.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        # context["stu"]="aa"
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Entry_v")
        else:
            return render(request, self.template_name,{"form":form})


class Entryv(TemplateView):
    model_name=Entry
    template_name = "Registration/entryv.html"
    def get_queryset(self):
        return self.model_name.objects.all()
    def get(self, request, *args, **kwargs):
        context={}
        context["entry"]=self.get_queryset()
        return render(request,self.template_name,context)




class Essentialcr(TemplateView):
    form_class=Essentialform

    model_name=Essential

    template_name = "Registration/essentialcr.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        # context["stu"]="aa"
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Essential_v")
        else:
            return render(request, self.template_name,{"form":form})


class Essentialv(TemplateView):
    model_name=Essential
    template_name = "Registration/essentialv.html"
    def get_queryset(self):
        return self.model_name.objects.all()
    def get(self, request, *args, **kwargs):
        context={}
        context["essential"]=self.get_queryset()
        return render(request,self.template_name,context)
class Accountcr(TemplateView):
    form_class=Accountform

    model_name=Account

    template_name = "Registration/accountcr.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        # context["stu"]="aa"
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Account_v")
        else:
            return render(request, self.template_name,{"form":form})


class Accountv(TemplateView):
    model_name=Account
    template_name = "Registration/accountv.html"
    def get_queryset(self):
        return self.model_name.objects.all()
    def get(self, request, *args, **kwargs):
        context={}
        context["account"]=self.get_queryset()
        return render(request,self.template_name,context)

class Entryccdd(TemplateView):
    form_class=Entryccddform

    model_name=Entry

    template_name = "Registration/accountcr.html"
    template_name1 = "Registration/entryccddo.html"
    def get(self,request,*args,**kwargs):
        context={}
        context["form"]=self.form_class
        # context["stu"]="aa"
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            category=form.cleaned_data["category"]
            # sdate= form.cleaned_data["sdate"]
            # edate=form.cleaned_data["edate"]
            # qs="aa"

            qs =Entry.objects.filter(category__category=category).values('category__category') \
                    .annotate(total=Sum('amount'))
            # qs=Entry.objects.filter(Q(dfield__gte=sdate)&Q(dfield__lte=edate)&Q(category__category="Travel")).aggregate(Sum('amount')).get('amount__sum')

            # fig = go.Figure()
            # scatter = go.Scatter(x=[i.category__category for i in qs],
            #                      y = [a.amount for a in qs],
            #                      mode='lines', name='test',
            #                      opacity=0.8, marker_color='green')
            # fig.add_trace(scatter)
            # plt_div = plot(fig, output_type='div')
            # colors = ['lightslategray', ] * 5
            # colors[1] = 'crimson'
            #
            # fig = go.Figure(data=[go.Bar(
            #     x=[i.category__category for i in qs],
            #     y = [a.amount for a in qs],
            #     # x=['Feature A', 'Feature B', 'Feature C',
            #     #    'Feature D', 'Feature E'],
            #     # y=[20, 14, 23, 25, 22],
            #     marker_color=colors  # marker color can be a single color value or an iterable
            # )])
            # fig.update_layout(title_text='Least Used Feature')
            # def index(request):
            x_data = [i.category__category for i in qs],
            y_data = [a.amount for a in qs],
            plot_div = plot([Scatter(x=x_data, y=y_data,
                                     mode='lines', name='test',
                                     opacity=0.8, marker_color='green')],
                            output_type='div')
            # return render(request, "index.html", context={'plot_div': plot_div})

            context = {}
            context["qs"] = qs
            return render(request, self.template_name1, context={'plot_div': plot_div})





