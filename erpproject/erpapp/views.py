from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EmployeeRegistrationForm, ProductForm, AdminLoginForm, DepartmentForm, UpdateDepartmentForm, \
    StudentRegistrationForm
from .models import Faculty, Department, Admin, Course, Student


def index(request):
    return render(request, "index.html")


def empregistration(request):
    form = EmployeeRegistrationForm()
    if request.method == "POST":
        formdata = EmployeeRegistrationForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg = "Faculty Registered Successfully"
            return render(request, "empregistration.html", {"empform": form, "msg": msg})
        else:
            msg = "Failed to Register Faculty"
            return render(request, "empregistration.html", {"empform": form, "msg": msg})
    return render(request, "empregistration.html", {"empform": form})


def emplogin(request):
    return render(request, "emplogin.html")


def checkemplogin(request):
    uname = request.POST["eusername"]
    pwd = request.POST["epassword"]

    flag = Faculty.objects.filter(Q(username=uname) & Q(password=pwd))

    if flag:
        emp = Faculty.objects.get(username=uname)
        request.session["eid"] = emp.id
        request.session["ename"] = emp.fullname
        return render(request, "emphome.html", {"eid": emp.id, "ename": emp.fullname})
    else:
        msg = "Login Failed"
        return render(request, "emplogin.html", {"msg": msg})


def emphome(request):
    eid = request.session["eid"]
    ename = request.session["ename"]

    return render(request, "emphome.html", {"eid": eid, "ename": ename})


def empprofile(request):
    eid = request.session["eid"]
    ename = request.session["ename"]
    emp = Faculty.objects.get(id=eid)
    return render(request, "empprofile.html", {"eid": eid, "ename": ename, "emp": emp})


def empchangepwd(request):
    eid = request.session["eid"]
    ename = request.session["ename"]
    return render(request, "empchangepwd.html", {"eid": eid, "ename": ename})


def empupdatepwd(request):
    eid = request.session["eid"]
    ename = request.session["ename"]

    opwd = request.POST["opwd"]
    npwd = request.POST["npwd"]

    flag = Faculty.objects.filter(Q(id=eid) & Q(password=opwd))

    if flag:
        Faculty.objects.filter(id=eid).update(password=npwd)
        msg = "Password Updated Successfully"
        return render(request, "empchangepwd.html", {"eid": eid, "ename": ename, "msg": msg})
    else:
        msg = "Old Password is Incorrect"
        return render(request, "empchangepwd.html", {"eid": eid, "ename": ename, "msg": msg})


def vieweproducts(request):
    eid = request.session["eid"]
    ename = request.session["ename"]

    productlist = Course.objects.all()

    return render(request, "vieweproducts.html", {"eid": eid, "ename": ename, "productlist": productlist})


def displayeproducts(request):
    eid = request.session["eid"]
    ename = request.session["ename"]

    pname = request.POST["pname"]

    productlist = Course.objects.filter(name__icontains=pname)

    return render(request, "displayeproducts.html", {"eid": eid, "ename": ename, "productlist": productlist})


def emplogout(request):
    request.session.flush()
    return redirect("emplogin")


def adminlogin(request):
    return render(request, "adminlogin.html")


def checkadminlogin(request):
    uname = request.POST["ausername"]
    pwd = request.POST["apassword"]

    flag = Admin.objects.filter(Q(username__exact=uname) & Q(password__exact=pwd))

    if flag:
        admin = Admin.objects.get(username=uname)
        request.session["auname"] = admin.username
        return redirect("adminhome")
    else:
        msg = "Login Failed"
        return render(request, "adminlogin.html", {"msg": msg})


def adminhome(request):
    if "auname" not in request.session:
        return redirect("adminlogin")
    auname = request.session["auname"]

    # Gather additional context data for the dashboard
    employee_count = Faculty.objects.count()
    course_count = Course.objects.count()
    product_count = Course.objects.count()
    student_count = Student.objects.count()

    return render(request, "adminhome.html", {
        "auname": auname,
        "employee_count": employee_count,
        "course_count": course_count,
        "product_count": product_count,
        "student_count":student_count
    })


def adddepartment(request):
    auname = request.session["auname"]
    form = DepartmentForm()
    if request.method == "POST":
        formdata = DepartmentForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg = "Department Added Successfully"
            return render(request, "adddept.html", {"auname": auname, "deptform": form, "msg": msg})
        else:
            msg = "Failed to Add Department"
            return render(request, "adddept.html", {"auname": auname, "deptform": form, "msg": msg})
    return render(request, "adddept.html", {"auname": auname, "deptform": form})


def updatedepartment(request):
    auname = request.session["auname"]
    form = UpdateDepartmentForm()
    if request.method == "POST":
        formdata = UpdateDepartmentForm(request.POST)

        deptid = formdata.data['id']
        deptname = formdata.data['name']
        deptloc = formdata.data['location']

        flag = Department.objects.filter(id=deptid)

        if flag:
            Department.objects.filter(id=deptid).update(name=deptname, location=deptloc)
            msg = "Department Updated Successfully"
            return render(request, "updatedept.html", {"auname": auname, "deptform": form, "msg": msg})
        else:
            msg = "Department ID Not Found"
            return render(request, "updatedept.html", {"auname": auname, "deptform": form, "msg": msg})

    return render(request, "updatedept.html", {"auname": auname, "deptform": form})


