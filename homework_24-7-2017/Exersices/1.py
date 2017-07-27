h = float(input("What's your height?(m)"))
w = float(input("What's your weight?(kg)"))
bmi = float(w/(h*h))

if bmi < 16:
    print("Severely underweight !!!")
elif bmi <= 18.5:
    print("Uderweight !")
elif bmi <= 25:
    print("Normal :D")
elif bmi <=30:
    print("Overweight !")
else:
    print("Obese !!!")

