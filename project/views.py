from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from .forms import *
from django.db.models import Q
from django.db.models import Max,Count,Avg


# from passlib.hash import pbkdf2_sha256
# from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# def get(self, request,a,b): url dispatcher class based views

# check_password = pbkdf2_sha256.hash(password, rounds=20000, salt_size=16)
#             dec_password = pbkdf2_sha256.verify(password, check_password)


class Home(View):
    def get(self, request):
        return render(request,'index.html')

class Home2(View):    
    # login_url = '/login' 
    def get(self, request):
        if 'username' in request.session:
            current_user = request.session['username']
            user = Users.objects.filter(username=current_user)

        # else:
        #     login_url = '/login'
        #     redirect_field_name = 'next'
        #     raise_exception = True   

        return render(request,'index1.html')

class About(View):
    def get(self, request):
        return render(request,'about.html')

class Services(View):
    def get(self, request):
        return render(request,'services.html')

class Gallery(View):
    def get(self, request):
        return render(request,'gallery.html')

class Team(View):
    def get(self, request):
        return render(request,'team.html')

class Contact(View):
    def get(self, request):
        return render(request,'contact.html')

class LoginSuccess(View):
    def get(self, request):
        return render(request,'login-success.html')

class LoginFailed(View):
    def get(self, request):
        return render(request,'login-failed.html')
        
class Signup(View):
    def get(self, request):
        return render(request,'signup.html')

    def post(self, request):
        uform = UserForm(request.POST)

        if uform.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            contact = request.POST.get("contact")
            address = request.POST.get("address")
            username = request.POST.get("username")
            password = request.POST.get("password")

            # enc_password = pbkdf2_sha256.encrypt(password, rounds=12000, salt_size=16)
            # tpassword = enc_password

            uform = Users(name=name, email=email, contact=contact, address=address, username=username,
                password=password)

            uform.save()
            print('napindot')
            return redirect('project:home_view')

        else:
            print(uform.errors)
            return HttpResponse('not valid')

class UsersDashboard(View):

    def get(self, request):
        
        users = Users.objects.all()
        context = {
            'users' : users,
                    
        }
        return render(request,'user-dashboard.html', context)

    def post(self, request):
        if request.method == 'POST':    
            if 'btnUpdateUsers' in request.POST: 
                print('update profile button clicked')
                uid = request.POST.get("users-id")            
                name = request.POST.get("users-name")
                email = request.POST.get("users-email")
                contact = request.POST.get("users-contact")
                address = request.POST.get("users-address")
                username = request.POST.get("users-username")
                password = request.POST.get("users-password")
                print(name)
                update_users = Users.objects.filter(uid = uid).update(name = name, email = email, contact = contact, address = address, username = username, password = password)
                print(update_users)
                print('profile updated')
            
            elif 'btnDelete' in request.POST:
                uid = request.POST.get("uuser-id")
                users = Users.objects.filter(uid=uid).delete()
                print('record deleted')

        return redirect('project:user-dashboard_view')


