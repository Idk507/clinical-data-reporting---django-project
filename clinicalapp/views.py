from django.shortcuts import render
from clinicalapp.models import patient,clinicaldata
from clinicalapp.forms import patientform,clinicaldataform
from django.views.generic import  ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
# Create your views here.

class patientlistview(ListView):
    model = patient
    
class patientcreateview(CreateView):
    model = patient
    success_url = reverse_lazy('index')
    fields = ('firstname','lastname','age')

class patientupdateview(UpdateView):
    model = patient
    success_url = reverse_lazy('index')
    fields = ('firstname','lastname','age')

class patientdeleteview(DeleteView):
    model = patient
    success_url = reverse_lazy('index')
    
def adddata(request,**kwargs):
    form = clinicaldataform()
    Patient = patient.objects.get(id = kwargs['pk'])
    if request.method == 'POST':
        form = clinicaldataform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')    
    return  render(request,'clinicaldata_form.html',{'form':form,'Patient':Patient})

def analyse(request,**kwargs):
    data = clinicaldata.objects.filter(patient_id=kwargs['pk'])
    responsedata = []
    for entry in data:
        if entry.componentname == 'hw':
            heightandweight = entry.componentvalue.split('/')
            if len(heightandweight)>1:
                feettometer = float(heightandweight[0])*0.4536
                BMI = (float(heightandweight[1]))/(feettometer**2)
                bmiEntry = clinicaldata()
                bmiEntry.componentname = 'BMI'
                bmiEntry.componentvalue = BMI
                bmiEntry.measureddatetime = entry.measureddatetime
                bmiEntry.patient_id = entry.patient_id
                responsedata.append(bmiEntry)
        print(responsedata)        
        responsedata.append(entry)
      
    return render(request,'generatereport.html',{'data':responsedata})