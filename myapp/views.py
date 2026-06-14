import json

import subprocess
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import   login_required
from django.contrib import auth
from .predictionfile import predict
from .predictiogen import predict_gen
from .predictionshape import predict_shape
# from .seg import get_infodetails
from   .models import  *
import datetime
# Create your views here.
def loginTemp(request):
    return  render(request,'loginindex.html')




def loginSend(request):
    username=request.POST["textfield"]
    password=request.POST["textfield2"]
    obj = login_table.objects.filter(username=username,password=password)

    if obj.exists():
        obj1 = login_table.objects.get(username=username, password=password)

        request.session["lid"] = obj1.id
        if obj1.type == 'admin':
            obj1 = auth.authenticate(username='admin', password='admin')
            if obj1 is not None:
                auth.login(request, obj1)
            return redirect('homeAView')
        elif obj1.type == 'researcher':
            obj1 = auth.authenticate(username='admin', password='admin')
            if obj1 is not None:
                auth.login(request, obj1)

            return redirect('HomeRView')

        else:
            return HttpResponse('''<script>alert('Invalid user');window.location="loginTemp"</script>''')
    else:
        return HttpResponse('''<script>alert('Invalid user');window.location="loginTemp"</script>''')


def logout(request):
    auth.logout(request)
    return redirect('/')
    # return  render(request,'adminindex.html')


@login_required(login_url='/')
def complaintView(request):
    obj=Complaint_table.objects.select_related('USER').all()
    return render(request,'Admin/complaint.html',{'details':obj})


@login_required(login_url='/')

def feedbackView(request):
    obj=Feedback_table.objects.select_related('USER').all()
    return render(request,'Admin/feedback.html',{'feed':obj})
@login_required(login_url='/')

def blockView(request):
    person = User_table.objects.all()
    return render(request, 'Admin/block.html', {'person': person})

def blockUser(request,id):
    loginobj=login_table.objects.get(id=id)
    loginobj.type='block'
    loginobj.save()
    return HttpResponse('''<script>alert('Blocked');window.location="/blockView"</script>''')

def unblockUser(request,id):
    loginobj=login_table.objects.get(id=id)
    loginobj.type='user'
    loginobj.save()
    return HttpResponse('''<script>alert('Unblocked');window.location="/blockView"</script>''')

def replyView(request,id):
    request.session["cid"]=id
    return render(request,'Admin/reply.html')
def replySend(request):
    cid=request.session["cid"]
    reply=request.POST["textarea"]
    obj=Complaint_table.objects.get(id=cid)
    obj.reply=reply
    obj.save()
    return HttpResponse('''<script>alert('success');window.location="complaintView"</script>''')

@login_required(login_url='/')

def verifyView(request):
    obj = Research_table.objects.all()
    return render(request, 'Admin/verify.html', {'verify': obj})
def acceptResearcher(request,id):
    loginobj=login_table.objects.get(id=id)
    loginobj.type='accept'
    loginobj.save()
    return HttpResponse('''<script>alert('accepted');window.location="/verifyView"</script>''')
def rejectResearcher(request,id):
    loginobj=login_table.objects.get(id=id)
    loginobj.type='reject'
    loginobj.save()
    return HttpResponse('''<script>alert('rejected');window.location="/verifyView"</script>''')

@login_required(login_url='/')

def viewdetails(request):
    obj = Bdetails_table.objects.all()
    return render(request, 'Admin/viewdetails.html',{"val":obj})

def deletedetails(request,id):
    obj=Bdetails_table.objects.get(id=id)
    obj.delete()
    return HttpResponse('''<script>alert('deleted');window.location="/viewdetails"</script>''')

def editdetails(request,id):
    request.session["iid"]=id
    obj = Bdetails_table.objects.get(id=id)
    return render(request,'Admin/editdetails.html',{"data":obj})