class RoomDashboard(View):

    def get(self, request):
        # username = "Psalm"
        # gh = Users.objects.filter(username = username)
        mr = MeetingRooms.objects.all()
        rr = Reservation.objects.all()

        # if 'date' in request.session:
        #     current_date = request.session['date']
        #  
        #     vacant = MeetingRooms.objects.filter(~Q(start_date=current_date)).filter(is_available=True)

            

        # po = request.POST.get("update-room")
        # yu = Reservation.objects.get(room=po)
        # op = MeetingRooms.objects.filter(room_id=yu)

        context = {
                     #name that we want to use
            'mr' : mr,
            'rr' : rr,
            }

        return render(request,'room-dashboard.html',context)


    def post(self,request):
        if request.method == 'POST':

            if 'btnAddRoom' in request.POST: 
                mform = MeetingForm(request.POST)

                if mform.is_valid():

                    rname = request.POST.get("add-room")
                    if (request.POST.get("isAvailable") == "on"):
                        isavailable = True
                    else:
                        isavailable = False

                    # isAvailable = request.POST.get("isAvailable") == True

                    print(isavailable)

                    addRom = MeetingRooms(meeting_room=rname, isAvailable=isavailable)
                    addRom.save()  
                    print(addRom)


                    return redirect('project:room-dashboard_view') 

            elif 'btnUpdateRoom' in request.POST:  
                rid = request.POST.get("update-rid")
                name = request.POST.get("update-username")
                email = request.POST.get("update-email")
                contact = request.POST.get("update-contact")
                timein = request.POST.get("update-timein")
                timeout = request.POST.get("update-timeout")
                date = request.POST.get("update-date")
                numpersons = request.POST.get("update-numpersons")
                room = request.POST.get("update-room")   

                update_reservation = Reservation.objects.filter(rid = rid).update(username=name, email=email, contact=contact,
                    date=date, timein=timein, timeout=timeout, numpersons=numpersons, room=room)
                print(update_reservation)
                print('profile updated')  

            elif 'btnDeleteRoom' in request.POST:
                rid = request.POST.get("delete-rid")
                agh = request.POST.get('setroomavail')
                ert = request.POST.get('date')
                users = Reservation.objects.filter(rid=rid).delete()
                
                ava = MeetingRooms.objects.filter(mid=agh).update(isAvailable = True, start_date = None)
                print(ava)
                print('record deleted')






        return redirect('project:room-dashboard_view')

class RoomSearch(View):
    def get(self, request):

        
        #most = Reservation.objects.all().annotate(Max('room_id')).aggregate(Count('room_id', distinct=False)).filter(room_id__count__gt=1)
        #most = Reservation.objects.aggregate(Max(Count('room_id', distinct=False)))[:1]
        #most = Reservation.objects.filter(room='1')
        
        #most = Reservation.objects.values('room_id').annotate(count=Count('room_id')).annotate(maxx=Max('count')

       
        #most = Reservation.objects.values('room_id').annotate(Count('room_id')).order_by().filter(room_id__count__gt=1).latest('room_id')
        #most = Reservation.objects.values('room').annotate(Count('room')).latest('room_id')
        # mtt = Reservation.objects.filter(room__in=[item['room'] for item in most])

        

        #Book.objects.annotate(num_authors=Count('authors')).aggregate(Avg('num_authors'))
        #most = Reservation.objects.raw('SELECT room_id, COUNT(room_id) AS `value_occurrence` FROM project_reservation GROUP BY room_id ORDER BY `value_occurrence` DESC LIMIT 1')
        most = Reservation.objects.values('room_id').annotate(count=Count('room_id')).order_by().latest('count')
        print(most['room_id'])
        print(most['count'])

        roof = most['room_id']
        print(roof)
        yot = MeetingRooms.objects.filter(mid=roof) 
        print(yot) 

        searchVacant = request.GET.get('search')

        if 'searchVacant' in request.GET:
            vacant = MeetingRooms.objects.filter(Q(isAvailable=True) & ~Q(start_date__iexact=searchVacant))
            #op = Reservation.objects.filter('Meeting Room').values('room')
            
            #vacant = MeetingRooms.objects.filter(isAvailable=True)
            #vacant = MeetingRooms.objects.exclude(start_date=searchVacant).filter(isAvailable=True)
            #vacant = MeetingRooms.objects.filter(start_date=searchVacant).filter(isAvailable=True)
            #vacant = MeetingRooms.objects.exclude(isAvailable=True).filter(start_date__icontains=searchVacant)
            #vacant = MeetingRooms.objects.exclude(start_date__icontains=searchVacant, isAvailable=False)
        else:
            vacant = MeetingRooms.objects.filter(isAvailable=True)         
            # return render(request,'room-dashboard2.html')
        

        context = {
                    'vacant': vacant,
                    'most'  : most,
                    'yot'   : yot,
                }

        return render(request,'room-dashboard2.html',context)  

    
         
