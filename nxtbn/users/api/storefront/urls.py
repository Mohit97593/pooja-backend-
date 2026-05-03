from django.urls import path

from nxtbn.users.api.storefront.views import SignupView, LogoutView, LoginView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='customer_signup'),
    path('login/', LoginView.as_view(), name='customer_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
