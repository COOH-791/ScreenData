from django.conf.urls import url
from .views import IndexView, ApiImpView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r"^api$", ApiImpView.as_view(), name="importance"),
]
