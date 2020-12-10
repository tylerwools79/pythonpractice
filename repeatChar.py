#create a lambda function to repeat a char n times
repeatChar = lambda ch,n:""+(ch*n)

print(repeatChar("*",4)=="****")
print(repeatChar("T",6)=="TTTTTT")
print(repeatChar("-",0)=="")