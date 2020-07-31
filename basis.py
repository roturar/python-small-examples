print('Hello World!')

# 1、绝对值
positive_number = abs(-5)
print(positive_number)

# 2、元素都为真
print(all([1, 0, 3, 5]))
print(all([1, 3, 2, 8]))

# 3、元素至少有一个为真
print(any([0, 0, 0, []]))
print(any([0, 0, 1, 0]))


# 4、ascii展示对象
class Student():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'id = ' + self.id + ', name =  ' + self.name


xiaoming = Student(id='001', name='xiaoming')
print(xiaoming)
print(ascii(xiaoming))
print(ascii('hello'))
print(ascii('中国'))
print(ascii(1))
print(ascii([1, 2]))


# 5、将十进制转换为二进制
print(bin(10))

# 6、十进制转换为八进制
print(oct(9))

# 7、十进制转换为十六进制
print(hex(15))

# 8、测试一个对象是Ture，还是False
print(bool(0))
print(bool([0, 0, 0]))  # 非0即为真，数组全是零也属于非‘0’，即为真
print(bool([]))
print(bool([1, 0, 1]))
print(bool('False'))

# 9、将一个字符串转换成字节类型
s = 'apple'
print(bytes(s, encoding='utf-8'))

# 10、将字符类型、数值类型等转换为字符串类型
i = 100
print(str(i))
