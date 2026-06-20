marks={"riya":99,"ramesh":68,"rahul":64,"priya":90,"rohan":88}
sum=0
avg=0
for m in marks.values():
    sum=sum+m
avg=sum/len(marks)
print("your average is",avg)
high=max(marks.values())
low=min(marks.values())
for m,y in marks.items():
    if y==high:
        print("the highest score is",high,"which was got by",m)
    elif y==low:
        print("the lowest score is",low,"which was got by",m)
name=input("enter name:")
print(marks.get(name,"we do not have the name you requested"))     
 

      
