from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from .models import Doctor, Patient
# Create your views here.
def About(request):
	return render(request, 'about.html')
def Home(request):
	return render(request, 'home.html')
def Contact(request):
	return render(request, 'contact.html')
def Index(request):
	if not request.user.is_staff:
		return redirect('Login')
	doctors = Doctor.objects.all()
	patient = Patient.objects.all()
	
	d = 0
	p = 0
	
	for i in doctors:
		d +=1
	for i in patient:
		p+=1
	
	d1 = {'d': d, 'p': p}
	return render(request, 'index.html', d1)
def Login(request):
	error=""
	if request.method == "POST":
		username=request.POST.get("username")
		password=request.POST.get("password")
		user=auth.authenticate(username=username, password=password)
		if user.is_staff:
			login(request,user)
			error = "no"
		else:
			error = "yes"
	d = {'error': error}
	return render(request,'login.html', d)
		
def Logout_admin(request):
    logout(request)
    return redirect('home');
def View_Doctor(request):
	if not request.user.is_staff:
		return redirect('Login')
	doc= Doctor.objects.all()
	d= {'doc': doc}
	return render(request,'view_doctor.html', d)

def Delete_Doctor(request, pid):
	if not request.user.is_staff:
		return redirect('Login')
	doctor= Doctor.objects.get(id=pid)
	doctor.delete()
	return redirect('view_doctor')
		
		

def Add_Doctor(request):
	error=""
	if not request.user.is_staff:
		return redirect('Login')

	if request.method == "POST":
		n=request.POST["name"]
		m=request.POST["mobile"]
		sp=request.POST["special"]
		try:
			Doctor.objects.create(Name=n, mobile=m, special=sp)
			error = "no"
		except:
			error = "yes"
	d = {'error': error}
	return render(request,'add_doctor.html', d)

def View_Patient(request):
	if not request.user.is_staff:
		return redirect('Login')
	doc= Patient.objects.all()
	d= {'doc': doc}
	return render(request,'view_patient.html', d)

def Delete_Patient(request, pid):
	if not request.user.is_staff:
		return redirect('Login')
	patient= Patient.objects.get(id=pid)
	patient.delete()
	return redirect('view_patient')

def Add_Patient(request):
	error=""
	if not request.user.is_staff:
		return redirect('Login')

	if request.method == "POST":
		n=request.POST["name"]
		g=request.POST["gender"]
		m=request.POST["mobile"]
		a=request.POST["address"]
		try:
			Patient.objects.create(name=n, gender=g, mobile=m, address=a)
			error = "no"
		except:
			error = "yes"
	d = {'error': error}
	return render(request,'add_patient.html', d)

def Add_Appointment(request):
	error=""
	if not request.user.is_staff:
		return redirect('Login')
	doctor1 = Doctor.objects.all()
	patient1 = Patient.objects.all()

	if request.method == "POST":
		n=request.POST["doctor"]
		p=request.POST["patient"]
		da=request.POST["date"]
		t=request.POST["time"]
		doctor=Doctor.objects.filter(Name=n).first()
		patient=Patient.objects.filter(name=p).first()
	    

		try:
			Appointment.objects.create(doctor=n, patient=p, date=da, time=t)
			error = "no"
		except:
			error = "yes"
	d = {'doctor': doctor1, 'patient': patient1, 'error': error}
	return render(request,'add_appointment.html', d)

def View_Appointment(request):
	if not request.user.is_staff:
		return redirect('Login')
	doc=View_Appoinment.objects.all()
	d= {'doc': doc}
	return render(request,'view_appointment.html', d)

def Delete_Appointment(request, pid):
	if not request.user.is_staff:
		return redirect('Login')
	app= Appoinment.objects.get(id=pid)
	app.delete()
	return redirect('view_appointment')
		
		
		



# Create your views here.
