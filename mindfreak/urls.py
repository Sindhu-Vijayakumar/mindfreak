from django.contrib import admin
from django.urls import path
from mindfreakapp.views import *
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', signin),
    path('signup/',signup),
    path('logout/',signout),
    path('contentpage/',contentpage),
    path('contentpage/<str:level>/',contentpage),
    path('addcontent/',addcontent),
    path('quizpage/',quizpage),
    path('quizpage/<str:level>/',quizpage),
    path('addquiz/',addquiz),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)