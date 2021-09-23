from django.db import models
from django.urls import reverse

# Create your models here.
class usersLog(models.Model):
    username=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    date=models.DateField()
    def __str__(self):
        return self.username

class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"

class Month(models.Model):

    name= models.CharField(max_length=200, blank=False)
    workdays= models.IntegerField()
    workhours= models.FloatField()
    
    class Meta:
        abstract = True

    def __str__(self):
        return 'Working Days: {0} Working Hours: {1}'.format(self.name, self.workdays)

class Months(Month):
    pass


class Machine(models.Model):
    
    mcid= models.CharField(max_length=200, blank=True)
    vsmname= models.CharField(max_length=200, blank=False)
    mcname= models.CharField(max_length=200, blank=False)
    mcskilllevel= models.IntegerField(blank=True, null=True)
    nomcs=models.IntegerField(blank=True, null=True)
    stdmng=models.FloatField(blank=True, null=True)
    opperhour=models.IntegerField(blank=True, null=True)
    efficiency=models.FloatField(blank=True, null=True)
    
    class Meta:
        abstract = True

    def __str__(self):
        return 'Machine Name: {0} VSM Name: {1} '.format(self.mcname, self.vsmname)

class Machines(Machine):
    pass

class MPP(models.Model):
    #ids=models.IntegerField(blank=True, null=True,default=123)
    vsmname= models.CharField(max_length=200, blank=False,default='SOME')
    mcname= models.CharField(max_length=200, blank=False,default='SOME STRING')
    prodqty=models.FloatField(blank=True, null=True,default=123)
    
    

    def _str_(self):
        return 'VSM Name: {0} Machine Name: {1} '.format(self.vsmname, self.mcname)



class MPPMarch1s(MPP):
    pass
class MPPMarch2s(MPP):
    pass

class Manpower(models.Model):
    vsmname= models.CharField(max_length=200, blank=False)
    mcname= models.CharField(max_length=200, blank=False)
    skilllevel=models.IntegerField(blank=True, null=True)
    prodqty=models.FloatField(blank=True, null=True)
    stdmng=models.FloatField(blank=True, null=True)
    nomcs=models.IntegerField(blank=True, null=True)
    manpower=models.IntegerField(blank=True, null=True)
    shifts=models.IntegerField(blank=True, null=True)


    '''def __init__(self, vsmname, mcname, prodqty, stdmng,nomcs,manpower,shifts):
        self.vsmname=vsmname
        self.mcname=mcname
        self.prodqty=prodqty
        self.stdmng=stdmng
        self.nomcs=nomcs
        self.manpower=manpower
        self.shifts=shifts'''

    def __str__(self):
        return 'VSM Name: {0} Machine Name: {1} Production Qty: {2} '.format(self.vsmname, self.mcname, self.prodqty)

class Manpowers(Manpower):
    pass

class Employee(models.Model):
    empid= models.CharField(max_length=200, blank=True)
    empname= models.CharField(max_length=200, blank=False)
    doj= models.CharField(max_length=200, blank=False)
    mcname= models.CharField(max_length=200, blank=False)
    skilllevel= models.IntegerField(blank=True, null=True)
    
    class Meta:
        abstract = True

    def __str__(self):
        return 'Employee Id: {0} Employee Name: {1} '.format(self.empid, self.empname)

class Employees(Employee):
    pass

class Schedule(models.Model):
    vsmname= models.CharField(max_length=200, blank=True)
    mcname= models.CharField(max_length=200, blank=True)
    shiftnor= models.IntegerField(blank=True, null=True)
    empid= models.CharField(max_length=200, blank=False)
    empname= models.CharField(max_length=200, blank=False)
    url = models.URLField(max_length=100,verbose_name="Image Url",help_text="Add url of the image to be displayed")

    def __str__(self):
        return 'VSM : {0} Machine Name: {1} '.format(self.vsmname, self.mcname)
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('place-detail', args=[str(self.place)])


class Schedules(Schedule):
    pass