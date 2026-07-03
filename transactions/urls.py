from django.urls import path
from. import views
urlpatterns = [
    path('view/',views.TrasactionAPIView.as_view()),
    path('add/',views.AddTransactionAPIView.as_view()),
    path('delete/<int:id>/',views.DeleteTransactionAPIView.as_view()),
    path('update/<int:id>/', views.UpdateTransactionAPIView.as_view()),
    path('view-single/<int:id>/', views.SingleTransactionAPIView.as_view()),
]
