"""
Input date and the code will return the week day. A number of different date formats are supported, including 1 December 2018, DEC 1 2019, 1/12/19, 12/1/2019, december the 1st etc.
"""

import re,itertools
weekdays={0:"Monday",1:"Tuesday",2:"It is Wednesday, my dudes",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
month={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:'October',11:"November",12:"December"}
mand=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
npo=input()
repo=npo.replace(", ",".").replace(" ",".").replace("/",".").replace(",",".").split(".")
patday=r"^[0-2][0-9]$|^3[0-1]$|^[1-9]$"
patday2=r"^[0-2][0-9][a-z]{2}$|^3[0-1][a-z]{2}$|^[1-9][a-z]{2}$"
patyear1=r"[0-9]{4}"
patyear2=r"^[0-9]{2}$"
patmon1=r"^0[0-9]$|^1[0-2]$|^[1-9]$"
patmon2=r"^[a-zA-Z]"
monlist1=list(); monlist2=list();daylist=list();yearlist1=list();yearlist2=list();daylist2=[]
dated={patday:daylist,patmon1:monlist1,patmon2:monlist2,patday2:daylist2}
dated2={patyear1:yearlist1,patyear2:yearlist2}
formats=[patday,patmon1,patmon2,patday2]
formatyears=[patyear1,patyear2]
for inpo in repo:
    for form in formats:
        if re.search(form,inpo):
            dated[form].append(inpo)
if monlist2:
    for x in monlist2:
        if x.lower()=="the":
            repo.remove(x)
            continue
        else:
            monlist1=[]
            t=monlist2[0]
            r=t.lower()
            for x in mand:
                if r.startswith(x):
                    z=mand.index(x)
                    monlist1.append(str(int(z)+1))
                    for n, i in enumerate(repo):
                        if i==t:
                            repo[n]=str(int(z)+1)
tepo=[]
tepo.append(repo[0])
tepo.append(repo[2])
for inpo in tepo:
    for form in formatyears:
        if re.search(form,inpo):
            dated2[form].append(inpo)
if daylist2:
    t=daylist2[0][:-2]
    daylist=[]
    daylist.append(t)
    repo.remove(daylist2[0])
    repo.append(daylist[0])
if yearlist1:
    for x in yearlist1:
        if x.lower=="the":
            repo.remove(x)
            continue
        else:
            yearlist2=[]
            yearlist2.append(yearlist1[0])
else:
    if len(yearlist2)==1:
        try:
            daylist.remove(yearlist2[0])
            monlist1.remove(yearlist2[0])
        except:
            pass
    for n,x in enumerate(yearlist2):
        if int(x)<30 and int(x)>9:
            yearlist2[n]="20"+x
        else:
            yearlist2[n]="19"+x

combo=[]
for a in yearlist2:
    for b in monlist1:
        for c in daylist:
            t=[a,b,c]
            if t not in combo:
                combo.append(t)
permo=[]
for x in list(itertools.permutations(repo)):
    r=list(x)
    t=r[0]
    try:
        if int(r[0])<30 and int(r[0])>9:
            r[0]="20"+t
        elif int(r[0])>30 and int(r[0])<100:
            r[0]="19"+t
        permo.append(r)
    except:
        pass
cembo=combo[:]
for x in combo:
    if x not in permo:
        cembo.remove(x)
def weeko(t):
    def leap(r):
        if r%4==0:
            if r%100==0:
                if r%400==0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    daysl=[31,29,31,30,31,30,31,31,30,31,30,31]
    l=0
    if leap(int(t[0])):
        l=sum(daysl[:(int(t[1])-1)])+int(t[2])
    else:
        l=sum(days[:(int(t[1])-1)])+int(t[2])
    r=l
    for x in range(1580,int(t[0])):
        if leap(x):
            r+=366
        else:
            r+=365
    weekdays={-1:"Sunday",0:"Monday",1:"Tuesday",2:"It is Wednesday, my dudes",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday",7:"Monday"}
    ter=(r)%7
    return weekdays[ter]
if len(cembo)==1:
    x=cembo[0]
    print(weeko(x))
else:
    for x in cembo:
        print("If you mean",x[2],month[int(x[1])],x[0],"it is:")
        print(weeko(x))
        print("")