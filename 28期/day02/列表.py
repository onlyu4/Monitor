
#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                    O\ = /O
#                ____/`---'\____
#              .   ' \\| |// `.
#               / \\||| : |||// \
#             / _||||| -:- |||||- \
#               | | \\\ - /// | |
#             | \_| ''\---/'' | |
#              \ .-\__ `-` ___/-. /
#           ___`. .' /--.--\ `. . __
#        ."" '< `.___\_<|>_/___.' >'"".
#       | | : `- \`.;`\ _ /`;.`/ - ` : | |
#         \ \ `-. \_ __\ /__ _/ .-` / /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
#
# .............................................
#          佛祖保佑             永无BUG
#  佛曰:
#          写字楼里写字间，写字间里程序员；
#          程序人员写程序，又拿程序换酒钱。
#          酒醒只在网上坐，酒醉还来网下眠；
#          酒醉酒醒日复日，网上网下年复年。
#          但愿老死电脑间，不愿鞠躬老板前；
#          奔驰宝马贵者趣，公交自行程序员。
#          别人笑我忒疯癫，我笑自己命太贱；
#          不见满街漂亮妹，哪个归得程序员？

#列表：
    #  专门存储大量数据的的数据类型，是可变的数据类型

#添加元素：
    #append()
list = []
list.append("zhangsan")
    #insert():插入
list.insert(0,"lisi")
#print(list)

#删除元素
    #remove()
list.remove("lisi")

    #pop
#list.pop(0)

    #clear:清空
list.clear()
#print(list)

#修改：
    #列表可以通过索引进行修改

list2 = ["足球","篮球","乒乓球","排球","台球"]
list2[1] = "张三"
#(list2)

#查询：
# for i in list2:
#     #print(i)
#     for  c in i:
#         print(c)

lst = [111, 222, 3, ["呵呵", [11, 22, [4, "胡辣汤", 5]], "哈哈"]]
lst[3][1][2][2] = 15
#print(lst)

# list = ["a","b","c","d","e"]
# for i in range(len(list)):
#     print(i)


#敏感词判断
li = ["苍老师", "东京热", "武藤兰", "波多也结二"]
user_input = input(">>>").strip()
for i in li:
    if i in user_input:
        number = len(i)
        user_input=user_input.replace(i,"*"*number)
print(user_input)