import math

print("Enter total lines of code")
loc = int(input())
print("No of lines of code are ",loc)

   
kloc = loc/1000
if kloc <50:
    mode = 'Organic'
elif kloc<300:
    mode = 'Semi-Detached'
else:
    mode = 'Embedded'


print("\nMode detected is ", mode)
var_table = {'Organic':[2.4,1.05,2.5,0.38],'Semi-Detached':[3.0,1.12,2.5,0.35],'Embedded':[3.6,1.2,2.5,0.32]}

E = math.pow(kloc,var_table[mode][1])*var_table[mode][0]
print("\nEffort required is %.1f Person-months" %(E))

TDEV = math.pow(E,var_table[mode][3])*var_table[mode][2]
print("Time for development is %.1f months" %(TDEV))

print("Average Staff Size is %.1f" %(E/TDEV))
print("Productivity is %.2f KLOC/person-month" %(kloc/E))
