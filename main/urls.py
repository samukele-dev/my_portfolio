from django.urls import path, register_converter
from . import views
from .converters import SlugsConverter

register_converter(SlugsConverter, 'slugs')



app_name = "main"

urlpatterns= [
    path('', views.IndexView.as_view(), name="home"),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
    path('portfolio/<slugs:slug>/', views.PortfolioDetailView.as_view(), name="portfolio"),
]