from django.urls import path
from guest import views

# urls pattern
urlpatterns = [
  path('state',views.state, name='state'),
  path('district',views.districts, name='district'),
  path('district/<data>',views.districts, name='district'),
  path('update_district/<data>',views.updatedistrict,name='updatedistrict'),
  path('addbylaw',views.addbylaw, name='addbylaw'),
  path('addbylaw/<data>',views.addbylaw,name='addbylaw'),
  path('update_addbylaw/<data>',views.updateaddbylaw,name='updateaddbylaw'),
  path('addmember',views.addmember, name='addmember'),
  path('addmember/<data>',views.addmember, name='addmember'),
  path('update_addmember/<data>',views.updateaddmember,name='updateaddmember'),
  path('institution',views.institutions, name='institution'),
  path('institution/<data>',views.institutions, name='institution'),
  path('update_institution/<data>',views.updateinstitution,name='updateinstitution'),
  path('affiliates',views.affiliate, name='affiliates'),
  path('affiliates/<data>',views.affiliate, name='affiliates'),
  path('update_affiliates/<data>',views.updateaffiliates,name='updateaffiliates'),
  path('events',views.event, name='events'),
  path('getdistrictbyid/<data>',views.getdistrictbyid, name='getdistrictbyid'),
  path('events/<data>',views.event, name='events'),
  path('update_events/<data>',views.updateevents,name='updateevents'),
  path('annualreport',views.annualreports, name='annualreport'),  
  path('annualreport/<data>',views.annualreports,name='annualreport'),
  path('update_annualreport/<data>',views.updateannualreport,name='updateannualreport'),
  path('signup',views.signupp, name='signup'),
  # path('subscription/<data>',views.subscription, name='subscription'),
  path('addmembershiptype',views.addmembershiptype, name='addmembershiptype'),
  path('addmembershiptype/<data>',views.addmembershiptype, name='addmembershiptype'),
  path('update_membershiptype/<data>',views.updatemembershiptype,name='updatemembershiptype'),
  path('addmembershipsubscription',views.addmembershipsubscription, name='addmembershipsubscription'),
  path('addmembershipsubscription/<data>',views.addmembershipsubscription, name='addmembershipsubscription'),
  path('update_membershipsubscription/<data>',views.updatemembershipsubscription,name='updatemembershipsubscription'),
  path('addeventtype',views.addeventtype, name='addeventtype'),
  path('addeventtype/<data>',views.addeventtype, name='addeventtype'),
  path('update_eventtype/<data>',views.updateeventtype,name='updateeventtype'),
  path('addpayment',views.addpayment, name='addpayment'),
  path('getpayment/<data>',views.getpayment, name='getpayment')
  
]