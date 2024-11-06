
from django.utils import timezone
import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from guest.models import  *
from guest.serializers import *
from rest_framework import status
from olc import settings
from django.contrib import messages

 

@csrf_exempt
def countrys(request):
    if request.method == 'GET':
        try:
           getcountry=country.objects.all()
           serializer=CountrySerializer(getcountry,many=True)
           return JsonResponse(serializer.data,safe=False,status=200)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
    return JsonResponse({"Data not found"}, status=404)

@csrf_exempt
def state(request,data=0):
    if request.method=='POST':
        try:
            countryid = request.POST.get('countryid')
            statename = request.POST.get('statename')
            print(countryid )
            print( statename)
            countryid =country.objects.get(countryid=countryid)
            
            statereg =states( country=countryid,statename=statename)
            
            statereg.save()
            
    
            return JsonResponse({"message":"State added successfully."}, status=201)
        except country.DoesNotExist:
            return JsonResponse({"error": "data not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    elif request.method =='GET':
        statedetails = states.objects.select_related('country').all()
        serializer =  stateSerializer( statedetails, many=True)
        print(serializer)
     
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method=='DELETE':
        print(data)
        statedetails=states.objects.get(stateid = data)
        print(statedetails)
        statedetails.delete()
        return JsonResponse ("Deleted Successfully", safe=False)
    return JsonResponse ({"error":"invalid request"},status=400) 

@csrf_exempt
def getstatebycountry(request, data):
    if request.method == 'GET':
        statedata=states.objects.select_related('country').filter(country=data)
        serializer= stateSerializer(statedata,many=True)
            
        return JsonResponse(serializer.data,safe=False)
        
        

@csrf_exempt 
def updatestate(request, data):
    if request.method == 'GET':
        try:
            print(data)
            statedata = states.objects.select_related("country").get(stateid=data)
            print("hello")
            serializer= stateSerializer(statedata)
            
            return JsonResponse(serializer.data,safe=False)
        except states.DoesNotExist:
            return JsonResponse({'error':'state not found'}, status=404)
        
    elif request.method == 'POST':
        try:
            # Retrieve the existing data based on the provided id  
            statedata = states.objects.get(stateid=data)
            
            # Get updated data from the request   
            countryid = request.POST.get('countryid')
            print(countryid)
            statename = request.POST.get('statename')
            print(statename)
           
           
            
            # Update data if provided
            if countryid:
                statedata.country_id = countryid
            if statename:
                statedata.statename = statename
                     
            # Save the updated data  
            statedata.save()  
            
            return JsonResponse({"message": "state updated successfully."}, status=200)
        except states.DoesNotExist:
            return JsonResponse({"error": "state not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request."}, status=400) 


@csrf_exempt
def districts(request,data=0):
    if request.method=='POST':
        try:
            countryid= request.POST.get('countryid')
            state = request.POST.get('stateid')
            districtname = request.POST.get('districtname')
            print(countryid)
            print(state )
            print( districtname)
            countryid=country.objects.get(countryid=countryid)
            stateid	=states.objects.get(stateid=state)
            
            districtreg = district(country=countryid,state=stateid,districtname=districtname)
            
            districtreg.save()
            
    
            return JsonResponse({"message":"District added successfully."}, status=201)
        except states.DoesNotExist:
            return JsonResponse({"error": "data not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    elif request.method =='GET':
        districtdetails = district.objects.select_related('country','state').all()
        serializer = districtSerializer(districtdetails, many=True)
        print(serializer)
     
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method=='DELETE':
        print(data)
        districtdetails=district.objects.get(districtid = data)
        print(districtdetails)
        districtdetails.delete()
        return JsonResponse ("Deleted Successfully", safe=False)
    return JsonResponse ({"error":"invalid request"},status=400) 

@csrf_exempt 
def updatedistrict(request, data):
    if request.method == 'GET':
        try:
            districtdata = district.objects.select_related("country","state").get(districtid=data)
            print("hello")
            serializer= districtSerializer(districtdata)
            
            return JsonResponse(serializer.data,safe=False)
        except district.DoesNotExist:
            return JsonResponse({'error':'district not found'}, status=404)
        
    elif request.method == 'POST':
        try:
            # Retrieve the existing data based on the provided id  
            districtdata = district.objects.get(districtid=data)
            
            # Get updated data from the request (
            countryid=request.POST.get('countryid')
            print(countryid) 
            stateid = request.POST.get('stateid')
            print(stateid)
            districtname = request.POST.get('districtname')
            print(districtname)
           
           
            
            # Update data if provided
            if countryid:
                districtdata.country_id = countryid
            if stateid:
                districtdata.state_id = stateid
            if districtname:
                districtdata.districtname = districtname
                     
            # Save the updated data  
            districtdata.save()  
            
            return JsonResponse({"message": "District updated successfully."}, status=200)
        except district.DoesNotExist:
            return JsonResponse({"error": "District not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request."}, status=400) 

@csrf_exempt
def addbylaw(request, data=0):
   
    if request.method == 'POST':
        try:
            description = request.POST.get('description')
            image = request.FILES.get('image')
            print(description)
            print(image)
            if image:
                imagefile = bylawtable(description=description,image=image) 
                imagefile .save()
                
                return JsonResponse({"message": "law uploaded successfully."}, status=201)
        except bylawtable.DoesNotExist:
            return JsonResponse({"error":"data not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
        
    elif request.method == 'GET':
        try:
            datadetails = bylawtable.objects.all()
            serializer = LawSerializer(datadetails, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == 'DELETE':
        print(data)
        datadetails = bylawtable.objects.get(id=data)
        
        print(datadetails)
        if datadetails.image:
            image_path = os.path.join(settings.MEDIA_ROOT, str(datadetails.image))
            if os.path.exists(image_path):
                os.remove(image_path)
                
        datadetails.delete()
       
        return JsonResponse("Deleted Successfully",safe=False)
    return JsonResponse({"error":"invalid request"},status=400)

@csrf_exempt 
def updateaddbylaw(request, data):
    if request.method == 'GET':
        try:
            bylawdata = bylawtable.objects.get( id=data)
            print("hello")
            serializer= LawSerializer( bylawdata)
            
            return JsonResponse(serializer.data,safe=False)
        except bylawtable.DoesNotExist:
            return JsonResponse({'error': 'bylaw not found'}, status=404)
        
    elif request.method == 'POST':
        try:
            # Retrieve the existing data based on the provided id  
            bylawdata = bylawtable.objects.get(id=data)
            
            # Get updated data from the request   
            description = request.POST.get('description')
            print(description)
            image = request.FILES.get('image')
            print(image )
           
           
            
            # Update data if provided
            if description:
                bylawdata.description = description
            if image:
               bylawdata.image = image
                     
            # Save the updated data  
            bylawdata.save()  
            
            return JsonResponse({"message": "bylaw updated successfully."}, status=200)
        except  bylawtable.DoesNotExist:
            return JsonResponse({"error": "bylaw not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request."}, status=400) 

@csrf_exempt
def addmember(request, data=0):
    if request.method == 'POST':
        try:
            firstname = request.POST.get('firstname')
            lastname= request.POST.get('lastname')
            designation= request.POST.get('designation')
            affliation= request.POST.get('affliation')
            duration_from= request.POST.get('duration_from')
            duration_to= request.POST.get('duration_to')
            twitter= request.POST.get('twitter')
            ORCID= request.POST.get('ORCID')
            image = request.FILES.get('image')
            
            print(firstname)
            print(lastname)
            print(designation)
            print(affliation)
            print(duration_from)
            print(duration_to)
            print(twitter)
            print(ORCID)
            print(image)
            
            if image:
                imagefile = boardmembers(firstname=firstname,lastname=lastname,designation=designation,affliation=affliation,duration_from=duration_from,duration_to=duration_to,twitter=twitter,ORCID=ORCID,image=image) 
                
                imagefile .save()
                
                return JsonResponse({"message": "member uploaded successfully."}, status=201)
        except boardmembers.DoesNotExist:
            return JsonResponse({"error":"data not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
        
    elif request.method == 'GET':
        try:
            datadetails = boardmembers.objects.all()
            serializer = BoardSerializer(datadetails, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == 'DELETE':
        print(data)
        datadetails = boardmembers.objects.get(id=data)
        
        print(datadetails)
        if datadetails.image:
            image_path = os.path.join(settings.MEDIA_ROOT, str(datadetails.image))
            if os.path.exists(image_path):
                os.remove(image_path)
                
        datadetails.delete()
       
        return JsonResponse("Deleted Successfully",safe=False)
    return JsonResponse({"error":"invalid request"},status=400)

@csrf_exempt 
def updateaddmember(request, data):
    if request.method == 'GET':
        try:
            boarddata = boardmembers.objects.get( id=data)
            serializer= BoardSerializer( boarddata)
            
            return JsonResponse(serializer.data,safe=False)
        except boardmembers.DoesNotExist:
            return JsonResponse({'error': 'member not found'}, status=404)
        
    elif request.method == 'POST':
        try:
            # Retrieve the existing data based on the provided id  
            boarddata = boardmembers.objects.get(id=data)
            
            # Get updated data from the request 
            firstname = request.POST.get('firstname')
            print(firstname)  
            lastname = request.POST.get('lastname')
            print(lastname)
            designation = request.POST.get('designation')
            print(designation)
            affliation = request.POST.get('affliation')
            print(affliation)
            duration_from = request.POST.get('duration_from')
            print(duration_from)
            duration_to = request.POST.get('duration_to')
            print(duration_to)
            twitter = request.POST.get('twitter')
            print(twitter)
            ORCID = request.POST.get('ORCID')
            print(ORCID)
            image = request.FILES.get('image')
            print(image )
           
           
            
            # Update data if provided
            boarddata.firstname = firstname
            boarddata.lastname = lastname
            boarddata.designation = designation
            boarddata.affliation = affliation
            boarddata.duration_from = duration_from
            boarddata.duration_to = duration_to
            boarddata.twitter = twitter
            boarddata.ORCID = ORCID
            if image:
               boarddata.image = image
                     
            # Save the updated data  
            boarddata.save()  
            
            return JsonResponse({"message": "member updated successfully."}, status=200)
        except  boardmembers.DoesNotExist:
            return JsonResponse({"error": "member not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request."}, status=400) 

@csrf_exempt
def institutions(request, data=0):
    if request.method=='POST':
        try:
            institutionname = request.POST.get('institutionname')
            institutionlink = request.POST.get('institutionlink')
            institution_district = request.POST.get('districtid')
            institution_state = request.POST.get('stateid')
            institution_country = request.POST.get('countryid')
            
            districtId = district.objects.get(districtid=institution_district)
            stateId = states.objects.get(stateid=institution_state)
            countryId = country.objects.get(countryid=institution_country)
            
            addinstitution = institution(institutionname=institutionname, institutionlink=institutionlink,districts=districtId,countrys=countryId,state=stateId)
            
            addinstitution.save()
            
    
            return JsonResponse({"message":"Registration uploaded successfully."}, status=201)
        except institution.DoesNotExist:
            return JsonResponse({"error": "data not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
        
    elif request.method=='GET':
        try:
            datadetails = institution.objects.all()
            serializer = InstitutionSerializer(datadetails,many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    elif request.method=='DELETE':
        print(data)
        
        datadetails= institution.objects.get(id=data)
        print(datadetails)                
        datadetails.delete()
        return JsonResponse("Deleted Successfully", safe=False)              
    return JsonResponse({"error":"invalid request"}, status=400)

@csrf_exempt 
def updateinstitution(request, data):
    if request.method == 'GET':
        try:
            institutiondata = institution.objects.get( id=data)
            serializer= InstitutionSerializer( institutiondata)
            
            return JsonResponse(serializer.data,safe=False)
        except institution.DoesNotExist:
            return JsonResponse({'error': 'institution not found'}, status=404)
        
    elif request.method == 'POST':
        try:
            # Retrieve the existing data based on the provided id  
            institutiondata = institution.objects.get(id=data)
            
            # Get updated data from the request 
            institutionname = request.POST.get('institutionname')
            print(institutionname)  
            institutionlink = request.POST.get('institutionlink')
            print(institutionlink)
            institution_district = request.POST.get('districtid')
            institution_state = request.POST.get('stateid')
            institution_country = request.POST.get('countryid')
            
            districtId = district.objects.get(districtid=institution_district)
            stateId = states.objects.get(stateid=institution_state)
            countryId = country.objects.get(countryid=institution_country)
            
           
            # Update data if provided
            if institutionname :
                institutiondata.institutionname  = institutionname 
            if institutionlink:
                institutiondata.institutionlink = institutionlink
            institutiondata.countrys = countryId
            institutiondata.state = stateId
            institutiondata.districts = districtId         
            # Save the updated data  
            institutiondata.save()  
            
            return JsonResponse({"message": "institution updated successfully."}, status=200)
        except  institution.DoesNotExist:
            return JsonResponse({"error": "institution not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request."}, status=400) 

@csrf_exempt
def affiliate(request, data=0):
   
    if request.method == 'POST':
        try:
            affiliatesname = request.POST.get('affiliatesname')
            affiliateslink = request.POST.get('affiliateslink')
            image = request.FILES.get('image')
            print(affiliatesname)
            print(affiliateslink)
            print(image)
            if image:
                imagefile = affiliates(affiliatesname=affiliatesname,affiliateslink=affiliateslink,image=image) 
                imagefile .save()
                
                return JsonResponse({"message": "affiliates uploaded successfully."}, status=201)
        except affiliates.DoesNotExist:
            return JsonResponse({"error":"data not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
        
    elif request.method == 'GET':
        try:
            datadetails = affiliates.objects.all()
            serializer = AffiliatesSerializer(datadetails, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == 'DELETE':
        print(data)
        datadetails = affiliates.objects.get(id=data)
        
        print(datadetails)
        if datadetails.image:
            image_path = os.path.join(settings.MEDIA_ROOT, str(datadetails.image))
            if os.path.exists(image_path):
                os.remove(image_path)
                
        datadetails.delete()
       
        return JsonResponse("Deleted Successfully",safe=False)
    return JsonResponse({"error":"invalid request"},status=400)

@csrf_exempt 
def updateaffiliates(request, data):
    if request.method == 'GET':
        try:
            affiliatesdata = affiliates.objects.get(id=data)
            serializer= AffiliatesSerializer( affiliatesdata)
            
            return JsonResponse(serializer.data,safe=False)
        except affiliates.DoesNotExist:
            return JsonResponse({'error': 'affiliates not found'}, status=404)
        
    elif request.method == 'POST':
        try:
            # Retrieve the existing data based on the provided id  
            affiliatesdata = affiliates.objects.get(id=data)
            
            # Get updated data from the request   
            affiliatesname = request.POST.get('affiliatesname')
            print(affiliatesname)
            affiliateslink = request.POST.get('affiliateslink')
            print(affiliateslink)
            image = request.FILES.get('image')
            print(image )
           
           
            
            # Update data if provided
            if affiliatesname:
                affiliatesdata.affiliatesname = affiliatesname
            if affiliateslink:
                affiliatesdata.affiliateslink = affiliateslink
            if image:
               affiliatesdata.image = image
                     
            # Save the updated data  
            affiliatesdata.save()  
            
            return JsonResponse({"message": "affiliates updated successfully."}, status=200)
        except  affiliates.DoesNotExist:
            return JsonResponse({"error": "affiliates not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request."}, status=400) 

@csrf_exempt
def event(request, data=0):
    if request.method == 'POST':
        try:
            eventname = request.POST.get('eventname')
            eventdate= request.POST.get('eventdate')
            eventtime= request.POST.get('eventtime')
            eventplace= request.POST.get('eventplace')
            state= request.POST.get('stateid')
            district= request.POST.get('districtid')
            eventdescription= request.POST.get('eventdescription')
            eventtype= request.POST.get('eventtype')
            eventbrochure = request.FILES.get('eventbrochure')
    
            print(eventname)
            print(eventdate)
            print(eventtime)
            print(eventplace)
            print(state)
            print(district)
            print(eventdescription)
            print(eventtype)
            print(eventbrochure)
            
            # if eventbrochure:
            imagefile = events(eventname=eventname,eventdate=eventdate,eventtime=eventtime,eventplace=eventplace,state_id=state,district_id=district,eventdescription=eventdescription,eventtype_id=eventtype,eventbrochure=eventbrochure) 
            print(imagefile)
            imagefile .save()
            
            return JsonResponse({"message": "event uploaded successfully."}, status=201)
        except events.DoesNotExist:
            return JsonResponse({"error":"data not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
        
    elif request.method == 'GET':
        try:
            datadetails = events.objects.select_related('state','district','eventtype').all()
            serializer = EventsSerializer(datadetails, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == 'DELETE':
        print(data)
        datadetails = events.objects.get(id=data)
        
        print(datadetails)
        if datadetails.eventbrochure:
            image_path = os.path.join(settings.MEDIA_ROOT, str(datadetails.eventbrochure))
            if os.path.exists(image_path):
                os.remove(image_path)
                
        datadetails.delete()
       
        return JsonResponse("Deleted Successfully",safe=False)
    return JsonResponse({"error":"invalid request"},status=400)

@csrf_exempt
def getdistrictbyid(request,data):
    if request.method == 'GET':
        print(data)
        getdistrict = district.objects.filter(state=data).values('districtid', 'districtname')
        print(getdistrict)
        return JsonResponse(list( getdistrict), safe=False)
    return JsonResponse({"error": "Invalid request."}, status=400)

@csrf_exempt 
def updateevents(request, data):
    if request.method == 'GET':
        try:
            print(data)
            eventdata = events.objects.select_related("state","district","eventtype").filter(id=data).all() 
            serializer= EventsSerializer(eventdata, many=True)
            
            return JsonResponse(serializer.data,safe=False)
        except events.DoesNotExist:
            return JsonResponse({'error': 'event not found'}, status=404)
        
    elif request.method == 'POST':
        try:
            # Retrieve the existing data based on the provided id  
            eventdata = events.objects.get(id=data)
            
            # Get updated data from the request 
            eventname = request.POST.get('eventname')
            print(eventname)  
            eventdate = request.POST.get('eventdate')
            print(eventdate)
            eventtime = request.POST.get('eventtime')
            print(eventtime)
            eventplace = request.POST.get('eventplace')
            print(eventplace)
            state = request.POST.get('state')
            print(state)
            district = request.POST.get('district')
            print(district)
            eventdescription = request.POST.get('eventdescription')
            print(eventdescription)
            eventtype = request.POST.get('eventtype')
            print(eventtype)
            eventbrochure = request.FILES.get('eventbrochure')
            print(eventbrochure )
           
           
            
            # Update data if provided
            if eventname:
                eventdata.eventname = eventname
            if eventdate:
                eventdata.eventdate = eventdate
            if eventtime:
                eventdata.eventtime = eventtime
            if eventplace:
                eventdata.eventplace = eventplace
            if state:
                eventdata.state_id = state
            if district:
                eventdata.district_id= district
            if eventdescription:
                eventdata.eventdescription = eventdescription
            if eventtype:
                eventdata.eventtype_id= eventtype
            if eventbrochure:
               eventdata.eventbrochure = eventbrochure
                     
            # Save the updated data  
            eventdata.save()  
            
            return JsonResponse({"message": "event updated successfully."}, status=200)
        except  events.DoesNotExist:
            return JsonResponse({"error": "event not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request."}, status=400)

@csrf_exempt
def annualreports(request, data=0):
   
    if request.method == 'POST':
        try:
            annualdescription = request.POST.get('annualdescription')
            annualbrochure = request.FILES.get('annualbrochure')
            print(annualdescription)
            print(annualbrochure)
            if annualbrochure:
                annualfile = annualreport(annualdescription=annualdescription,annualbrochure=annualbrochure) 
                annualfile .save()
                
                return JsonResponse({"message": "law uploaded successfully."}, status=201)
        except annualreport.DoesNotExist:
            return JsonResponse({"error":"data not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
        
    elif request.method == 'GET':
        try:
            datadetails = annualreport.objects.all()
            serializer = AnnualreportSerializer(datadetails, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == 'DELETE':
        print(data)
        datadetails = annualreport.objects.get(id=data)
        
        print(datadetails)
        if datadetails.annualbrochure:
            image_path = os.path.join(settings.MEDIA_ROOT, str(datadetails.annualbrochure))
            if os.path.exists(image_path):
                os.remove(image_path)
                
        datadetails.delete()
       
        return JsonResponse("Deleted Successfully",safe=False)
    return JsonResponse({"error":"invalid request"},status=400)

@csrf_exempt 
def updateannualreport(request, data):
    if request.method == 'GET':
        try:
            annualdata = annualreport.objects.get( id=data)
            print("hello")
            serializer= AnnualreportSerializer( annualdata )
            
            return JsonResponse(serializer.data,safe=False)
        except annualreport.DoesNotExist:
            return JsonResponse({'error': 'annual report not found'}, status=404)
        
    elif request.method == 'POST':
        try:
            # Retrieve the existing data based on the provided id  
            annualdata = annualreport.objects.get(id=data)
            
            # Get updated data from the request   
            annualdescription = request.POST.get('annualdescription')
            print(annualdescription)
            annualbrochure = request.FILES.get('annualbrochure')
            print(annualbrochure )
           
           
            
            # Update data if provided
            if annualdescription:
                annualdata.annualdescription = annualdescription
            if annualbrochure:
               annualdata.annualbrochure = annualbrochure
                     
            # Save the updated data  
            annualdata.save()  
            
            return JsonResponse({"message": "annual report updated successfully."}, status=200)
        except  annualreport.DoesNotExist:
            return JsonResponse({"error": "annual report not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request."}, status=400)

@csrf_exempt
def signupp(request, data=0):
    if request.method == 'POST':
        try:
            countrys= request.POST.get('countryid')
            state= request.POST.get('stateid')
            districtid= request.POST.get('districtid')
            institutions = request.POST.get('institution')
            libraryname= request.POST.get('libraryname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            registereddate=timezone.now().date()
    
            # print(displayname)
            # print(state)
            # print(districtid)
            # print(firstname)
            # print(lastname)
            # print(affiliation)
            # print(Linkedln)
            # print(biography)
            # print(ORCID)
            # print(registereddate)
            # print(email)
            # print(password)
            
              # Check the already exist of email and contact
            if subscribe.objects.filter(email=email).exists():
                return JsonResponse({"success":False})
            
            # Create a new Login entry for the user
            subscribereg = subscribe()
            subscribereg.email = email
            subscribereg.password = password  
            subscribereg.role = 'user'  # Or any default role you want
            subscribereg.status = 'active'  # Default status
            subscribereg.save() 
            # print(subscribereg.id)
            signupreg = signup()
            signupreg.country=country.objects.get(countryid=countrys)
            signupreg.state=states.objects.get(stateid=state)
            signupreg.district=district.objects.get(districtid=districtid)
            signupreg.institution=institution.objects.get(id=institutions)
            signupreg.library=libraryname
            signupreg.registereddate=registereddate
            signupreg.subscribe=subscribe.objects.get(id=subscribereg.id)
            
            signupreg.save()

            subscribeObj = signup.objects.last()
            subscribreid = subscribeObj.subscribe_id
            
            
            
            return JsonResponse({"success":True,"id":subscribreid}, status=201)
        except signup.DoesNotExist:
            return JsonResponse({"error":"data not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
        
    elif request.method == 'GET':
        try:
            signupdetails = signup.objects.select_related('state','district','affiliation').all()
            serializer = SignupSerializer(signupdetails, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == 'DELETE':
        print(data)
        signupdetails = signup.objects.get(id=data)
         
        signupdetails.delete()
       
        return JsonResponse("Deleted Successfully",safe=False)
    return JsonResponse({"error":"invalid request"},status=400)

@csrf_exempt
def addmembershiptype(request, data=0):
    if request.method=='POST':
        try:
            membershiptypename = request.POST.get('membershiptypename')
            description = request.POST.get('description')
            print(membershiptypename)
            print(description)
            
            addtype = membershiptype(membershiptypename=membershiptypename, description=description)
            
            addtype.save()
            
    
            return JsonResponse({"message":"Membership type uploaded successfully."}, status=201)
        except membershiptype.DoesNotExist:
            return JsonResponse({"error": "data not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
        
    elif request.method=='GET':
        try:
            typedetails = membershiptype.objects.all()
            serializer = MembershiptypeSerializer(typedetails,many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    elif request.method=='DELETE':
        print(data)
        
        typedetails= membershiptype.objects.get(id=data)
        print(typedetails)                
        typedetails.delete()
        return JsonResponse("Deleted Successfully", safe=False)              
    return JsonResponse({"error":"invalid request"}, status=400)

@csrf_exempt 
def updatemembershiptype(request, data):
    if request.method == 'GET':
        try:
            typedata = membershiptype.objects.get( id=data)
            serializer= MembershiptypeSerializer( typedata)
            
            return JsonResponse(serializer.data,safe=False)
        except membershiptype.DoesNotExist:
            return JsonResponse({'error': 'membership types not found'}, status=404)
        
    elif request.method == 'POST':
        try:
            # Retrieve the existing data based on the provided id  
            typedata = membershiptype.objects.get(id=data)
            
            # Get updated data from the request 
            membershiptypename = request.POST.get('membershiptypename')
            print(membershiptypename)  
            description = request.POST.get('description')
            print(description)
           
            # Update data if provided
            if membershiptypename :
                typedata.membershiptypename  = membershiptypename 
            if description:
                typedata.description = description
                     
            # Save the updated data  
            typedata.save()  
            
            return JsonResponse({"message": "membership types updated successfully."}, status=200)
        except  membershiptype.DoesNotExist:
            return JsonResponse({"error": "membership types not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request."}, status=400) 

@csrf_exempt
def addmembershipsubscription(request, data=0):
    if request.method == 'POST':
        try:
            membershiptype = request.POST.get('membershiptype')
            duration= request.POST.get('duration')
            price= request.POST.get('price')
            description= request.POST.get('description')
           
    
            print(membershiptype)
            print(duration)
            print(price)
            print(description)
        
            membersubs = membershipsubscription(membershiptype_id=membershiptype,duration=duration,price=price,description=description) 
           
            membersubs .save()
            
            return JsonResponse({"message": "membershipsubscription uploaded successfully."}, status=201)
        except membershipsubscription.DoesNotExist:
            return JsonResponse({"error":"data not found"},status=404)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
        
    elif request.method == 'GET':
        try:
            membershipsubscriptiondetails = membershipsubscription.objects.select_related('membershiptype').all()
            serializer = MembershipsubscriptionSerializer(membershipsubscriptiondetails, many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == 'DELETE':
        print(data)
        membershipsubscriptiondetails = membershipsubscription.objects.get(id=data)
        membershipsubscriptiondetails.delete()
       
        return JsonResponse("Deleted Successfully",safe=False)
    return JsonResponse({"error":"invalid request"},status=400)

@csrf_exempt 
def updatemembershipsubscription(request, data):
    if request.method == 'GET':
        try:
            print(data)
            membershipsubscriptiondata = membershipsubscription.objects.select_related("membershiptype").filter(id=data).all() 
            serializer= MembershipsubscriptionSerializer( membershipsubscriptiondata, many=True)
            
            return JsonResponse(serializer.data,safe=False)
        except membershipsubscription.DoesNotExist:
            return JsonResponse({'error': 'membershipsubscription not found'}, status=404)
        
    elif request.method == 'POST':
        try:
            # Retrieve the existing data based on the provided id  
            membershipsubscriptiondata = membershipsubscription.objects.get(id=data)
            
            # Get updated data from the request 
          
            membershiptype = request.POST.get('membershiptype')
            print(membershiptype)
            duration = request.POST.get('duration')
            print(duration)
            price = request.POST.get('price')
            print(price)
            description = request.POST.get('description')
            print(description )
           
            # Update data if provided
           
            if membershiptype:
                membershipsubscriptiondata.membershiptype_id = membershiptype
            if duration:
                membershipsubscriptiondata.duration= duration
            if price:
                membershipsubscriptiondata.price = price
            if description:
                membershipsubscriptiondata.description = description
                     
            # Save the updated data  
            membershipsubscriptiondata.save()  
            
            return JsonResponse({"message": "membershipsubscription updated successfully."}, status=200)
        except  membershipsubscription.DoesNotExist:
            return JsonResponse({"error": "membershipsubscription not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request."}, status=400)

@csrf_exempt
def addeventtype(request, data=0):
    if request.method=='POST':
        try:
            eventtypename = request.POST.get('eventtypename')
            eventtypedescription = request.POST.get('eventtypedescription')
            print(eventtypename)
            print(eventtypedescription)
            
            addeventtype = eventtype(eventtypename=eventtypename, eventtypedescription=eventtypedescription)
            
            addeventtype .save()
            
    
            return JsonResponse({"message":"Eventtypetype uploaded successfully."}, status=201)
        except eventtype.DoesNotExist:
            return JsonResponse({"error": "data not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
        
    elif request.method=='GET':
        try:
            eventtypedetails = eventtype.objects.all()
            serializer = EventtypeSerializer(eventtypedetails,many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    elif request.method=='DELETE':
        print(data)
        
        eventtypedetails= eventtype.objects.get(id=data)
        print(eventtypedetails)                
        eventtypedetails.delete()
        return JsonResponse("Deleted Successfully", safe=False)              
    return JsonResponse({"error":"invalid request"}, status=400)

@csrf_exempt 
def updateeventtype(request, data):
    if request.method == 'GET':
        try:
            eventtypedata = eventtype.objects.get( id=data)
            serializer= EventtypeSerializer(eventtypedata)
            
            return JsonResponse(serializer.data,safe=False)
        except eventtype.DoesNotExist:
            return JsonResponse({'error': 'Event type  not found'}, status=404)
        
    elif request.method == 'POST':
        try:
            # Retrieve the existing data based on the provided id  
            eventtypedata = eventtype.objects.get(id=data)
            
            # Get updated data from the request 
            eventtypename = request.POST.get('eventtypename')
            print(eventtypename)  
            eventtypedescription = request.POST.get('eventtypedescription')
            print(eventtypedescription)
           
            # Update data if provided
            if eventtypename :
                eventtypedata.eventtypename  = eventtypename 
            if eventtypedescription:
                eventtypedata.eventtypedescription = eventtypedescription
                     
            # Save the updated data  
            eventtypedata.save()  
            
            return JsonResponse({"message": "event types updated successfully."}, status=200)
        except  eventtype.DoesNotExist:
            return JsonResponse({"error": "event types not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request."}, status=400) 


        
        
       
   
    
@csrf_exempt
def addpayment(request, data=0):
    if request.method=='POST':
        try:
            member = request.POST.get('member')
            membershiptypes = request.POST.get('membershiptype')
            price = request.POST.get('price')
            payment_date = timezone.now().date()
            payment_status = "Payment Done"
            print(member)
            print(membershiptypes)
            print(price)
            print(payment_date)
            print(payment_status)
            
            addpayment = payment()
            addpayment.member=signup.objects.get(id=member)
            addpayment.membershiptype=membershiptype.objects.get(id=membershiptypes)
            addpayment.price=price
            addpayment.payment_date=payment_date
            addpayment.payment_status=payment_status
            
            addpayment.save()
            
    
            return JsonResponse({"message":"Payment successfully."}, status=201)
        except payment.DoesNotExist:
            return JsonResponse({"error": "data not found."}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
        
    elif request.method=='GET':
        try:
            typedetails = payment.objects.all()
            serializer = PaymentSerializer(typedetails,many=True)
            return JsonResponse(serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

    
@csrf_exempt
def getpayment(request,data=0):
    if request.method=="GET":
        membership=membershipsubscription.objects.get(id=data)
        membershipprice=membership.price
     
        membership_type=membershiptype.objects.get(id=data)
        membershipname=membership_type.membershiptypename
        
        subsriptiondetails={
            'price':membershipprice,
            'name':membershipname
            
        }
        return JsonResponse(subsriptiondetails,safe=False)
    
@csrf_exempt
def getinstitutionbyDistrict(request,data=0):
    if request.method == "GET":
        # try:
            
            institution_list = institution.objects.filter(districts_id=data)
            serializer = InstitutionSerializer(institution_list,many=True)
            return JsonResponse(serializer.data,safe=False)
        # except Exception as e:
        #     return JsonResponse({"error":str(e)},status=500)