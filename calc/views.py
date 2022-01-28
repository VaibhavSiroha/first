from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Vaibhav'})
def add(request):
    A = str(request.POST.get('num1'))
    password = str(request.POST.get('num2'))
    def check_user_name(A,password):
        db = sql.connect(host="localhost",user="root", password="1234",database="web")
        
        cursor = db.cursor()
        sqle = "SELECT * FROM users WHERE UserName = '%s'" % (A) + "and Password ='%s'" % (password)
        try:
            cursor.execute(sqle)
            results = cursor.fetchall()
            if len(results) == 0:
                res="UserName not found"
            else:
                res="Welcome " + A
        except:
            print("Error: unable to fetch data")
        
        return render(request, 'result.html',{'result':res})
    return check_user_name(A,password)