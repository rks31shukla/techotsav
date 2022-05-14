from django.urls import path
from . import views
urlpatterns = [
    path('regb/',views.formbasic,name='registerbasic'),
    path('rega/',views.formadvance,name='registeradvance'),
    path('regg/',views.formgaming,name='registergaming'),
    path('regp/',views.formproject,name='registerproject'),
    path('submit/',views.submit,name='submit')
]
