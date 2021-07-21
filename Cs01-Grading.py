S1=int(input("ใส่คะแนนเก็บ :"))
S2=int(input("ใส่คะแนนสอบกลางภาค :"))
S3=int(input("ใส่คะแนนสอบปลายภาค :"))
Scorall=S1+S2+S3
if(Scorall==100 or Scorall>80):
    print("A")
elif(Scorall==79 or Scorall>=75):
    print("B+")
elif(Scorall==74 or Scorall>=70):
    print("C+")
elif(Scorall==69 or Scorall>=65):
    print("C")
elif(Scorall==59 or Scorall>=55):
    print("D+")
elif(Scorall==54 or Scorall>=50):
    print("D")
elif(Scorall==49 or Scorall>=0):
    print("F")