def editdetails_POST(request):
    Image = request.FILES["file"]
    Common_Name = request.POST["textfield"]
    Scientific_Name = request.POST["textfield9"]
    Kingdom = request.POST["textfield2"]
    Phylum = request.POST["textfield3"]
    Class = request.POST["textfield4"]
    Order = request.POST["textfield5"]
    Family = request.POST["textfield6"]
    Genus = request.POST["textfield7"]
    Species = request.POST["textfield8"]
    LifeCycle = request.POST["textarea"]
    obj = Bdetails_table.objects.get(id=request.session["iid"])
    obj.Image = Image
    obj.Common_Name = Common_Name
    obj.Scientific_Name = Scientific_Name
    obj.Kingdom = Kingdom
    obj.Phylum = Phylum
    obj.Class = Class
    obj.Order = Order
    obj.Family = Family
    obj.Genus = Genus
    obj.Species = Species
    obj.LifeCycle = LifeCycle
    obj.save()
    return HttpResponse('''<script>alert('Details Edited ');window.location="viewdetails"</script>''')

@login_required(login_url='/')

def uploaddetailsView(request):
    return render(request, 'Admin/Bdetails.html')


def uploaddetails(request):
    Image = request.FILES['file']
    Common_Name = request.POST["textfield"]
    Scientific_Name = request.POST["textfield9"]

    Kingdom = request.POST['textfield2']
    Phylum = request.POST['textfield3']
    Class = request.POST['textfield4']
    Order = request.POST['textfield5']
    Family = request.POST['textfield6']
    Genus = request.POST['textfield7']
    Species = request.POST['textfield8']
    LifeCycle = request.POST['textarea']

    fn = FileSystemStorage()
    fs = fn.save(Image.name, Image)
    ob = Bdetails_table()

    ob.Image = fs
    ob.Common_Name = Common_Name
    ob.Scientific_Name = Scientific_Name

    ob.Kingdom = Kingdom
    ob.Phylum = Phylum
    ob.Class = Class
    ob.Order = Order
    ob.Family = Family
    ob.Genus = Genus
    ob.Species = Species
    ob.LifeCycle = LifeCycle
    ob.save()
    return HttpResponse('''<script>alert('findings uploaded');window.location="viewdetails"</script>''')




def registerationRView(request):
    obj = Research_table.objects.all()
    return render(request, 'Researcher/../templates/RRegister.html', {'profile': obj})
def registerview(request):
    return render(request, 'RRegister.html')

def registerationRSend(request):
    name = request.POST["textfield"]
    place = request.POST["textfield2"]
    post = request.POST["textfield4"]
    pin = request.POST["textfield3"]
    phone = request.POST["textfield5"]
    username = request.POST["textfield6"]
    password = request.POST["textfield7"]

    if login_table.objects.filter(username=username).exists():
        return HttpResponse('''<script>alert('The username already existed');</script>''')

    objlog = login_table(username=username, password=password, type='researcher')
    objlog.save()

    obR = Research_table(LOGIN=objlog, name=name, place=place, post=post, pin=pin, phone=phone)
    obR.save()

    return HttpResponse('''<script>alert('registered');window.location="loginTemp"</script>''')



@login_required(login_url='/')


def HomeRView(request):
    return render(request,'Researcher/researcherindex.html')

@login_required(login_url='/')

def homeAView(request):
        # return render(request, 'Admin/HomeA.html')
    return render(request, 'Admin/adminindex_main.html')

@login_required(login_url='/')

def myprofileView(request):
    obj=Research_table.objects.get(LOGIN__id=request.session['lid'])
    return render(request, 'Researcher/myprofile.html',{'profile':obj})

def updateprofile(request):
    name=request.POST["textfield"]
    place=request.POST["textfield2"]
    post=request.POST["textfield3"]
    pin=request.POST["textfield4"]
    phone=request.POST["textfield5"]
    ob=Research_table.objects.get(LOGIN__id=request.session['lid'])
    ob.name=name
    ob.place=place
    ob.post=post
    ob.pin=pin
    ob.phone=phone
    ob.save()
    return HttpResponse('''<script>alert('profile updated');window.location="myprofileView"</script>''')


@login_required(login_url='/')

def passwordView(request):
        obj=Research_table.objects.get(LOGIN__id=request.session['lid'])
        return render(request,'Researcher/password.html',{'password':obj})

