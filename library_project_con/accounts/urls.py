from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .decorators import user_authenticated
urlpatterns = [
    # the code below: if user is authenticated ,don't return login page.
    # user_authenticated is custom decorators.
    path('login/', (user_authenticated)(auth_views.LoginView.as_view(template_name='login.html')), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), {'next_page': 'index'}, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('change-password/', views.change_password, name="change_password"),

    path('profile/<str:username>', views.profile, name="profile"),
    path('favorite/<int:id>', views.favorite, name="favorite"),
    path('update-profile/', views.update_profile, name="update_profile"),
]
