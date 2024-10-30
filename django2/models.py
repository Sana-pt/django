from django.db import models

# Create your models here.
class usermodel(models.Model):
    user_id=models.IntegerField(primary_key=True)
    user_name=models.CharField(max_length=200)
    user_age=models.IntegerField()
    date=models.DateField()

class bookmodel(models.Model):
    book_id=models.IntegerField(primary_key=True)
    book_title=models.CharField(max_length=100)
    book_author=models.CharField(max_length=100)
    published_date=models.DateField()
    isbn=models.CharField(max_length=13)

class productmodel(models.Model):
    p_name=models.CharField(max_length=500)
    p_description=models.TextField()
    p_price=models.DecimalField(max_digits=10,decimal_places=2)
    p_stock_quantity=models.IntegerField()
    p_created_at=models.DateTimeField(auto_now_add=True)

class customer1model(models.Model):
    first_name=models.CharField(max_length=500)
    last_name=models.CharField(max_length=500)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15)
    address=models.TextField()
    date_of_birth=models.DateField()

class blogmodel(models.Model):
    title=models.CharField(max_length=800)
    content=models.TextField()
    author=models.CharField(max_length=500)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class user1model(models.Model):
    u_id=models.IntegerField(primary_key=True)
    u_name=models.CharField(max_length=500)
    u_age=models.IntegerField()
    def __str__(self):
        return self.u_name
class productuser1model(models.Model):
    product_id=models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=500)
    usern=models.ForeignKey(user1model,on_delete=models.CASCADE)
  
class publishermodel(models.Model):
    pb_name=models.CharField(max_length=500)
    pb_address=models.CharField(max_length=500)
    pb_email=models.EmailField(unique=True)
    def __str__(self):
        return self.pb_name
class bookpbmodel(models.Model):
    bpb_title=models.CharField(max_length=500)
    bpb_publication_date=models.DateField()
    bpb_isbn=models.CharField(max_length=13,unique=True)
    bpb_publisher=models.ForeignKey(publishermodel,on_delete=models.CASCADE)
    def __str__(self):
        return self.bpb_title

class coursemodel(models.Model):
    course_name=models.CharField(max_length=500)
    course_code=models.CharField(max_length=200,unique=True)
    date=models.DateTimeField()
    def __str__(self):
        return self.course_name
class studentmodel(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15)
    course=models.ForeignKey(coursemodel,on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name
    
class Organizer(models.Model):
    name=models.CharField(max_length=100)
    contact_email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15)
    def __str__(self):
        return self.name
class Event(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField()
    location=models.CharField(max_length=300)
    organizer=models.ForeignKey(Organizer,on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock_quantity=models.IntegerField()
    def __str__(self):
        return self.name
    
class Hotel(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    rating=models.FloatField()
    description=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name
class Booking(models.Model):
    guest_name=models.CharField(max_length=100)
    check_in_date=models.DateField()
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name='bookings')
    def __str__(self):
        return self.guest_name
    
class formmodel(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    phone=models.CharField(max_length=15)

class UserProfile(models.Model):
    username=models.CharField(max_length=150,unique=True)
    date_of_birth=models.DateField()
    location=models.CharField(max_length=100)
    bio=models.TextField(null=True)
    
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
