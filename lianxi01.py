
"""
练习1 通过代码获取两段内容，并且计算他们的长度的和。获取值1的内容，获取值2的内容，值1的长度加值2的长度
"""
# a = input("任意输入内容1：")
# b = input("任意输入内容2：")
# print("a+b的内容长度:",len(a+b))

# a = input("请输入内容1：")
# b = input("请输入内容2：")
# print(len(a+b))



"""
练习2：
通过print打印，模拟一个红绿灯的功能，注意：红灯30次，绿灯35次，黄灯3次。
"""
# ligh = {"红灯":30,"绿灯":35,"黄灯":3}
# while True:
#     for i in ligh:    #用i来遍历ligh字典，i 的遍历对象是key值
#         for j in range(ligh[i]):    #用j来遍历lingh中的value值（ligh[i]），当上一步：i是红灯时，执行j的遍历从0-29（左闭右开）共30次循环，然后继续i等于绿灯时，j继续遍历绿灯对应的value值执行0-34共35次
#             print(i,"倒计时还有：",ligh[i]-j,"秒")                   
        
"""
练习3：
使用代码，实现一个注册的功能。
用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头。
储到到字典中，{username:password}
"""
# username = input("请输入账号：")
# password = input("请输入密码：")
# if len(username) >= 5 and len(password)<= 8:
#     if username[0] in "qwertyuiopasdfghjklzxcvbnm":
#         if len(password) >= 6 and len(password) <= 12:
#             print("注册成功！",{username:password})
#         else:
#             print("密码长度不符合规范，请输入5-8位的密码")
#     else:
#         print("账号必须是小写开头，请输入正确的账号")
# else:
#     print("账号长度不符合规范，请输入5-8位的账号")


"""练习4自动判断账号长度是5-8位，并且账号首位为小写字母开头"""
# def checkname(username):
#     """自动判断账号长度是5-8位，并且账号首位为小写字母开头"""
#     if len(username) >= 5 and len(username)<= 8:
#         if username[0] in "qwertyuiopasdfghjklzxcvbnm":
#             print("ok")
#         else:
#             print("账号必须是小写开头，请输入正确的账号")
#     else:
#         print("账号长度不符合规范，请输入5-8位的账号")

# a = "4jkkfdk"
# checkname(a)

"""练习5定义一个方法，用来判断用户输入的账号和密码是否符合规范"""
# def checkname(username,password):
#     if len(username) >=5 and len(username) <=8:
#         if username[0] in "qwertyuioopasdfgjklzxcvbnm":
#             if len(password) >= 6 and len(password) <= 12:
#                 return True
#             else:
#                 return "密码长度不符合规范，请输入5-8位的密码"
#         else:
#             return "账号必须是小写开头，请输入正确的账号"
#     else:
#         return "账号长度不符合规范，请输入5-8位的账号"

# checkname("zhangsan","123456223")

"""
练习6：请使用代码完成一个登录注册得功能，并且数据要存到数据库中
"""
iiiiii
iiiiii
diamam