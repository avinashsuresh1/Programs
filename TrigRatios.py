#Given angle in degrees this program gives the value of all 6 trigonometric ratios
import math

x = float(input("Enter angle in degrees: "))

csign=1

if(x>=360):
    xshort = x%360
else:
    xshort = x

if(xshort==0 or xshort==180):
    sin=0
    cos=1
elif(xshort==90 or xshort==270):
    sin=1
    cos=0    
else: 
    xc = xshort*math.pi/180
    sum=0
    for i in range(85):     #Can't exceed beyond 85, will result in overflow
        sum+=(-1)**i*xc**(2*i+1)/math.factorial(2*i+1)
        
    sin=round(sum,12)
    cos=round(math.sqrt(1-sum**2),12)

if(xshort>90 and xshort<=270):
    csign=-1

cos*=csign

if(sin==0):
    cot="undefined"
    cosec="undefined"
    tan=0
    sec=int(1/cos)
elif(cos==0):
    tan="undefined"
    sec="undefined"
    cot=0
    cosec=int(1/sin)
else:
    tan=round(sin/cos, 12)
    cot=round(cos/sin, 12)
    sec=round(1/cos, 12)
    cosec=round(1/sin, 12)

print("\nResults: \n")
print(f"\t1. sin({x}\u00B0) = {sin}")
print(f"\t2. cos({x}\u00B0) = {cos}")
print(f"\t3. tan({x}\u00B0) = {tan}")
print(f"\t4. cosec({x}\u00B0) = {cosec}")
print(f"\t5. sec({x}\u00B0) = {sec}")
print(f"\t6. cot({x}\u00B0) = {cot}")
