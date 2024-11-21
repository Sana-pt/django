"""
URL configuration for django1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django2 import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my',views.fun1),
    path('a',views.fun2),
    path('y',views.fun3),
    path('w',views.fun4),
    path('p',views.fun5),
    path('o',views.fun6),
    path('t',views.fun7),
    path('l',views.fun8),
    path('b',views.fun9),
    path('k',views.fun10),
    path('data',views.fun11),
    path('bmodel',views.fun12),
    path('bmodelt',views.fun13,name='my'),
    path('delete_book/<int:id>',views.delete,name='delete_book'),
    path('update_book/<int:id>',views.update,name='update_book'),
    path('pmodel',views.createf,name='prod'),
    path('redirect',views.create,name='re'),

    path('delete_cust/<int:pk>',views.deletecust,name='delete_cust'),
    path('update_cust/<int:pk>',views.updatecust,name='update_cust'),
    path('cmodel',views.createcust,name='create_cust'),
    path('redirectcust',views.cust,name='cust'),

    path('blogmodel',views.blogcreate,name='create_blog'),
    path('redirectblog',views.blog,name='blog'),
    
    path('upmodel',views.updisp,name='upmodel'),
    path('upmodelform',views.updispadd,name='upmodelform'),
     
    path('bpbmodeltable',views.bpbcreatef,name='publ'),
    path('bpbmodelform',views.bpbcreate),
    path('delete_publ/<int:id>',views.bpbcreatedlt,name='delete_publ'),
    path('update_publ/<int:id>',views.bpbcreateupdate,name='update_publ'),
    
    path('addstudent',views.addstudent),
    path('displayStudents',views.displayStudents,name='displayStudents'),
    path('displaySpecificStudent/<int:id>',views.displaySpecificStudent,name='dss'),
    path('updateStudent/<int:id>',views.updateStudent,name='updateStudent'),
    path('deleteStudent/<int:id>',views.deleteStudent,name='deleteStudent'),
    path('display_specific_course/<int:id>',views.specificCourse,name='dsc'),

    path('add_organizer',views.add_organizer,name='add_organizer'),
    path('add_event',views.add_event,name='add_event'),
    path('list_organizers',views.list_organizers,name='list_organizers'),
    path('list_events',views.list_events,name='list_events'),
    path('update_organizer/<int:id>/', views.update_organizer, name='update_organizer'),
    path('update_event/<int:id>/', views.update_event, name='update_event'),
    path('delete_organizer/<int:id>/', views.delete_organizer, name='delete_organizer'),
    path('delete_event/<int:id>/', views.delete_event, name='delete_event'),

    # path('add_product',views.add_product,name='add_product'),

    path('hotels/', views.hotel_list, name='hotel_list'),
    path('hotels/create/', views.create_hotel, name='create_hotel'),
    path('hotels/<int:hotel_id>/bookings/', views.hotel_bookings, name='hotel_bookings'),
    path('hotels/bookings/create/', views.create_booking, name='add_booking'),
    path('hotels/bookings/<int:hotel_id>/update/', views.update_booking, name='update_booking'),
    path('hotels/bookings/<int:hotel_id>/delete/', views.delete_booking, name='delete_booking'),
    path('hotels/high-rating/<str:min_rating>/', views.high_rating_hotels, name='high_rating_hotels'),

    path('fo',views.fun14),

    path('userprofile',views.manage_profile),

    path('img',views.login),

    path('blog',views.post_blog,name='post_blog'),
    path('addpost', views.add_post, name='add_post'),
    path('update/<int:pk>/',views.update_post, name='update_post'), 
    path('delete/<int:pk>/',views.delete_post, name='delete_post'),
    path('imgb',views.loginblog,name='loginblog'),

    path('form1',views.user),
    path('userimg1',views.disp_img),

    path('add_image',views.add_image),
    path('view_image',views.view_image),

   path('base',views.base),
   path('home',views.home), 
   path('about',views.about), 

   path('base1',views.base1),
   path('home1',views.home1), 
   path('about1',views.about1), 
   path('categories1',views.categories1),

   path('home3', views.home, name='home'),
   path('products', views.products, name='products'),
   path('profile', views.profile, name='profile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)