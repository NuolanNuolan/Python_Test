from def_hello import *
from collections import OrderedDict


# //大小写
# name = "ada lovalcase"
# print(name.title())
# 全部大写
# print(name.upper())
# 全部小写
# print(name.lower())
# //字符串拼接
# firat_name = "yuan"
# last_name  = "lianlin"
# print("hello, "+firat_name.title()+last_name+"!")
# //制表符
# name = "python"
# print("\t\n\t"+name)
# //删除空白
# name = 'python '
# name = name.rstrip()
# print(name)

# name = "yuanliANlin"
# print("hello "+name.lower()+" "+"would you like to learn some python today?")

# print(0.1*31)

# age = "23"
# message = "happy "+ str(age) + "rd birthday"
# print(message)

# print(3/2)

# 数组的操作
# nameArr = ["apple","mac","book","pro","google"]
# nameArr[0] = "Apple"
# nameArr.append("121")
# nameArr.insert(1,"google")
# del nameArr[0]
# print(nameArr.pop(0))
# nameArr.remove("google")
# nameArr.sort(reverse=True)
# del nameArr[0]
# nameArr.append("iOS")
# nameArr.extend(nameArr)
# print(len(nameArr))
# for name in nameArr:
#   print(name)

# for value in range(0,10):
#   print(value)

# numbers = list(range(1,101,2))
# print(numbers)

# squares = []
# for value in range(1,10):

#   squares.append(value*2)
# print(squares)
# print(min(squares))
# print(max(squares))
# print(sum(squares))

# squares = [value**2 for value in range(1,11)]
# print(squares)

# squares = []
# for value in range(1,101):
#   squares.append(value)

# print(squares)
# print(len(squares))
# for value1 in squares[:3]:
#   print(value1)

# #元组
# dimensions = (200,500,500)
# dimensions = (400,400,500)
# for value in dimensions:
#     print(value)

# names = ["admin","root","yuanlianlin","memeda","fuck"]
# for name in names:
#     print("hello %s welcome"%name)

# names =  {'color':'yellow','points':'5','name':'alien'}
# aliens = {'color':'yellow','points':'5','name':names}
# print(aliens)

# message = input("plaese input:")
# print(message)

# name = 'input:'
# message = ""
# while message !='exit':
#     message = input(name)
#     print(message)

# count = 1
# while count<=5:
#     print("%dxxx"%count)
#     count+=1

# promt = "push:"
# active = True
# while active:
#     message = input(promt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# response = {}
# isTrue =  True

# while isTrue:
#     name = input("what is name?:")
#     respons = input("lalalalla:")

#     response[name] = respons

#     report = input("hhaaa:")
#     if report == 'no' or report == 'NO':
#         isTrue = False

# print(response)

# for  key,value in response.items():
#     print("name :%s respons: %s"%(key,value))

# def build(first,last,userinfo):
#     profile = {}
#     profile['firatname'] = first
#     profile['lastname'] = last
#     for key,value in userinfo.items():
#         profile[key] = value
#     return profile
# print(build('yll','YLL',{"hahha":'memeda','xixixi':'papapa'}))


# name = make_pizza('size','name')
# print(name)
# my_dog = electri("hehehe",17)
your_dog = Dog("hahaha", '20')
# my_dog.sit()
# your_dog.sit()
# print(my_dog.age)
# my_dog.changeage(15)
# print(my_dog.age,my_dog.battery_size)
# my_dog.battery_size.describe_battery()


favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['yll'] = 'oc'
favorite_languages['phil'] = 'ruby'
for key, value in favorite_languages.items():
    print(key, value)
