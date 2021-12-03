from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logoutUser, name='logout'),
    path('assignments', assignments, name='assignments'),
    path('notes', notes, name='notes'),
    path('jounrals', journals, name='journals'),
    path('journal/<int:id>', journalView, name='journal'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
