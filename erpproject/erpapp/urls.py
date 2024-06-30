from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('empregistration',views.empregistration,name="empregistration"),
    path('stdregistration', views.stdregistration, name="stdregistration"),
    path('emplogin',views.emplogin,name="emplogin"),
    path('stdlogin',views.stdlogin,name="stdlogin"),
    path('checkemplogin',views.checkemplogin,name="checkemplogin"),
    path('checkstdlogin',views.checkstdlogin,name="checkstdlogin"),
    path('emphome',views.emphome,name="emphome"),
    path('stdhome',views.stdhome,name="stdhome"),
    path('empprofile',views.empprofile,name="empprofile"),
    path('stdprofile',views.stdprofile,name="stdprofile"),
    path('empchangepwd',views.empchangepwd,name="empchangepwd"),
    path('stdchangepwd',views.stdchangepwd,name="stdchangepwd"),
    path('empupdatepwd', views.empupdatepwd, name="empupdatepwd"),
    path('stdupdatepwd', views.stdupdatepwd, name="stdupdatepwd"),
    path("vieweproducts",views.vieweproducts,name="vieweproducts"),
    path("viewsproducts", views.viewsproducts, name="viewsproducts"),
    path("displayeproducts",views.displayeproducts,name="displayeproducts"),
    path("displaysproducts",views.displaysproducts,name="displaysproducts"),
    path('emplogout',views.emplogout,name='emplogout'),
    path('stdlogout',views.stdlogout,name='stdlogout'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('checkadminlogin',views.checkadminlogin,name="checkadminlogin"),
    path('adminhome',views.adminhome,name="adminhome"),
    path("adddept",views.adddepartment,name="adddept"),
    path("updatedept",views.updatedepartment,name="updatedept"),
    path("addproduct",views.addproduct,name="addproduct"),
    path("viewaproducts",views.viewaproducts,name="viewaproducts"),
    path('viewemps',views.viewemployees,name="viewemps"),
    path('viewstd',views.viewstudents,name="viewstd"),
    path('viewdepts',views.viewdepartments,name="viewdepts"),
    path("deleteemp/<int:eid>",views.deleteemp,name="deleteemp"),
    path('adminlogout', views.adminlogout, name='adminlogout'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