def updatepassword(request):
    currentpassword=request.POST["textfield"]
    newpassword=request.POST["textfield2"]
    confirmpassword=request.POST["textfield3"]
    ob = login_table.objects.get(id=request.session['lid'])
    if ob.password == currentpassword:
        if newpassword==confirmpassword:
            ob.password=newpassword
            ob.save()
            return HttpResponse('''<script>alert('password updated');window.location="HomeRView"</script>''')
        else:
            return HttpResponse('''<script>alert('new password and confirm password are not equal');window.location="HomeRView"</script>''')
    else:
        return HttpResponse('''<script>alert('old password not equal to current password');window.location="HomeRView"</script>''')


@login_required(login_url='/')

def viewfindings(request):
    obj = Findings_table.objects.filter(RESEARCHER__LOGIN__id=request.session['lid'])
    return render(request,'Researcher/view findings.html', {'val': obj})

def deletefindings(request,id):
    obj=Findings_table.objects.get(id=id)
    obj.delete()
    return HttpResponse('''<script>alert('deleted');window.location="/viewfindings"</script>''')



@login_required(login_url='/')

def uploadfindingsView(request):
    return render(request, 'Researcher/uploadfindings.html')


def uploadfindings_post(request):
    name=request.POST['textfield']
    find=request.POST['textarea']
    image=request.FILES['file']
    fn=FileSystemStorage()
    fs=fn.save(image.name,image)
    ob=Findings_table()
    ob.RESEARCHER=Research_table.objects.get(LOGIN__id=request.session['lid'])
    ob.findings=find
    ob.name=name
    ob.image=fs
    ob.save()
    return HttpResponse('''<script>alert('findings uploaded');window.location="viewfindings"</script>''')














# -----------------------------------------
def logincode(request):
    print(request.POST)
    un = request.POST['username']
    pwd = request.POST['password']

    a = login_table.objects.filter(username=un, password=pwd)
    if a.exists():
        ob = login_table.objects.get(username=un, password=pwd)
        data = {"task": "valid", "lid": ob.id, "type": ob.type}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    else:
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)





    # print(un, pwd)
    # try:
    #     ob = login_table.objects.get(username=un, password=pwd)
    #
    #     if ob is None:
    #         data = {"task": "invalid"}
    #     else:
    #         print("in user function")
    #         data = {"task": "valid", "lid": ob.id,"type":ob.type}
    #     r = json.dumps(data)
    #     print(r)
    #     return HttpResponse(r)
    # except:
    #     data = {"task": "invalid"}
    #     r = json.dumps(data)
    #     print(r)
    #     return HttpResponse(r)

#-------------------------
def registercode(request):
     print(request.POST)
     name = request.POST['name']
     place = request.POST['place']
     post = request.POST['post']
     pin = request.POST['pin']
     phone = request.POST['phone']
     username = request.POST['uname']
     password  = request.POST['password']
     print(name,place,post,pin,phone,username,password)

     if login_table.objects.filter(username=username).exists():
         return JsonResponse({"status": "not ok"})

     objlog = login_table(username=username, password=password, type='user')
     objlog.save()

     obU = User_table(LOGIN=objlog, name=name, place=place, post=post, pin=pin, phone=phone)
     obU.save()

     return JsonResponse({"status":"ok"})
#---------------------------------
def complaintcode(request):
    print(request.POST)
    complaint = request.POST['complaint']
    lid = request.POST['lid']
    date = datetime.datetime.now().date()
    reply = "pending"


    objc = Complaint_table( complaint=complaint, date=date, reply=reply,USER=User_table.objects.get(LOGIN=lid))
    objc.save()
    return JsonResponse({"status":"ok"})
#--------------------------
def complaintViewcode(request):
    lid = request.POST["lid"]

    obj = Complaint_table.objects.filter(USER__LOGIN=lid)
    ls=[]
    for i in obj:
        r={"id":i.id,"complaint":i.complaint,"date":str(i.date),"reply":i.reply}
        ls.append(r)

    print(ls)
    return JsonResponse({"status":"ok","data":ls})
#----------------------------
def deletecomplaintcode(request):
    ccid = request.POST["cid"]
    obj = Complaint_table.objects.get(id=ccid)
    obj.delete()
    return JsonResponse({"status": "ok"})

#---------------------------
def changepassword(request):
    old = request.POST['old']
    new = request.POST['new']
    confirm = request.POST['confirm']
    lid = request.POST['lid']

    if login_table.objects.filter(id=lid,password=old).exists():
        if new == confirm:
            login_table.objects.filter(id=lid, password=old).update(password=confirm)
            return JsonResponse({"status": "ok"})
        else:
            return JsonResponse({"status": "not ok"})
    else:
        return JsonResponse({"status": " not ok"})


