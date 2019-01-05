# data type have int float bool str / list
# for loop 清單中的東西拿出來
cars = ['BMW', 'Toyota']
for car in cars:
    print(car) #兩個迴圈走兩次


#import載入
#import random不需要等號 
import random
start = input('請隨機設定初始值: ')
end = input('請隨機設定範圍結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
    count = count + 1
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
        print('你猜中了!')
        print('這是你猜的第', count, '次')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
    print('這是你猜的第', count, '次')


#密碼設定
password = 'a123456'
i = 3
while i > 0:
    i = i - 1
    pwd = input('請輸入您的密碼: ')
    if pwd == password :
        print('登入成功')
        break
    else:
        print('密碼錯誤!')
        if i > 0:
            print('你還有', i, '次機會')
        else:
            print('你沒機會了 要被鎖了 哈哈')
            break


password = 'a123456'
i = 3
while True:
    pwd = input('請輸入您的密碼: ')
    if pwd == password :
        print('登入成功')
        break
    else:
        i = i - 1
        print('密碼錯誤! 還有', i, '次機會')
        if i == 0:
            break
    

#迴圈
#x = 5
#while x < 10:
#    print('x little 10')
#    print('run')
#    x = x + 1
#print("end")

while True:
    mode = input('請輸入遊戲模式: ')
    if mode == 'q':
        break
    elif mode == '1':
        print('啟動模式一')
    elif mode == '2':
        print('啟動模式二')
    else:
        print('只能輸入1/2/q')

i = 3
while i < 10:
    print('hi')
    i = i + 2

while True:
    name =input('請輸入您的姓名')
    if name == 'q':
        break
    else:
        print('重新輸入')

#年齡
age = input('請輸入年齡')
age = int(age)
if age < 13:
    print('國小')
elif age >=13 and age <18:
    print('國高中')
elif age >=18 and age <22:
    print('國高中')
else:
    print('社會')

#溫度
c = input('請輸入攝氏溫度')
c = float(c)
f = c * 9 / 5 + 32
print('華氏溫度為:', f)

#BMI值
height = input('請輸入您的身高(cm): ')
weight = input('請輸入您的體重(kg): ')
height = float(height)
weight = float(weight)
height = height / 100
bmi = weight/(height*height)
if bmi < 18.5:
    print('體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('正常範圍')
elif bmi >= 24 and bmi <27:
    print('過重')
elif bmi >=27 and bmi <30:
    print('輕度肥胖')
elif bmi >=30 and bmi <35:
    print('中度肥胖')
else :
    print('重度肥胖')
