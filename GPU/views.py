# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Produto
def home(request):
    context = {
        'Produtos':Produto.objects.order_by("-price_boleto"),
        #'Produtos': Produto.objects.filter(nome__contains='Processador') 
        'Query':"",
        'Qsort':"",
    }


    return render(request, "home.html", context)


class HomeView(ListView):
    model = Produto
    template_name = 'home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Produtos'
    paginate_by = 30
    ordering = ["-price_boleto"]
    def get_context_data(self, *args, **kwargs): #Pega a query da search e procura

        context = super(HomeView, self).get_context_data(*args, **kwargs)
        if self.request.GET.get('searchPC' and 'sortPC'):
            qsort = self.request.GET.get('sortPC')
            query = self.request.GET.get('searchPC')
            context = { #Salve a query digitada pro user
                'Query':query,
                'Qsort':qsort,
            }
            if query == '':
                if qsort == 'Decrescente':
                    context['Produtos'] = Produto.objects.order_by("-price_boleto")
                elif qsort == 'Crescente':
                    context['Produtos'] = Produto.objects.order_by("price_boleto")
            else:
                q = query.split() #Quebra a query e define uma lista de pesquisa com append - Ex: [GTX, 1660]
                for teste in q:
                    if qsort == 'Decrescente':
                        context['Produtos'] = Produto.objects.filter(nome__icontains=teste).order_by("-price_boleto")
                    elif qsort == 'Crescente':
                        context['Produtos'] = Produto.objects.filter(nome__icontains=teste).order_by("price_boleto")
        return context

def about(request):

    return render(request, "about.html")