from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def fun1(request):
    return HttpResponse("Hi")
def fun2(request):
    return HttpResponse('<h1>Good morning</h1>\n<h2>Hello world</h2>')
def fun3(request):
    return HttpResponse("HELLO WORLD")
def fun4(request):
    return render(request,"hi.html")
def fun5(request):
    return render(request,"2.html",{"name":"anu"})
def fun6(request):
    context={
        'fruits':['apple','banana','cherry'],
    }
    return render(request,"fruits.html",context)
def fun7(request):
    items=[
        {'Name':'laptop','Price':'200','Quantity':'12'},
        {'Name':'phone','Price':'500','Quantity':'5'},
        {'Name':'tv','Price':'400','Quantity':'10'},
    ]
    return render(request,"item.html",{'item':items})
def fun8(request):
    product_list=[
        {'Name':'Laptop','Price':'$999.99','Stock':'In stock'},
        {'Name':'Smartphone','Price':'$599.99','Stock':'Out of stock'},
        {'Name':'Tablet','Price':'$299.99','Stock':'In stock'},
        {'Name':'Headphones','Price':'$149.99','Stock':'In stock'},
    ]
    return render(request,"product_list.html",{'product_list':product_list})
def fun9(request):
    data=usermodel.objects.all()
    return render(request,"all.html",{'data1':data})
