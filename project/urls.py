from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'project'

urlpatterns= [
	path('', views.Home.as_view(), name="home_view"),
	path('signup', views.Signup.as_view(), name="signup_view"),
	path('user-dashboard', views.UsersDashboard.as_view(), name="user-dashboard_view"),
	path('room-dashboard', views.RoomDashboard.as_view(), name="room-dashboard_view"),
	path('room-search', views.RoomSearch.as_view(), name="room-search_view"),
	path('room-reservation', views.RoomReservation.as_view(), name="room-reservation_view"),
	path('user-reservation', views.DisplayUserReservation.as_view(), name="user-reservation_view"),
	path('about', views.About.as_view(), name="about_view"),
	path('services', views.Services.as_view(), name="services_view"),
	path('gallery', views.Gallery.as_view(), name="gallery_view"),
	path('team', views.Team.as_view(), name="team_view"),
	path('contact', views.Contact.as_view(), name="contact_view"),
	path('login', views.LoginPage.as_view(), name="login_view"),
	path('home2', views.Home2.as_view(), name="home2_view"),
	path('updateuser', views.UpdateUser.as_view(), name="updateuser_view"),
	path('login-success', views.LoginSuccess.as_view(), name="loginsuccess_view"),
	path('login-failed', views.LoginFailed.as_view(), name="loginfailed_view"),	

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)