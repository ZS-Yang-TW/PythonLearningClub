# 模組匯入
from alive_progress import alive_bar
from time import sleep

# 定義顏色
RED = "\033[31m"  # 紅色
GREEN = "\033[32m"  # 綠色
YELLOW = "\033[33m"  # 黃色
BLUE = "\033[34m"  # 藍色
MAGENTA = "\033[35m"  # 品紅色
CYAN = "\033[36m"  # 青色
WHITE = "\033[37m"  # 白色
RESET = "\033[0m"  # 重置顏色
BOLD = "\033[1m"  # 粗體

# 輸入（性別、年齡、身高（公分）、體重（公斤）、體脂率（百分比）、活動因子、壓力因子）
gender = input("請輸入性別（男/女）：")
age = int(input("請輸入年齡："))
height = float(input("請輸入身高（公分）："))
weight = float(input("請輸入體重（公斤）："))
body_fat = float(input("請輸入體脂率（百分比）："))
activity_factor = float(input("請輸入活動因子："))
stress_factor = float(input("請輸入壓力因子："))

# 單位轉換
height_meter = height/100

# 計算「BMI」
BMI = weight/(height_meter**2)

# 計算「除脂體重」
weight_without_fat = weight*(100-body_fat)/100

# 計算「基礎代謝率」
if gender == "男":
    BMR = 66 + (13.7*weight+5*height-6.8*age)
else:
    BMR = 665 + (9.6*weight+1.8*height-4.7*age)

# 計算「總熱量消耗」
TDEE = BMR*activity_factor*stress_factor

# 計算三大營養入的熱量比例
carbon = TDEE*0.2
protein = TDEE*0.3
fat = TDEE*0.5

carbon_g = carbon/4
protein_g = protein/4
fat_g = fat/9

# 邏輯判斷 - 體重狀態
if BMI < 18.5:
    weight_status = "體重過輕"
elif 18.5 <= BMI < 24:
    weight_status = "體重正常"
elif 24 <= BMI < 27:
    weight_status = "過重"
elif 27 <= BMI < 30:
    weight_status = "輕度肥胖"
elif 30 <= BMI < 35:
    weight_status = "中度肥胖"
else:
    weight_status = "重度肥胖"
    
# 樣式設定
if weight_status == "體重過輕":
    weight_status = BOLD + RED + weight_status + RESET
if weight_status == "體重正常":
    weight_status = BOLD + GREEN + weight_status + RESET
if weight_status == "過重":
    weight_status = BOLD + YELLOW + weight_status + RESET
if weight_status == "輕度肥胖":
    weight_status = BOLD + RED + weight_status + RESET
if weight_status == "中度肥胖":
    weight_status = BOLD + RED + weight_status + RESET
if weight_status == "重度肥胖":
    weight_status = BOLD + RED + weight_status + RESET
    
# 進度條動畫
print("\n")
with alive_bar(100, title = "📋 飲食報告生成中...") as bar:
    for i in range(100):
        sleep(0.01)
        bar()

# 輸出 - 飲食報告
print("\n")
print(BOLD + "#----- 您的健康飲食報告 -----#" + RESET)
print("您的體重狀態為：", weight_status)
print("您的BMI為：", round(BMI, 2))
print("您的除脂體重為：", weight_without_fat, "公斤")
print("您的基礎代謝率為：", round(BMR, 2), "大卡")
print("您的總熱量消耗為：", round(TDEE, 2), "大卡")

print("\n")
print(BOLD + "您的低碳飲食法三大營養素建議克數為：" + RESET)
print("🍙 碳水化合物：", round(carbon_g, 2), "公克")
print("🥚 蛋白質：", round(protein_g, 2), "公克")
print("🪔 脂肪", round(fat_g, 2), "公克")