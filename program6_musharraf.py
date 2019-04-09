import math

print("Enter total lines of code")
loc=int(input())

   
kloc = loc/1000.0
mode_table = ['Organic','Semi-Detached','Embedded']

if kloc <50:
    mode = 'Organic'
elif kloc<300:
    mode = 'Semi-Detached'
else:
    mode = 'Embedded'

print("Mode is ",mode)
var_dict = {'Organic':[2.4,1.05,2.5,0.38],'Semi-Detached':[3.0,1.12,2.5,0.35],'Embedded':[3.6,1.2,2.5,0.32]}
var_table = [[0.75,0.88,1,1.15,1.40,-1],[-1,0.94,1,1.08,1.16,-1],[0.70,0.85,1,15,1.30,1.65],[-1,-1,1,1.11,1.30,1.66],[-1,-1,1,1.06,1.21,1.56],[-1,0.87,1,1.15,1.30,-1],[-1,0.87,1,1.07,1.15,-1],[1.46,1.19,1,0.86,0.71,-1],[1.29,1.13,1.00,0.91,0.82,-1],[1.42,1.17,1,0.86,0.70,-1],[1.21,1.10,1,0.90,-1,-1],[1.14,1.07,1,0.95,-1,-1],[1.24,1.10,1.00,0.91,0.82,-1],[1.24,1.10,1,0.91,0.83,-1],[1.23,1.08,1,1.04,1.10,-1]]

driver_table = ["RELY","DATA","CPLX","TIME","STOR","VIRT","TURN","ACAP","AEXP","PCAP","VEXP","LEXP","MODP","TOOL","SCED"]
ratings = []
print('Rate each of the following drivers from 1 - 5: \n0-Very Low\t1-Low\t2-Nominal\t3-High\t4-Very High\t5-Extra High\n')
i,EAF=0,1
while i < (len(driver_table)):
    inp = int(input(str(driver_table[i]) + ": "))
    if var_table[i][inp]==-1:
        print("No values exist for this rating. Please try again")
        continue
    ratings.append(inp)
    EAF*=var_table[i][inp]
    i+=1
    
print("EAF is ", EAF)

E = math.pow(kloc,var_dict[mode][1])*var_dict[mode][0]*EAF  #E = a(KLOC^b)
print("\nEffort required is %.1f Person-months" %(E))

TDEV = math.pow(E,var_dict[mode][3])*var_dict[mode][2] #Time for Development = c(E^d)
print("Time for development is %.1f months" %(TDEV))

print("Average Staff Size is %.1f" %(E/TDEV))
print("Productivity is %.2f KLOC/person-month" %(kloc/E))
