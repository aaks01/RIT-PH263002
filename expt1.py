#Experiment No. 1
#look up corresponding pdf for experiment details
def vernier_callipers () :
    print("Vernier Callipers")
    unit=str(input("Enter Unit used : "))
    lc=float(input("Enter Least Count  ("+unit+") : "))
    ze=int(input("Mention the division of vernier scale coinciding with main scale on zeroing : "))
    error=0.0
    if ze!=0 :
        sign=str(input("Is vernier zero left or right to main scale zero (L/R) ? : "))
        if sign=="L" :
            error=ze*lc
        elif sign=="R" :
            error=-1*ze*lc
    n=int(input("Enter Number of Readings to be taken : "))
    i=0
    tr=0
    while i<n :
        print("Reading "+str(i+1))
        msr=float(input("Enter MSR ("+unit+"): "))
        vsc=int(input("Enter coinciding vernier division : "))
        tr+=msr+(vsc*lc)+error
        i+=1
    print("Mean reading ("+unit+") : "+str(tr/n))
def screw_gauge () :
    print("Screw Gauge")
    unit=str(input("Enter Unit used : "))
    lc=float(input("Enter Least Count  ("+unit+") : "))
    thsd=int(input("Enter No. of divisions in Head Scale : "))
    ze=int(input("Mention the division of head scale coinciding with pitch scale on zeroing : "))
    if ze!=0 :
        sign=str(input("Is head scale zero up or down to pitch scale zero (U/D) ? : "))
        if sign=="D" :
            error=-1*ze*lc
        elif sign=="U" :
            error=(thsd-ze)*lc
    n=int(input("Enter Number of Readings to be taken : "))
    i=0
    tr=0
    while i<n :
        print("Reading "+str(i+1))
        psr=float(input("Enter PSR ("+unit+"): "))
        hsd=int(input("Enter coinciding headscale division : "))
        tr+=psr+(hsd*lc)+error
        i+=1
    print("Mean reading ("+unit+") : "+str(tr/n))
option=int(input("Enter 1 for vernier experiment and 2 for screw gauge experiment : "))
if option==1 :
    vernier_callipers()
elif option==2 :
    screw_gauge()
else :
    print("Wrong Option !")