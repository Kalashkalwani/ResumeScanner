from django.shortcuts import render
from django.http import HttpResponse
from . import analyser

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.template.defaulttags import register

# Create your views here.

def index(request):
    if request.method == 'POST':
        myfile = request.FILES['resume']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        item = analyser.analyse('media/'+myfile.name)

        s = int(item['score'].sum(axis=0))
        d={}
        l=['Web Designing & Development','Operations management','Supply chain','Project management','Data Science & ML','Database Management Systems']
        for i in range(len(l)):
            d[l[i]] = round((item.loc[l[i]]['score']/s)*100)
        print(d)

        return render(request, 'result.html', 
        context={'wdd':d['Web Designing & Development'],'om':d['Operations management'],'sc':d['Supply chain'],
        'pm':d['Project management'],'ds':d['Data Science & ML'],'dbms':d['Database Management Systems']})

    return render(request, 'base.html')