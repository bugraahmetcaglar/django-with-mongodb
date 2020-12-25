from django.conf.urls import url

from user.views import AccountLoginAPIView, AccountLogoutAPIView, AccountRegisterAPIView

urlpatterns = [
    url(r'^user/login$', AccountLoginAPIView.as_view(), name="user_login_api"),
    url(r'^user/login$', AccountRegisterAPIView.as_view(), name="user_register_api"),
    url(r'^user/logout$', AccountLogoutAPIView.as_view(), name="user_logout_api"),
]