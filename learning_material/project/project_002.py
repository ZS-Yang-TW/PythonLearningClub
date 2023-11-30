# 使用者輸入
gender = input("請輸入性別（男/女）：")
age = int(input("請輸入年齡："))
height = float(input("請輸入身高（公分）："))
weight = float(input("請輸入體重（公斤）："))
body_fat = float(input("請輸入體脂率（百分比）："))
activity_factor = float(input("請輸入活動因子："))
stress_factor = float(input("請輸入壓力因子："))

# 計算BMI
BMI = weight / (height/100)**2

# 計算除脂體重
lean_body_mass = weight * (100 - body_fat) / 100

# 計算基礎代謝率
if gender == "男":
    bmr = 66 + ( 13.7*weight + 5*height - 6.8*age ) 
elif gender == "女":
    bmr = 655 + ( 9.6*weight + 1.8*height - 4.7*age )

# 計算總熱量消耗
TDEE = bmr * activity_factor * stress_factor

# 計算低碳飲食法的三大營養素熱量
carbohydrate = TDEE * 0.2
protein = TDEE * 0.3
fat = TDEE * 0.5

# 計算低碳飲食法的三大營養素克數
carbohydrate_gram = carbohydrate / 4
protein_gram = protein / 4
fat_gram = fat / 9

# 判斷體重狀態
if BMI < 18.5:
    BMI_status = "體重過輕"
elif BMI >= 18.5 and BMI < 24:
    BMI_status = "正常"
elif BMI >= 24 and BMI < 27:
    BMI_status = "過重"
elif BMI >= 27 and BMI < 30:
    BMI_status = "輕度肥胖"
elif BMI >= 30 and BMI < 35:
    BMI_status = "中度肥胖"
elif BMI >= 35:
    BMI_status = "重度肥胖"
    
# 顯示健康飲食推薦報告：

print("\n#-----您的健康飲食推薦報告-----#\n")
print("您的BMI為：",BMI)
print("您的除脂體重為：",lean_body_mass)
print("您的體重狀態為：",BMI_status)
print("您的體脂率為：",body_fat,"%")
print("您的基礎代謝率為：",bmr)
print("您的總熱量消耗為：",TDEE,"\n")
print("您的低碳飲食法三大營養素建議克數為：")
print("碳水化合物：",carbohydrate_gram,"克")
print("蛋白質：",protein_gram,"克")
print("脂肪：",fat_gram,"克")