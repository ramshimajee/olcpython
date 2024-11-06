from django.db import models

class country(models.Model):
    countryid = models.AutoField(primary_key=True)
    countryname = models.CharField(max_length=50)
    
    def __str__(self):
        return self.countryname

class states(models.Model):
    stateid = models.AutoField(primary_key=True)
    country=models.ForeignKey(country, on_delete=models.CASCADE)
    statename = models.CharField(max_length=50)
    
    def __str__(self):
        return self.statename
    
class district(models.Model):
    districtid = models.AutoField(primary_key=True)
    country=models.ForeignKey(country, on_delete=models.CASCADE)
    state = models.ForeignKey(states, on_delete=models.CASCADE)
    districtname = models.CharField(max_length=100)
    
    def __str__(self):
        return self.districtname
    
class bylawtable(models.Model):
    description =models.TextField()
    image = models.ImageField(upload_to='image/')
    
    def _str_(self):
        return self.description
    
class boardmembers(models.Model):
    firstname =models.CharField(max_length=100)
    lastname =models.CharField(max_length=100)
    designation =models.CharField(max_length=100)
    affliation = models.CharField(max_length=50)
    duration_from =models.DateField()
    duration_to=models.DateField()
    image = models.ImageField(upload_to='image/')
    twitter =models.CharField(max_length=50)
    ORCID = models.BigIntegerField()
    
    
    def _str_(self):
        return self.firstname

    
class institution(models.Model):
    institutionname = models.CharField(max_length=100)
    institutionlink= models.CharField(max_length=100)
    countrys = models.ForeignKey(country,on_delete=models.CASCADE)
    state = models.ForeignKey(states,on_delete=models.CASCADE)
    districts = models.ForeignKey(district,on_delete=models.CASCADE)
    
    def _str_(self):
        return self.institutionname
    
class affiliates(models.Model):
    affiliatesname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/')
    affiliateslink= models.CharField(max_length=100)
    
    def _str_(self):
        return self.affiliatesname
    
class eventtype(models.Model):
    eventtypename = models.CharField(max_length=100)
    eventtypedescription = models.TextField()
   
    
    def _str_(self):
        return self.eventtypename
    
class events(models.Model):
    eventname =models.CharField(max_length=100)
    eventdate =models.DateField()
    eventtime =models.CharField(max_length=50)
    state=models.ForeignKey(states, on_delete=models.CASCADE)
    district=models.ForeignKey(district,  on_delete=models.CASCADE)
    eventplace=models.CharField(max_length=50)
    eventdescription = models.TextField()
    eventbrochure = models.ImageField(upload_to='image/')
    eventtype=models.ForeignKey(eventtype, on_delete=models.CASCADE)
       
    def _str_(self):
        return self.eventname
    
class annualreport(models.Model):
    annualdescription =models.TextField()
    annualbrochure = models.ImageField(upload_to='image/')
    
    def _str_(self):
        return self.annualdescription

class subscribe(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    role=models.CharField( max_length=50)
    status=models.CharField(max_length=50)
    
    def _str_(self):
        return self.email
    
    
class signup(models.Model):
    country=models.ForeignKey(country, on_delete=models.CASCADE)
    state=models.ForeignKey(states, on_delete=models.CASCADE)
    district=models.ForeignKey(district,  on_delete=models.CASCADE)
    institution=models.ForeignKey(institution, on_delete=models.CASCADE)
    library = models.CharField(max_length=50)
    registereddate =models.DateTimeField()
    subscribe=models.ForeignKey(subscribe, on_delete=models.CASCADE)
    
    def _str_(self):
        return self.country
    
class membershiptype(models.Model):
    membershiptypename = models.CharField(max_length=100)
    description= models.TextField()
    
    def _str_(self):
        return self.membershiptypename
    
class membershipsubscription(models.Model):
    membershiptype = models.ForeignKey(membershiptype, on_delete=models.CASCADE)
    duration = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()
  
    def _str_(self):
        return self.duration
    
class payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    member=models.ForeignKey(signup, on_delete=models.CASCADE)
    membershiptype= models.ForeignKey(membershiptype, on_delete=models.CASCADE) 
    price= models.FloatField()
    payment_date= models.DateField() 
    payment_status = models.CharField(max_length=100)  
  