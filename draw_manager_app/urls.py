from django.urls import path
from . import views

app_name = 'draw'
urlpatterns = [
    path('', views.Top_pageView.as_view(), name="top_page"),
    path('inquiry/',views.InquiryView.as_view(), name="inquiry"),
    path('draw_list/',views.DrawListView.as_view(), name="draw_list"),
    path('draw_detail/<int:pk>/',views.DrawDetailView.as_view(), name="draw_detail"),
    path('draw_create/', views.DrawCreateView.as_view(), name="draw_create"),
    path('draw_update/<int:pk>/', views.DrawUpdateView.as_view(), name="draw_update"),
    path('draw_delete/<int:pk>/', views.DrawDeleteView.as_view(), name="draw_delete"),
]