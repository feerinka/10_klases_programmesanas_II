while True:
    choice = input("lai turpinātu, nospiediet y, lai pabeigt -n\n")
    if choice=="y":
        print("Cik rezistoru ķēdē?")
        count=int(input())
        if count==2:

          r1=float(input("R1= "))
          r2=float(input("R2 "))
          if r1==0 or r2==0:
              print("uzmanību, īss savienojums!")
          else:
           r=round(1/(1/r1+1/r2),2)

          print("R =",r,"ohm")

        if count==3:
          r1=float(input("R1= "))
          r2=float(input("R2 "))
          r3=float(input("R3 "))
          if r1==0 or r2==0 or r3==0:
             print("uzmanību, īss savienojums!")
          else:
            r=round(1/(1/r1+1/r2+1/r3),2)

            print("R =",r,"ohm")
    if choice=="n":
        break 


