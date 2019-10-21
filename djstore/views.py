from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from .models import Product, Topproduct, Category, Banertop, Banerleft, Banerright
from .forms import *
from main.settings import *
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives, EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, ListView, View
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormMixin
from django.views.generic.detail import DetailView
from comments.forms import CommentForm
from django.utils import translation
from django.utils.translation import gettext_lazy as _


def reklama(request):
    return render(request, 'reklama_page.html')


class HomeView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['topproducts'] = Topproduct.objects.all()
        top = self.request.GET.get('q')
        if top:
            context['topproducts'] = Topproduct.objects.filter(
                Q(name__icontains=top) |
                Q(description__icontains=top)
            )
            if context['topproducts'].count() == 0:
                messages.warning(self.request, _(
                    'Axtardığınız mehsul mövcud deyil'), extra_tags='toroduct')
        cat = self.request.GET.get('cat')
        if cat:
            context['topproducts'] = Topproduct.objects.filter(
                Q(category__title__icontains=cat)
            )

            if context['topproducts'].count() == 0:
                messages.warning(self.request, _(
                    'Bu Kateqoriyada mehsul mövcud deyil'), extra_tags='toroduct')
        context['categories'] = Category.objects.all()
        context['top_banner'] = Banertop.objects.all()
        context['banner_left'] = Banerleft.objects.all()
        context['banner_right'] = Banerright.objects.all()
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = Product.objects.filter(is_active=True)
        cat = self.request.GET.get('cat')
        if cat:
            qs = self.request.GET.get('cat')

            qs = Product.objects.filter(
                Q(category__title__icontains=cat)

            )

        q = self.request.GET.get('q')
        if q:
            qs = Product.objects.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q)
            )
        if qs.count() == 0:
            messages.warning(self.request, _(
                'Axtardığınız məhsul mövcud deyil'), extra_tags='product')
        return qs




class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'createproduct.html'
    success_url = reverse_lazy('djstore:home')

    def form_valid(self, form):
        subject, from_email, to = 'DJ BAZAR', 'emka6451@gmail.com', 'emka6451@gmail.com'
        text_content = 'DJ BAZAR'
        html_content = '<h1>User mehsul elave edib.</h1><br><h4>Admin Panele Daxil olun</h4><h3><a href="http://localhost:8000/admin">Click</a></h3>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return super().form_valid(form)


class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'category-detail.html'

class ProductDetailView(DetailView, CreateView):
    model = Product
    template_name = 'description.html'
    context_object_name = 'product'
    form_class = CommentForm


    def get_success_url(self, **kwargs):
        return reverse_lazy('djstore:product-detail', kwargs={'pk':self.kwargs['pk']})


    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        comments = self.object.comments.all()
        context['comments'] = comments
        return context

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.product = get_object_or_404(Product, pk=self.kwargs['pk'])
        comment.save()
        return super().form_valid(form)


class TopProductDetailView(DetailView, CreateView):
    model = Topproduct
    template_name = 'description.html'
    context_object_name = 'product'
    form_class = CommentForm


    def get_success_url(self, **kwargs):
        return reverse_lazy('djstore:top-product-detail', kwargs={'pk':self.kwargs['pk']})


    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        comments = self.object.comments.all()
        context['comments'] = comments
        return context

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.topproduct = get_object_or_404(Topproduct, pk=self.kwargs['pk'])
        comment.save()
        return super().form_valid(form)

from django.http import HttpResponse


def contact_view(request):
    context = {}
    context['form'] = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = request.POST.get('name')
            contact_email = request.POST.get('email')
            contact_subject = request.POST.get('subject')
            contact_content = request.POST.get('message')

            subject = contact_subject
            from_email = settings.EMAIL_HOST_USER
            to = [settings.EMAIL_HOST_USER]

            ctx = {

                'name': contact_name,
                'email': contact_email,
                'subject': contact_subject,
                'content': contact_subject,

            }

            html_content = render_to_string('mail_template.html', ctx)  # render with dynamic value
            text_content = strip_tags(html_content)  # Strip the html tag. So people can see the pure text at least.

            msg_t = EmailMultiAlternatives(
                subject, text_content, from_email, [to])

            msg_t.attach_alternative(html_content, "text/html")

            msg_t.send()

            messages.success(request, _('Sizin mesajınız uğurla çatdırıldı. 24 saat ərzində E-poçt cavablanacağ!'))
            return redirect(reverse_lazy('djstore:contact'))
        else:
            context['form'] = form
        # return redirect('djstore:contact')
    return render(request, 'contact.html',context)
