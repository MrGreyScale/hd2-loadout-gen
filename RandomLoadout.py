#created by @_greyscale_ on discord
#this program will randomize loadout
from random import randint

#Variables
pti = int
sti = int
tti = int
ati = int

Primary_Index = int
Secondary_Index = int
Throwable_Index = int
AP_Index = int

Primary = "" 
Secondary = ""
Throwable = ""
ArmorType=""
ArmorPassive=""


cls = "\n" * 100
d = "=" * 50

#Primaries
ARs = ['AR-23 Liberator','AR-23C Liberator Concussive', 'StA-52 Assault Rifle', 'AR-23A Liberator Carbine','AR-61 Tenderizer','AR-32 Pacifier','AR-23P Liberator Penetrator','BR-14 Adjudicator']
MRs = ['R-2 Amendment','R-63 Diligence','R-2124 Constitution','R-6 Deadeye','R-63CS Diligence Counter Sniper']
SMG = ['MP-98 Knight','StA-11 SMG','SMG-37 Defender','SMG-72 Pummeler','SMG-32 Reprimand']
SG = ["SG-8 Punisher","SG-451 Cookout","SG-225 Breaker","SG-225SP Breaker Spray & Pray","SG-225IE Breaker Incendiary","SG-8S Slugger","SG-20 Halt"]
EXP = ["CB-9 Exploding Crossbow","R-36 Eruptor"]
EB = ["LAS-5 Scythe","LAS-16 Sickle","PLAS-39 Accelerator Rifle","SG-8P Punisher Plasma","ARC-12 Blitzer","PLAS-1 Scorcher","PLAS-101 Purifier","LAS-17 Double-Edge Sickle"]
P_SPEC = ["JAR-5 Dominator","FLAM-66 Torcher"]

#Secondaries
PISTOL = ["P-2 Peacemaker","P-19 Redeemer","P-113 Verdict","P-92 Warrant","P-4 Senator"]
MELEE = ["CQC-19 Stun Lance","CQC-30 Stun Baton","CQC-5 Combat Hatchet","CQC-2 Saber"]
S_SPEC = ["P-11 Stim Pistol","SG-22 Bushwhacker","LAS-7 Dagger","LAS-58 Talon","GP-31 Grenade Pistol","PLAS-15 Loyalist","P-72 Crisper","GP-31 Ultimatum"]

#Throwables
STANDARD = ["TED-63 Dynamite","G-6 Frag","G-10 Incendiary","G-12 High Explosive"]
T_SPEC = ["G-3 Smoke","G-13 Incendiary Impact","G-142 Pyrotech","K-2 Throwing Knife","G-16 Impact","G-50 Seeker","G-109 Urchin","G-23 Stun","G-4 Gas","G-123 Thermite"]

#Armor Passives
Passives = ["Advanced Filtration","Democracy Protects","Electrical Conduit","Engineering Kit","Extra Padding","Fortified","Inflammable","Med-Kit","Peak Physique","Scout","Servo-Assisted","Unflinching","Siege-Ready","Acclimated","Integrated Explosives","Gunslinger","Reinforced Eppauletts","Ballistic Padding"]


#code
while True:
    pti = randint(1,7)
    sti = randint(1,3)
    tti = randint(1,2)
    ati = randint(1,3)


    #Picking the Primary
    if pti == 1:
       Primary_Index = randint(0,len(ARs)-1)
       for i, v in enumerate(ARs):
            if i == Primary_Index:
                Primary = v
                break
            else:
                continue
    elif pti == 2:
        Primary_Index = randint(0,len(MRs)-1)
        for i, v in enumerate(MRs):
            if i == Primary_Index:
                Primary = v
                break
            else:
                continue
    elif pti==3:
        Primary_Index = randint(0,len(SMG)-1)
        for i, v in enumerate(SMG):
            if i == Primary_Index:
                Primary = v
                break
            else:
                continue
    elif pti==4:           
        Primary_Index = randint(0,len(SG)-1)
        for i, v in enumerate(SG):
            if i == Primary_Index:
                Primary = v
                break
            else:
                continue
    elif pti==5:
        Primary_Index = randint(0,len(EXP)-1)
        for i, v in enumerate(EXP):
            if i == Primary_Index:
                Primary = v
                break
            else:
                continue

    elif pti==6:
        Primary_Index = randint(0,len(EB)-1)
        for i, v in enumerate(EB):
            if i == Primary_Index:
                Primary = v
                break
            else:
                continue

    elif pti==7:
        Primary_Index = randint(0,len(P_SPEC)-1)
        for i, v in enumerate(P_SPEC):
            if i == Primary_Index:
                Primary = v
                break
            else:
                continue

    #Picking the Secondary
    if sti == 1:
       Secondary_Index = randint(0,len(PISTOL)-1)
       for i, v in enumerate(PISTOL):
            if i == Secondary_Index:
                Secondary = v
                break
            else:
                continue
    elif sti == 2:
        Secondary_Index = randint(0,len(MELEE)-1)
        for i, v in enumerate(MELEE):
            if i == Secondary_Index:
                Secondary = v
                break
            else:
                continue
    elif sti==3:
        Secondary_Index = randint(0,len(S_SPEC)-1)
        for i, v in enumerate(S_SPEC):
            if i == Secondary_Index:
                Secondary = v
                break
            else:
                continue
    
    #Picking the Throwable
    if tti == 1:
       Throwable_Index = randint(0,len(STANDARD)-1)
       for i, v in enumerate(STANDARD):
            if i == Throwable_Index:
                Throwable = v
                break
            else:
                continue
    elif tti == 2:
        Throwable_Index = randint(0,len(T_SPEC)-1)
        for i, v in enumerate(T_SPEC):
            if i == Throwable_Index:
                Throwable = v
                break
            else:
                continue
    
    #Armor Type
    if ati == 1:
        ArmorType="Light"
    elif ati == 2:
        ArmorType="Medium"
    elif ati == 3:
        ArmorType="Heavy"
    
    #Armor Passive
    AP_Index = randint(0,len(Passives)-1)
    for i, v in enumerate(Passives):
        if i == AP_Index:
            ArmorPassive = v
            break
        else:
            continue
    print(f"{cls}\nPrimary: {Primary}\nSecondary: {Secondary}\nThrowable: {Throwable}\n{d}\nArmor Passive: {ArmorPassive}\nArmor Type: {ArmorType}\n{d}")
    if input("Type EXIT to leave. ") == "EXIT":
        break