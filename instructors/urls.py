from django.conf.urls import url
from instructors import views


urlpatterns = [
    url(r'^register/$', views.InstructorRegister.as_view(),
        name='instructor_register',),
]