class RoomReservation(View):
    def get(self, request):
        if 'usern' in request.session:

            current_user = request.session['usern']
            gh = Users.objects.filter(username = current_user)

            mr = MeetingRooms.objects.all()
            rr = Reservation.objects.all()

            context = {
                'gh' : gh,           #name that we want to use
                'mr' : mr,
                'rr' : rr,
                }

            return render(request,'room-reservation.html', context)

    def post(self, request):
        rform = ReservationForm(request.POST)
        mform = MeetingForm(request.POST)

        if rform.is_valid() and mform.is_valid():
            name = rform.cleaned_data.get("username")
            email = request.POST.get("email")
            contact = request.POST.get("contact")
            timein = request.POST.get("timein")
            timeout = request.POST.get("timeout")
            date = request.POST.get("date")
            numpersons = request.POST.get("numpersons")
            room = rform.cleaned_data.get("room")
            # doctor_id = patForm.cleaned_data.get("Doctor")

            rform = Reservation(username=name, email=email, contact=contact, timein=timein, timeout=timeout,
                date=date, numpersons=numpersons, room=room)

            # datee = request.POST.get("date")
            rooms= request.POST.get("room")
            mform = MeetingRooms.objects.filter(mid=rooms).update(isAvailable=False, start_date=date)

            #yu = MeetingRooms(rid=room, is_available=False, start_date= date)
            rform.save()
            print(mform)
            
            return redirect('project:home2_view')

        else:
            print(rform.errors)
            print(mform.errors)
            return HttpResponse('not valid')



class DisplayUserReservation(View):

    def get(self, request):
        if 'usern' in request.session:
            current_user = request.session['usern']
            kl = Reservation.objects.filter(username=current_user)

            context={'kl' : kl,
                }
            return render(request,'usersreservation.html', context)
            
    def post(self, request):
        if request.method == 'POST':
            if 'btnDeleteReservation' in request.POST:
                rid = request.POST.get("delete-riddd")
                delete_reservation = Reservation.objects.filter(rid=rid).delete()
                print(delete_reservation)


        return redirect('project:user-reservation_view')



class UpdateUser(View):
    """docstring for ClassName"""
    def get(self, request):
        if 'usern' in request.session:
            current_user = request.session['usern']
            jp = Users.objects.filter(username=current_user)

            context={'jp':jp,
                }
        return render(request,'updateuser.html',context)

    def post(self,request):
        if request.method == 'POST':
            if 'btnUpdate' in request.POST:
                uid = request.POST.get("update-uid")
                name = request.POST.get("update-name")
                email = request.POST.get("update-email")
                contact = request.POST.get("update-contact")
                address = request.POST.get("update-address")
                username = request.POST.get("update-username")
                password = request.POST.get("update-password")
                
                update_account = Users.objects.filter(uid=uid).update(name=name, email=email, contact=contact,
                    address=address, username=username, password=password)
                print(update_account)
                # return redirect('project:updateuser_view')

            elif 'btnDelete' in request.POST:
                uidd = request.POST.get("update-uid")

                delete_account = Users.objects.filter(uid=uidd).delete()
                print(delete_account)
                return redirect('project:home_view')

        return redirect('project:updateuser_view')
      

class LoginPage(View):
    def get(self, request):
        return render(request,'login.html')

    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            check_user = Users.objects.filter(username=username, password=password)
            check_admin = Admin.objects.filter(username='admin', password='admin')

            if check_user:
                request.session['usern'] = username
                if Users.objects.filter(username=username).count()>0: 
                        return redirect('project:loginsuccess_view')

            if check_admin:
                request.session['admin'] = username
                if Admin.objects.filter(username=username).count()>0:    
                    return redirect('project:user-dashboard_view')
            
            else:   
                return redirect('project:loginfailed_view')
        else:   
            return render(request,"signup.html")
