fh=open("output1.txt",'w')
c= float (input("enter celcius value:"))
f=(c*(9/5)+32)
fh.write("fahrenheit is :"+str(f))
#,celceius =(fahrenheit-32)x5/9 fahernheit to celcius
f= float(input("enter value in fahernheit:"))
c=((f-32)*5/9)
fh.write("celcius conversion is :"+str(c))
fh.close
