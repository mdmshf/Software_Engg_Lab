
import math

table=[[3.2,1.05,2.5,0.38],[3.0,1.12,2.5,0.35],[2.8,1.20,2.5,0.32] ]
mode=["Organic","Semi-Detached","Embedded"] 
driver=["RELY","DATA","CPLX","TIME","STOR","VIRT","TURN","ACAP","AEXP","PCAP", "VEXP","LEXP","MODP","TOOL","SCED"] 
costdrivers=[ 
              [0.75,0.88,1,1.15,1.40,-1], 
              [-1,0.94,1,1.08,1.16,-1], 
              [0.70,0.85,1,1.15,1.30,1.65], 

              [-1,-1,1,1.11,1.30,1.66], 
              [-1,-1,1,1.06,1.21,1.56], 
              [-1,0.87,1,1.15,1.30,-1], 
              [-1,0.87,1,1.07,1.15,-1], 

              [1.46,1.19,1,0.86,0.71,-1], 
              [1.29,1.13,1.00,0.91,0.82,-1], 
              [1.42,1.17,1,0.86,0.70,-1], 
              [1.21,1.10,1,0.90,-1,-1], 
              [1.14,1.07,1,0.95,-1,-1], 

              [1.24,1.10,1.00,0.91,0.82,-1], 
              [1.24,1.10,1,0.91,0.83,-1], 
              [1.23,1.08,1,1.04,1.10,-1] 
              ] 

mp=[ 
          [0.06,0.16,0.26,0.42,0.16], 
          [0.06,0.16,0.24,0.38,0.22], 
          [0.07,0.17,0.25,0.33,0.25], 
          [0.07,0.17,0.24,0.31,0.28], 
          [0.08,0.18,0.25,0.26,0.31], 
          [0.08,0.18,0.24,0.24,0.34] 
        ] 
tp=[ 
          [0.10,0.19,0.24,0.39,0.18], 
          [0.12,0.19,0.21,0.34,0.26], 
          [0.20,0.26,0.21,0.27,0.26], 
          [0.22,0.27,0.19,0.25,0.29], 
          [0.36,0.36,0.18,0.18,0.28], 
          [0.40,0.38,0.16,0.16,0.30] 
        ] 

phases=["Planning and Requirements","System Design","Detail Design","Module Code and Test","Integration and Test"] 

print("\nEnter the size of project : ") 
size=int(input())
if(size>=2 and size<=50) :
  model=0 
elif(size>50 and size<=300) :
  model=1 
elif(size>300) :
  model=2 
print("\nMode = %s",mode[model]) 
EAF=1 
for i in range(15):
  a=-1 
  while(a==-1):  
              print("\nRate cost driver %s on scale of 0-5 : ",driver[i]) 
              print("\n0-Very Low\t1-Low\t2-Nominal\t3-High\t4-Very High\t5-Extra High\n") 
              rating=int(input())
              a=costdrivers[i][rating] 
              if(a==-1) :
                print("\nNo value exist for this rating..Enter another rating...\n") 

 
  EAF=EAF*a  
print("\nEAF = ",EAF) 

effort=(table[int(model)][0]*pow(size,table[int(model)][1])) * EAF 
time=table[int(model)][2]*pow(effort,table[int(model)][3]) 
staff=effort/time 
productivity=size/effort 

print("\n\nEffort = %f Person-Month",effort) 
print("\nDevelopment Time = %f Months",time) 
print("\nAverage Staff Required = %d Persons",staff)
print("\nProductivity = %f KLOC/Person-Month",productivity) 
print("\n\n") 

if(model==0) :

  print("\nEnter Ogranic - Small(0) or Medium(1) : ") 
  S=int(input())

elif(model==1) :

  print("\nEnter Semi-Detached - Medium(2) or Large(3) : ") 
  S=int(input()) 

elif(model==2) :

  print("\nEnter Embedded - Large(4) or Extra Large(5) : ") 
  S=int(input())

print("\n\nPhase-wise Distribution of Effort is :\n\n") 
for i in range(5):

   print("\n%s Phase  =  ",phases[i]) 
   print("%f",effort*mp[S][i]) 

print("\n\nPhase-wise Distribution of Development Time is :\n\n") 
for i in range(5):

   print("\n Phase  =  ",phases[i]) 
   print("%f",time*tp[S][i]) 


