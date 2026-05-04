def calculate_bmi(height, weight):
    print("height = " + str(height))
    print("weight = " + str(weight))
    bmi=weight/(height*height)
    print("bmi = " + str(bmi))
    if bmi<18.5:
        print("underweight")
        print("-1")
    if bmi>25.0:
        print("overweight")
        print("1")
    else:
        print("normal weight")
        print("0")

calculate_bmi(weight = 57, height = 1.73)

