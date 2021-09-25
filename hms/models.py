from django.db import models



class Doctor(models.Model):
	 Name=models.CharField(max_length=50)
	 mobile=models.IntegerField()
	 special=models.CharField(max_length=50)
	 def __str__(self):
	 	 return self.Name

	
	



class Patient(models.Model):
	 name=models.CharField(max_length=50)
	 gender=models.CharField(max_length=10)
	 address=models.CharField(max_length=50)
	 mobile=models.IntegerField(null=True)
	 def __str__(self):
	 	 return self.name



class Appoinment(models.Model):
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
class AppoinmentDate(models.Model):	
	date=models.DateField()
	time=models.TimeField()

# Create your models here.
