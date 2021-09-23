from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls import url

urlpatterns = [
    #path("",views.homePage,name='home'),
    path("login/",views.loginPage,name='login'),
    path("",views.home,name='home'),
    path("home/",views.home,name='home'),
    path("home2/",views.home2,name='home2'),
    path("registration/",views.registration,name='registration'),
    path("logoutUser",views.logoutUser,name='logoutUser'),
    path("menu",views.menu,name='menu'),
    path("emp",views.emp,name='emp'),
    path("machine",views.machine,name='machine'),
    path("mpp",views.mpp,name='mpp'),
    path("monthlypp",views.monthlypp,name='monthlypp'),
    path("month",views.month,name='month'),
    path("about",views.about,name='about'),
    
    path("display_months",views.display_months,name='display_months'),

    url(r'^mont$', views.index, name='index'),
    url(r'^months$', views.display_months, name="display_months"),
    url(r'^add_month$', views.add_month, name="add_month"),
    url(r'^months/edit_item/(?P<pk>\d+)$', views.edit_month, name="edit_month"),
    url(r'^months/delete/(?P<pk>\d+)$', views.delete_month, name="delete_month"),

    path("display_machines",views.display_machines,name='display_machines'),

    url(r'^mac$', views.machineindex, name='machineindex'),
    url(r'^machines$', views.display_machines, name="display_machines"),
    url(r'^add_machine$', views.add_machine, name="add_machine"),
    url(r'^machines/edit_item/(?P<pk>\d+)$', views.edit_machine, name="edit_machine"),
    url(r'^machines/delete/(?P<pk>\d+)$', views.delete_machine, name="delete_machine"),

    path("display_employees",views.display_employees,name='display_employees'),

    url(r'^empl$', views.employeeindex, name='employeeindex'),
    url(r'^employees$', views.display_employees, name="display_employees"),
    url(r'^add_employee$', views.add_employee, name="add_employee"),
    url(r'^employees/edit_item/(?P<pk>\d+)$', views.edit_employee, name="edit_employee"),
    url(r'^employees/delete/(?P<pk>\d+)$', views.delete_employee, name="delete_employee"),

    path("display_mpps",views.display_mpps,name='display_mpps'),

        
    url(r'^mpps$', views.display_mpps, name="display_mpps"),
    url(r'^add_mpp$', views.add_mpp, name="add_mpp"),
    url(r'^mpps/edit_item/(?P<month>[-\w]+)/(?P<version>[-\w\ ]+)/(?P<pk>\d+)$', views.edit_mpp, name="edit_mpp"),
    url(r'^mpps/delete/(?P<pk>\d+)$', views.delete_mpp, name="delete_mpp"),

    url(r'^yetto$', views.yetto, name="yetto"),
    path("manpower_display/", views.manpower_display, name="manpower"),
    path("shift_display/", views.shift_display, name="shift"),
    
    url(r'^mppupload$', views.mppupload, name="mppupload"),
    url(r'^mppprevious$', views.mppprevious, name="mppprevious"),
    

]