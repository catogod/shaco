from django.urls import path
from . import views

urlpatterns =[
path("",views.Main_login),
path("RegisterNDLogin",views.RegisterNDLogin),
path("menu",views.Menu_handele),
path("user",views.User_handele),
path("shop",views.shop_handele),
path("top",views.Top_page_handele),
path("log_out",views.Log_out),
path("trivia",views.Trivia_handele),
path("admin",views.admin_handele),
path("admin_RNL",views.admin_RNL_handele),
path("log_out_admin",views.Log_out_admin),
path("rrr",views.rulate),#testing
]