#-----------------------
def updateprofilecode(request):
    print(request.POST)
    name = request.POST["name"]
    place = request.POST["place"]
    post = request.POST["post"]
    pin = request.POST["pin"]
    phone = request.POST["phone"]
    lid = request.POST["lid"]
    ob = User_table.objects.get(LOGIN__id=lid)
    ob.name = name
    ob.place = place
    ob.post = post
    ob.pin = pin
    ob.phone = phone
    ob.save()
    return JsonResponse({"status":"ok"})
#---------------
def viewprofilecode(request):
    lid = request.POST["lid"]
    obj = User_table.objects.get(LOGIN__id=lid)
    print(obj,"kkkkkkkk")
    return JsonResponse({"status":"ok","name":obj.name,"place":obj.place,"post":obj.post,"pin":str(obj.pin),"phone":str(obj.phone)})

#----------------------
def editprofilecode(request):
    print(request.POST)
    id = request.POST["lid"]
    name = request.POST["name"]
    phone = request.POST["phone"]
    place = request.POST["place"]
    post = request.POST["post"]
    pin = request.POST["pin"]
    print(name, place, post, pin, phone)
    obj = User_table.objects.get(LOGIN__id=id)
    obj.name = name
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.phone = phone
    obj.save()
    return JsonResponse({"status":"ok"})


#----------------
def findingViewcode(request):
    # lid = request.POST["lid"]
    obj = Findings_table.objects.all()
    ls = []
    for i in obj:
        r = {"id": i.id, "image": i.image.url[1:], "findings": i.findings, "name": i.name}
        ls.append(r)
    print(ls)
    return JsonResponse({"status": "ok", "data": ls})
#------------------------------
def feedbackcode(request):
    print(request.POST)
    feedback = request.POST['feedback']
    date = datetime.datetime.now().date()
    rating = request.POST['rating']
    lid=request.POST["lid"]

    objf = Feedback_table( feedback=feedback, date=date, rating=rating,USER=User_table.objects.get(LOGIN=lid))
    objf.save()
    return JsonResponse({"status":"ok"})
#-----------------------------
def feedbackViewcode(request):
    # lid = request.POST["lid"]

    obj = Feedback_table.objects.all()
    ls = []
    for i in obj:
        r = {"id": i.id, "feedback": i.feedback, "date": i.date, "rating": i.rating}
        ls.append(r)
    return JsonResponse({"status": "ok", "data": ls})
#---------------------------
def detailsViewcode(request):

    obj = Bdetails_table.objects.all()
    ls = []
    for i in obj:
        r = {"id": i.id, "Image": i.Image.url[1:], "Common_Name": i.Common_Name,"Scientific_Name": i.Scientific_Name, "Kingdom": i.Kingdom , "Phylum": i.Phylum , "Class": i.Class , "Order": i.Order ,"Family": i.Family ,"Genus": i.Genus,"Species": i.Species, "LifeCycle": i.LifeCycle}
        ls.append(r)
    print(ls)
    return JsonResponse({"status": "ok", "data": ls})

#-----------------------------
def detailsViewcodeMore(request):
    id = request.POST['id']
    obj = Bdetails_table.objects.get(id=id)
    return JsonResponse({
        'Common_Name':obj.Common_Name,
        'Scientific_Name': obj.Scientific_Name,
        'Kingdom':obj.Kingdom,
        'Phylum':obj.Phylum,
        'Class':obj.Class,
        'Order':obj.Order,
        'Family':obj.Family,
        'Genus':obj.Genus,
        'Species':obj.Species,
        'Life Cycle':obj.LifeCycle,
        'Image':request.build_absolute_uri(obj.Image.url),
    })
#-----------------------------
def detailsViewcodeMore1(request):
    print(request.POST)
    id = request.POST['id']
    obj = Bdetails_table.objects.get(Scientific_Name=id)
    return JsonResponse({
        'Common_Name':obj.Common_Name,
        'Scientific_Name': obj.Scientific_Name,
        'Kingdom':obj.Kingdom,
        'Phylum':obj.Phylum,
        'Class':obj.Class,
        'Order':obj.Order,
        'Family':obj.Family,
        'Genus':obj.Genus,
        'Species':obj.Species,
        'Life Cycle':obj.LifeCycle,
        'Image':request.build_absolute_uri(obj.Image.url),
    })
