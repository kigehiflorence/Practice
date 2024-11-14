weight=input("Weight: ")
kg_or_lbs=input("(K)g or (L)bs: ")
if kg_or_lbs == "K":
    converted=float(weight)/0.45
    print("Weight in lbs: " ,converted)
elif kg_or_lbs == "L":
    converted= float(weight) *0.45
    print("Weight in kg: " , converted)
