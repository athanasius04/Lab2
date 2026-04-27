def calculate_bmi(height, weight):
    print("height = " + str(height))
    print("weight = " + str(weight))
    bmi=weight/(height*height)
    print("bmi = " + str(bmi))
    if bmi<18.5:
        print("underweight")
    if bmi>25.0:
        print("overweight")
    else:
        print("normal weight")

calculate_bmi(weight = 57, height = 1.73)

