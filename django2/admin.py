from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(usermodel)

admin.site.register(bookmodel)

admin.site.register(productmodel)

class custadmin(admin.ModelAdmin):
    list_display=('first_name','last_name','address',)
    search_fields=('first_name',)
    list_filter=('first_name',)
admin.site.register(customer1model,custadmin)
admin.site.site_header="SANA'S SITE"

class blogadmin(admin.ModelAdmin):
    list_display=('title','author','created_at')
    search_fields=('title',)
    list_filter=('author','created_at',)
admin.site.register(blogmodel,blogadmin)
admin.site.site_header="Blog management site"

admin.site.register(user1model)
admin.site.register(productuser1model)

class bookadmin(admin.ModelAdmin):
    list_display=('bpb_title','bpb_isbn','bpb_publisher')
    search_fields=('bpb_title','bpb_isbn',)
    list_filter=('bpb_publication_date',)
admin.site.register(bookpbmodel,bookadmin)
admin.site.register(publishermodel)
admin.site.site_header="Book Publish"

admin.site.register(coursemodel)
admin.site.register(studentmodel)

admin.site.register(Organizer)
admin.site.register(Event)

admin.site.register(Product)
admin.site.register(Category)

class HotelAdmin(admin.ModelAdmin):
    list_display=('name','location','rating')
    search_fields=('name','location')
    list_filter=('rating',)
class BookingAdmin(admin.ModelAdmin):
    list_display=('guest_name','check_in_date','hotel')
    search_fields=('guest_name',)
    list_filter=('check_in_date',)
admin.site.register(Hotel,HotelAdmin)
admin.site.register(Booking,BookingAdmin)

admin.site.register(userimg)

admin.site.register(Image)