#------------------------------
def researcherViewcode(request):

    obj = Research_table.objects.all()
    ls = []
    for i in obj:
        r = {"id": i.LOGIN.id, "name": i.name, "phone": i.phone, "place": i.place, "post": i.post,
             "pin": i.pin}
        ls.append(r)
    return JsonResponse({"status": "ok", "data": ls})

def chat_send(request):
    FROM_id=request.POST['from_id']
    TOID_id=request.POST['to_id']
    msg=request.POST['message']

    from  datetime import datetime
    c=Chat()
    c.FROMID_id=FROM_id
    c.TOID_id=TOID_id
    c.message=msg
    c.date=datetime.now()
    c.save()
    return JsonResponse({'status':"ok"})

def chat_view(request):
    fromid = request.POST["from_id"]
    toid = request.POST["to_id"]

    res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid)).order_by('id')
    l = []

    for i in res:
        time_str = i.date.strftime("%I:%M %p")
        l.append({
            "id": i.id,
            "msg": i.message,
            "from": i.FROMID_id,
            "date": i.date.strftime("%Y-%m-%d"),
            "time": time_str,
            "to": i.TOID_id
        })

    return JsonResponse({"status": "ok", 'data': l})

#---------------------------------------
def scan(request):
    Image = request.FILES["file"]
    fs=FileSystemStorage()
    fn=fs.save(Image.name,Image)
    res,p=predict(r"C:\Users\user\Desktop\myproject final1\myproject\media/"+fn)
    p=round(float(p)*100,2)

    print("--------------",res,"---lll",p)
    if res!='Invalid' and p>60:




        res=res.split("#")
        res1=predict_gen(r"C:\Users\user\Desktop\myproject final1\myproject\media/"+fn)
        result2 = subprocess.run(
            [r'C:\Users\user\AppData\Local\Programs\Python\Python36\python.exe',
             r'C:\Users\user\Desktop\myproject final1\myproject\myapp\seg.py',r"C:\Users\user\Desktop\myproject final1\myproject\media/"+fn]
        )

        # res2=get_infodetails(r"C:\PycharmProjects\PycharmProjects\myproject\media/"+fn)
        print(res,"----","res1==",res1,"====",result2)
        f = open("resfile.txt", "r")
        d=f.read()
        print(d,"===============")
        return JsonResponse({"task":res[0],"task1":res1,"fn":fn,"s":d,"sh":res[1],"p":p})
    else:
        return JsonResponse({"task": "invalid","fn":fn})
# "====================chat with user ========================"

def chatwithuser(request):
    ob = User_table.objects.all()
    return render(request,"Researcher/fur_chat.html",{'val':ob})



def chatview(request):
    ob = User_table.objects.all()
    d=[]
    for i in ob:
        r={"name":i.name,'photo':i.name,'email':i.place,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)




def coun_insert_chat(request,msg,id):
    print("===",msg,id)
    ob=Chat()
    ob.FROMID=login_table.objects.get(id=request.session['lid'])
    ob.TOID=login_table.objects.get(id=id)
    ob.message=msg
    ob.date=datetime.datetime.now().strftime("%Y-%m-%d")
    ob.save()

    return JsonResponse({"task":"ok"})
    # refresh messages chatlist



def coun_msg(request,id):

    ob1=Chat.objects.filter(FROMID__id=id,TOID__id=request.session['lid'])
    ob2=Chat.objects.filter(FROMID__id=request.session['lid'],TOID__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.FROMID.id,"msg":i.message,"date":i.date,"chat_id":i.id})

    obu=User_table.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.name,"photo":obu.name,"user_lid":obu.LOGIN.id})

#--------------------------

def machinelcode(request):
    # id = request.POST['id']
    # obj = Bdetails_table.objects.get(id=id)
    return JsonResponse({
        'Name':"danaus",
        'Gender':"female",
        'WingShape':"",
        'WingColor':"blue",
        'BodyShape':"oval",
        'Texture':"dusted",
        'Result':"100",
        'Image':"null",
    })
