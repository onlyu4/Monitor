
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

#所有空的字符串都是false，其他都是True
print(bool(" "))

#字符串
    #多个字符连成串，单个文字符号叫做字符。

#索引和切片：
    #索引：每个字符在字符串中的位置，从0开始。
a = "abcdefg"
print(a[3])

#切片
    #从字符串中取出字符组成新的字符串
s = "abcdefg"
print(s[1:5])   #取头不取尾

c = "上海自来水来自海上"

if c[:] == c[::-1]:
    print("Ture")

#转大写：
    #upper(),把字符串转换成大写

#去首尾空格
    #strip()，去掉首尾的空白

#替换：
    #repla(),把字符串中的呃xxx替换成xxx

Frist = "  asdas sad  asd as da d".strip().replace(" ","")
print(Frist)

#字符串切割：
    #split(),切割字符串，得到的结果是一个列表

#判断字符串是否由数字组成
    #isdigit()判断字符串是否由字符串组成

#计数：
    #count()，统计xxx字符在字符串中出现的次数

#查找子字符串在字符串中出现的位置：
    #indx()   find()

#统计字符串的长度：
    #len()

# test = "zhangsanlisi王五"
# i = 0
# while i < len(test):
#     print(test[i])
#     i+=1

# for i in test:
#     print(i)

count = 0
test = input(":")
for i in test:
    if i.isdigit():
        count+=1
print(count)


