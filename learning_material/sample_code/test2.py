## 輸入基本資料
"性別" #gender
"年齡" #age
"身高" #height
"公斤" #kg
"體脂率" # BMR

#LBM
#Boy_BMR = 13.7*(kg)+5*(height)-6.8*(age)
#irl_BMR = 13.7*(kg)+5*(height)-6.8*(age)
#print("男性BMR",Boy_BMR)
#print("女性BMR",Girl_BMR)
#體脂率 = 1.2 x BMI 值+ 0.23 x 年齡 - 5.4 -10.8 x 性別
#體脂肪率 (Body Fat %) 
#除脂體重FFMI = 體重*(100-體脂率)
#基礎代謝率（BMR）
#TDEE = BMR*活動因子*壓力因子
#BMI < 18.5 體重過輕
#18.5 ≤ BMI < 24 正常
#24 ≤ BMI < 27 過重
#27 ≤ BMI < 30 輕度肥胖
#30 ≤ BMI < 35 中度肥胖
#BMI ≥ 35 重度肥胖
#碳水化合物**：TDEE * 20%
#蛋白質**：TDEE * 30%
#肪脂**：TDEE * 50%
# Boy_BMR = float{(13.7*(kg)+5*(height)-6.8*(age))} 

gender = input("請輸入性別(男/女):")
age = input("請輸入年齡:")
height = int(input("請輸入身高:")) 
kg = int(input("請輸入公斤:")) 
Body_Fat = int(input("請輸入體脂率百分比:"))
act = float(input("請輸入活動因子:"))
press = float(input("請輸入壓力因子:"))
BMI = int(kg) / ((int(height) / 100) ** 2)
FFMI = (kg*(100-(Body_Fat))/100)


if BMI < 18.5:
    BMI_status = "體重過輕"
elif BMI >= 18.5 and BMI < 24 :
    BMI_status = "正常"
elif BMI >= 27 and  BMI < 30  :
    BMI_status ="過重"
elif BMI >= 30 and BMI < 35  :
   BMI_status ="中度肥胖"
else :
    BMI_status ="重度肥胖" 

if gender == "男":
    BMR = 66 + (13.7 * float(kg) + 5 * int(height) - 6.8 * float(age))
    print("男性BMR",BMR)
elif gender == "女":
    BMR = 655 + (9.6 * float(kg) + 1.8 * int(height) - 4.7 * float(age))
    print("女性BMR",BMR)

TDEE = BMR*act*press
carbohydrate = TDEE*0.2
protein = TDEE*0.3
fat = TDEE*0.5


carbohydrate_gram =carbohydrate / 4 
protein_gram = protein / 4
fat_gram = fat / 9

print("\n#-----您的健康飲食推薦報告-----#\n")
print("您的BMI為:",BMI)
print("您的除脂體重為:",FFMI)
print("您的體重狀態為:",BMI_status)
print("您的體脂肪率為:",Body_Fat)
print("您的基礎代謝率為:",BMR)
print("您的總熱量消耗為:",TDEE)
print(f"您的低碳飲食法三大營養素建議克數為:")
print("碳水化合物:",carbohydrate_gram,"g")
print("蛋白質:",protein_gram,"g")
print("肪脂:",fat_gram,"g")