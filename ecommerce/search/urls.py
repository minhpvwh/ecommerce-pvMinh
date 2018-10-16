from django.conf.urls import url



from .views import (
    SearchProductView   ,
)


app_name="search"
urlpatterns = [

    #ss3
    url(r'^$', SearchProductView.as_view(),name='query'),

]
