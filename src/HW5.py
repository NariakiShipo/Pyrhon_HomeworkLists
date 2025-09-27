def BMI_Calculator(weight, height) -> str:
    bmi = weight / (height ** 2)
    match bmi:
        case bmi if bmi < 18:
            return "Underweight"
        case bmi if 18 <= bmi < 24:
            return "Normal"
        case bmi if 24 <= bmi < 27:
            return "Overweight"
        case bmi if 27 <= bmi < 30:
            return "Mild obesity"
        case bmi if 30 <= bmi < 35:
            return "Moderate obesity"
        case bmi if bmi >= 35:
            return "Severe obesity"
height = float(input())
weight = float(input())
category = BMI_Calculator(weight, height)
print(category)