def fun10(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        age=request.POST.get('age')
        date=request.POST.get('date')
        user_obj=usermodel()
        user_obj.user_id=id
        user_obj.user_name=name
        user_obj.user_age=age
        user_obj.date=date
        user_obj.save()
    return render(request,"add_user.html")

def fun11(request):
    data=bookmodel.objects.all()
    return render(request,"book_model.html",{'data1':data})

def fun12(request):
    if request.method == "POST":
        id=request.POST.get('id')
        title=request.POST.get('title')
        author=request.POST.get('author')
        published_date=request.POST.get('published_date')
        isbn=request.POST.get('isbn')
        user_obj=bookmodel()
        user_obj.book_id=id
        user_obj.book_title=title
        user_obj.book_author=author
        user_obj.published_date=published_date
        user_obj.isbn=isbn
        user_obj.save()
        return redirect('my')
    return render(request,"book_model.html")
def fun13(request):
    data=bookmodel.objects.all()
    return render(request,"bmodel_table.html",{'data1':data})

def delete(request,id):
    book=bookmodel.objects.get(book_id=id)
    book.delete()
    return redirect('my')
def update(request,id):
    book=bookmodel.objects.filter(book_id=id)
    if request.method == "POST":
        ID=request.POST.get('id')
        title=request.POST.get('title')
        author=request.POST.get('author')
        published_date=request.POST.get('published_date')
        isbn=request.POST.get('isbn')
        user_obj=bookmodel()
        user_obj.book_id=id
        user_obj.book_title=title
        user_obj.book_author=author
        user_obj.published_date=published_date
        user_obj.isbn=isbn
        user_obj.save()
        return redirect('my')
    return render(request,"update.html",{'updatekey':book})

def create(request):
    if request.method == "POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        price=request.POST.get('price')
        stock_quantity=request.POST.get('stock_quantity')
        created_at=request.POST.get('created_at')
        product=productmodel()
        product.p_name=name
        product.p_description=description
        product.p_price=price
        product.p_stock_quantity=stock_quantity
        product.p_created_at=created_at
        product.save()
        return redirect('prod')
    return render(request,"product_model.html")
def createf(request):
    products=productmodel.objects.all()
    return render(request,"productmodel_table.html",{'product1':products})

def createcust(request):
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        address=request.POST.get('address')
        date_of_birth=request.POST.get('date_of_birth')
        customer=customer1model()
        customer.first_name=first_name
        customer.last_name=last_name
        customer.email=email
        customer.phone_number=phone_number
        customer.address=address
        customer.date_of_birth=date_of_birth
        customer.save()
        return redirect('cust')
    return render(request,"customer_model.html")
def cust(request):
    customers=customer1model.objects.all()
    return render(request,"customermmodel_table.html",{'cust1':customers})
def deletecust(request,pk):
    cust=customer1model.objects.get(pk=pk)
    cust.delete()
    return redirect('cust')
def updatecust(request,pk):
    cust=customer1model.objects.get(pk=pk)
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        address=request.POST.get('address')
        date_of_birth=request.POST.get('date_of_birth')
        cust.first_name=first_name
        cust.last_name=last_name
        cust.email=email
        cust.phone_number=phone_number
        cust.address=address
        cust.date_of_birth=date_of_birth
        cust.save()
        return redirect('cust')
    return render(request,"cust_model_update.html",{'updatekey':cust})

def blogcreate(request):
    if request.method == "POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        author=request.POST.get('author')
        created_at=request.POST.get('created_at')
        updated_at=request.POST.get('updated_at')
        blog=blogmodel()
        blog.title=title
        blog.content=content
        blog.author=author
        blog.created_at=created_at
        blog.updated_at=updated_at
        blog.save()
        return redirect('blog')
    return render(request,"blog_model.html")
def blog(request):
    blogs=blogmodel.objects.all()
    return render(request,"blogmodel_table.html",{'blog1':blogs})

def updisp(request):
    up=productuser1model.objects.all()
    return render(request,"productuser1model_table.html",{'up1':up})
def updispadd(request):
    udata=user1model.objects.all()
    if request.method == "POST":
        u_id=request.POST.get('u_id')
        prname=request.POST.get('prname')
        uadd=productuser1model()
        uadd.product_id=u_id
        uadd.product_name=prname
        uadd.usern=user1model.objects.get(u_id=request.POST.get('u_id'))
        uadd.save()
        return redirect('upmodel')
    return render(request,"productuser1model_form.html",{'udata1':udata})

        
def bpbcreate(request):
    pub=publishermodel.objects.all()
    if request.method == "POST":
        title=request.POST.get('title')
        publication_date=request.POST.get('publication_date')
        isbn=request.POST.get('isbn')
        publish=bookpbmodel()
        publish.bpb_title=title
        publish.bpb_publication_date=publication_date
        publish.bpb_isbn=isbn
        publish.bpb_publisher=publishermodel.objects.get(id=request.POST.get('pubf'))
        publish.save()  
        return redirect('publ')
    return render(request,"bookpb_form.html",{'pubb':pub})
def bpbcreatef(request):
    publishes=bookpbmodel.objects.all()
    return render(request,"bppublisher_table.html",{'publishes1':publishes})
def bpbcreatedlt(request,id):
    publishes=bookpbmodel.objects.get(id=id)
    publishes.delete()
    return redirect('publ')
def bpbcreateupdate(request,id):
    pb=publishermodel.objects.all()
    publishes=bookpbmodel.objects.get(id=id)
    if request.method == "POST":
        title=request.POST.get('title')
        publication_date=request.POST.get('publication_date')
        isbn=request.POST.get('isbn')
        publishes.bpb_title=title
        publishes.bpb_publication_date=publication_date
        publishes.bpb_isbn=isbn
        publishes.bpb_publisher=publishermodel.objects.get(id=request.POST.get('id'))
        publishes.save() 
        return redirect('publ')
    return render(request,"bookpb_update.html",{'updatekey1':publishes,'upd':pb,})

def addstudent(request):
    data=coursemodel.objects.all()
    if request.method == "POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        obj=studentmodel()
        obj.first_name=first_name
        obj.last_name=last_name
        obj.email=email
        obj.phone_number=phone_number
        obj.course=coursemodel.objects.get(id=request.POST.get('course'))
        obj.save()
        return redirect('displayStudents')
    return render(request,'add_student.html',{'data':data})
def displayStudents(request):
    display=studentmodel.objects.all()
    return render(request,'display_students.html',{'disp':display})
def displaySpecificStudent(request,id):
    data=studentmodel.objects.get(id=id)
    return render(request,'display_specific_student.html',{'specific':data})
def updateStudent(request,id):
    data=studentmodel.objects.get(id=id)
    dataa=coursemodel.objects.all()
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        data.first_name=first_name
        data.last_name=last_name
        data.email=email
        data.phone_number=phone_number
        data.course=coursemodel.objects.get(id=request.POST.get('course'))
        data.save()
        return redirect('displayStudents')
    return render(request,'update_student.html',{'data':data,'dataa':dataa})
def deleteStudent(request,id):
    dele=studentmodel.objects.get(id=id)
    dele.delete()
    return redirect('displayStudents')
def specificCourse(request,id):
    c=coursemodel.objects.get(id=id)
    data=studentmodel.objects.filter(course=c)
    return render(request,'display_specific_course.html',{'dataa':data,'cc':c})

def add_organizer(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        contact_email=request.POST.get('contact_email')
        phone_number=request.POST.get('phone_number')
        Organizer.objects.create(name=name,contact_email=contact_email,phone_number=phone_number)
        return redirect('list_organizers')
    return render(request,'add_organizer.html')
def add_event(request):
    organizers=Organizer.objects.all()
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        location=request.POST.get('location')
        organizer_id=request.POST.get('organizer')
        organizer=Organizer.objects.get(id=organizer_id)
        Event.objects.create(title=title,date=date,location=location,organizer=organizer)
        return redirect('list_events')
    return render(request,'add_event.html',{'organizers':organizers})
def list_organizers(request):
    organizers=Organizer.objects.all()
    return render(request,'list_organizers.html',{'organizers':organizers})
from django.db.models import Q
def list_events(request):
    events=Event.objects.all()
    if request.method == "POST":
        value=request.POST.get('search')
        srch=Event.objects.filter(Q(title__icontains=value))
        return render(request,'list_events.html',{'events':srch})
    return render(request,'list_events.html',{'events':events})
def update_organizer(request, id):
    organizer=Organizer.objects.get(id=id)
    if request.method == 'POST':
        organizer.name=request.POST.get('name')
        organizer.contact_email=request.POST.get('contact_email')
        organizer.phone_number=request.POST.get('phone_number')
        organizer.save()
        return redirect('list_organizers')
    return render(request,'update_organizer.html',{'organizer':organizer})
def update_event(request, id):
    event=Event.objects.get(id=id)
    organizers=Organizer.objects.all()
    if request.method == 'POST':
        event.title=request.POST.get('title')
        event.date=request.POST.get('date')
        event.location=request.POST.get('location')
        event.organizer=Organizer.objects.get(id=request.POST.get('organizer'))
        event.save()
        return redirect('list_events')
    return render(request,'update_event.html',{'event':event,'organizers':organizers})
def delete_organizer(request, id):
    organizer=Organizer.objects.get(id=id)
    organizer.delete()
    return redirect('list_organizers')
def delete_event(request, id):
    event=Event.objects.get(id=id)
    event.delete()
    return redirect('list_events')

# def add_product(request):
#     if request.method == 'POST':
#         name=request.POST['name']
#         category_id=request.POST['category']
#         price=request.POST['price']
#         stock_quantity=request.POST['stock_quantity']
#         category=Category.objects.get(id=category_id)
#         product=Product(name=name,category=category,price=price,stock_quantity=stock_quantity)
#         product.save()
#         return redirect('product_list')
#     categories=Category.objects.all()
#     return render(request,'add_product.html',{'categories':categories})
# def add_category(request):
#     Categories=Category.objects.all()
#     if request.method == 'POST':
#         name=request.POST.get('title')
#         description=request.POST.get('date')
#         categories=Organizer.objects.get(id=organizer_id)
#         Event.objects.create(title=title,date=date,location=location,organizer=organizer)
#         return redirect('list_events')
#     return render(request,'add_event.html',{'organizers':organizers})
# def list_product(request):
#     lists=Product.objects.all()
#     if request.method == "POST":
#         value=request.POST.get('search')
#         srch=Product.objects.filter(Q(name__icontains=value))
#         return render(request,'list_product.html',{'lists':srch})
#     return render(request,'list_product.html',{'lists':lists})



def hotel_list(request):
    hotels=Hotel.objects.all()
    if request.method == "POST":
        search_t=request.POST.get('search')
        if search_t:
            hotels=hotels.filter(name_icontains=search_t)
    return render(request,'hotel_list.html',{'hotels':hotels})
def hotel_bookings(request,hotel_id):
    hotel=Hotel.objects.filter(id=hotel_id).first()
    bookings=hotel.bookings.all() if hotel else []
    return render(request,'hotel_bookings.html',{'hotel': hotel,'bookings':bookings})
def create_hotel(request):
    if request.method == 'POST':
        name=request.POST['name']
        location=request.POST['location']
        rating=request.POST['rating']
        description=request.POST.get('description', '')
        Hotel.objects.create(name=name,location=location,rating=rating,description=description)
        return redirect('hotel_list')
    return render(request,'create_hotel.html')
def create_booking(request):
    if request.method == 'POST':
        guest_name=request.POST['guest_name']
        check_in_date=request.POST['check_in_date']
        hotel_id=request.POST['hotel']
        hotel=Hotel.objects.filter(id=hotel_id).first()
        if hotel:
            Booking.objects.create(guest_name=guest_name,check_in_date=check_in_date,hotel=hotel)
            return redirect('hotel_bookings',hotel_id=hotel.id)
    hotels=Hotel.objects.all()
    return render(request,'create_booking.html',{'hotels': hotels})
def update_booking(request,booking_id):
    booking=Booking.objects.filter(id=booking_id).first()
    if booking:
        if request.method == 'POST':
            booking.guest_name=request.POST['guest_name']
            booking.save()
            return redirect('hotel_bookings',hotel_id=booking.hotel.id)
    return render(request,'update_booking.html',{'booking':booking})
def update_hotel(request, hotel_id):
    hotel=Hotel.objects.filter(id=hotel_id).first()
    if hotel:
        if request.method == 'POST':
            hotel.name=request.POST['name']
            hotel.location=request.POST['location']
            hotel.rating=request.POST['rating']
            hotel.description=request.POST.get('description','')
            hotel.save()
            return redirect('hotel_list')
    return render(request, 'update_hotel.html', {'hotel': hotel})
def delete_hotel(request,hotel_id):
    hotel=Hotel.objects.filter(id=hotel_id).first()
    if hotel:
        hotel.delete()
    return redirect('hotel_list')
def delete_booking(request,booking_id):
    booking=Booking.objects.filter(id=booking_id).first()
    hotel_id=booking.hotel.id if booking else None
    if booking:
        booking.delete()
    return redirect('hotel_bookings',hotel_id=hotel_id) if hotel_id else redirect('hotel_list')
def high_rating_hotels(request,min_rating):
    hotels=Hotel.objects.filter(rating__gt=min_rating)
    return render(request,'high_rating_hotels.html',{'hotels':hotels})

from .forms import userform
def fun14(request):
    if request.method == "POST":
        form=userform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=userform()
    return render(request,"users.html",{'form1':form})

from .forms import UserProfileForm
def manage_profile(request):
    if request.method == "POST":
        form=UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=UserProfileForm()
    return render(request,"profile_form.html",{'form2': form})

def login(request):
    return render(request,"staticlogin.html")




from .forms import PostForm
def post_blog(request):
    posts = Post.objects.all()
    return render(request, 'post_blog.html', {'posts': posts})
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_blog') 
    else:
        form = PostForm()
        return render(request, 'postblog_form.html', {'form': form}) 
def update_post(request,pk):
    post=Post.objects.get(pk=pk)
    if request.method == "POST":
        post.title=request.POST.get('title')
        post.content=request.POST.get('content')
        post.save()
        return redirect('post_blog')
    form=PostForm(instance=post)
    return render(request,'update_post.html',{'form':form,'post':post})
def delete_post(request,pk):
    post=Post.objects.get(pk=pk)
    post.delete()
    return redirect('post_blog')
def loginblog(request):
    if request.method == "POST":
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_blog') 
    else:
        form=PostForm()
    posts=Post.objects.all()
    return render(request,'staticblog_table.html',{'posts':posts,'form':form}) 

from .forms import userregistrationform
def user(request):
    if request.method == 'POST':
      data=userregistrationform(request.POST)
      if data.is_valid():
            data.save()
    else:
        data=userregistrationform()
    return render(request,'add_userregistration.html',{'form':data})

def disp_img(request):
    img1=userimg.objects.all()
    return render(request,'userimg_table.html',{'img1':img1})
    
def add_image(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        image=request.FILES.get('image')
        obj=Image(title=title, image=image)
        obj.save()
    return render(request,'image_form.html')
def view_image(request):
    data=Image.objects.all()
    return render(request,'view_image.html',{'dataa':data})

def base(request):
    return render(request,"base.html")
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")

def base1(request):
    return render(request,"base1.html")
def home1(request):
    return render(request,"home1.html")
def about1(request):
    return render(request,"about1.html")
def categories1(request):
    return render(request,"categories1.html")


def home(request):
    return render(request, 'home2.html')
def products(request):
    products = [
        {'name': 'Product 1', 'description': 'Description of product 1', 'price': 10.00},
        {'name': 'Product 2', 'description': 'Description of product 2', 'price': 15.00},
        {'name': 'Product 3', 'description': 'Description of product 3', 'price': 20.00},
    ]
    return render(request, 'products.html', {'products': products})
def profile(request):
    return render(request, 'profile.html')