def addproduct(request):
    auname = request.session["auname"]
    form = ProductForm()
    if request.method == "POST":
        formdata = ProductForm(request.POST, request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg = "Product Added Successfully"
            return render(request, "addproduct.html", {"auname": auname, "productform": form, "msg": msg})
        else:
            msg = "Failed to Add Product"
            return render(request, "addproduct.html", {"auname": auname, "productform": form, "msg": msg})
    return render(request, "addproduct.html", {"auname": auname, "productform": form})


def viewemployees(request):
    auname = request.session["auname"]
    emplist = Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request, "viewemps.html", {"auname": auname, "emplist": emplist, "count": count})


def viewdepartments(request):
    auname = request.session["auname"]
    deptlist = Department.objects.all()
    count = Department.objects.count()
    return render(request, "viewdepts.html", {"auname": auname, "deptlist": deptlist, "count": count})


def viewaproducts(request):
    auname = request.session["auname"]
    productlist = Course.objects.all()
    count = Course.objects.count()
    return render(request, "viewaproducts.html", {"auname": auname, "productlist": productlist, "count": count})


def deleteemp(request, eid):
    Faculty.objects.filter(id=eid).delete()
    return redirect("viewemps")


def adminlogout(request):
    request.session.flush()
    return redirect("adminlogin")


def stdregistration(request):
    form = StudentRegistrationForm()
    if request.method == "POST":
        formdata = StudentRegistrationForm(request.POST)
        if formdata.is_valid():
            formdata.save()
            msg = "Student Registered Successfully"
            return render(request, "stdregistration.html", {"stdform": form, "msg": msg})
        else:
            msg = "Failed to Register Student"
            return render(request, "stdregistration.html", {"stdform": form, "msg": msg})
    return render(request, "stdregistration.html", {"stdform": form})


def stdlogin(request):
    return render(request, "stdlogin.html")


def checkstdlogin(request):
    uname = request.POST["susername"]
    pwd = request.POST["spassword"]

    flag = Student.objects.filter(Q(username=uname) & Q(password=pwd))

    if flag:
        std = Student.objects.get(username=uname)
        request.session["sid"] = std.id
        request.session["sname"] = std.username
        return render(request, "stdhome.html", {"sid": std.id, "sname": std.username})
    else:
        msg = "Login Failed"
        return render(request, "stdlogin.html", {"msg": msg})


def viewstudents(request):
    sname = request.session["suname"]
    stdlist = Student.objects.all()
    count = Student.objects.count()
    return render(request, "viewstd.html", {"sname": sname, "stdlist": stdlist, "count": count})


def deletestd(request, eid):
    Student.objects.filter(id=eid).delete()
    return redirect("viewstd")


def stdhome(request):
    sid = request.session["sid"]
    sname = request.session["sname"]

    return render(request, "stdhome.html", {"sid": sid, "sname": sname})


def stdprofile(request):
    sid = request.session["sid"]
    sname = request.session["sname"]
    std = Student.objects.get(id=sid)
    return render(request, "stdprofile.html", {"sid": sid, "sname": sname, "std": std})


def stdchangepwd(request):
    sid = request.session["sid"]
    sname = request.session["sname"]
    return render(request, "stdchangepwd.html", {"sid": sid, "sname": sname})


def stdupdatepwd(request):
    sid = request.session["sid"]
    sname = request.session["sname"]

    oopwd = request.POST["oopwd"]
    nnpwd = request.POST["nnpwd"]

    flag = Student.objects.filter(Q(id=sid) & Q(password=oopwd))

    if flag:
        Student.objects.filter(id=sid).update(password=nnpwd)
        msg = "Password Updated Successfully"
        return render(request, "stdchangepwd.html", {"sid": sid, "sname": sname, "msg": msg})
    else:
        msg = "Old Password is Incorrect"
        return render(request, "stdchangepwd.html", {"sid": sid, "sname": sname, "msg": msg})


def stdlogout(request):
    request.session.flush()
    return redirect("stdlogin")


def viewsproducts(request):
    sid = request.session["sid"]
    sname = request.session["sname"]

    productlist = Course.objects.all()

    return render(request, "viewsproducts.html", {"sid": sid, "sname": sname, "productlist": productlist})


def displaysproducts(request):
    sid = request.session["sid"]
    sname = request.session["sname"]

    prname = request.POST["prname"]

    productlist = Course.objects.filter(name__icontains=prname)

    return render(request, "displaysproducts.html", {"sid": sid, "sname": sname, "productlist": productlist})


def setcookies(request):
    response = HttpResponse("COOKIES DEMO .. !!")
    response.set_cookie("username", "KLEF")  # non-persistent cookie
    response.set_cookie("location", "Hyderabad", max_age=15)  # persistent cookie
    return response


def getcookies(request):
    uname = request.COOKIES.get("username")
    loc = request.COOKIES.get("location")

    if uname is not None and loc is not None:
        response = uname + "," + loc
    elif uname is not None and loc is None:
        response = uname
    elif uname is None and loc is not None:
        response = loc
    else:
        response = "COOKIES NOT FOUND"

    return HttpResponse(response)