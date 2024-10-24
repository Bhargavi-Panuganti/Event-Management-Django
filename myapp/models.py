from django.db import models

# Create your models here.
class world(models.Model):
    country=models.CharField(max_length=30)
    continentt=models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.country+" "+self.continent

class MenuCat(models.Model):
    menu_categ=models.CharField(max_length=120)
    def __str__(self) -> str:
        return self.menu_categ
items=[(1,"indian"),(2,"French"),(3,"Roman"),(4,"Greek")]
class Menu(models.Model):
    menuitem=models.CharField(max_length=120)
    price=models.IntegerField(default='0')
    categ_id=models.IntegerField(choices=items)
    def __tuple__(self) -> tuple:
        return self.menuitem,self.price,self.categ_id



    
class Venue(models.Model):
    name=models.CharField('Venue Name',max_length=50)
    address=models.CharField(max_length=50)
    zip=models.CharField('Zip code',max_length=50)
    phone=models.CharField('Phone No',max_length=10)
    web=models.URLField('website',blank=True)
    email_address=models.EmailField('Email')
    def __str__(self) -> str:
        return self.name

class MyUser(models.Model):
    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    email=models.EmailField('User Email')
    def __str__(self) -> str:
        return self.first_name+" "+self.last_name
    

class Event(models.Model):
    name=models.CharField('Event Name',max_length=50)
    event_date=models.DateTimeField('Event Date')
    venue=models.ForeignKey(Venue,blank=True,null=True,on_delete=models.CASCADE)
    manager=models.CharField(max_length=60)
    description=models.TextField(blank=True)
    attendes=models.ManyToManyField(MyUser,blank=True)

    def __str__(self) -> str:
        return self.name
    
