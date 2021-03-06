padding = "\n"

words = ['a','b','c']
print(words[0])
print(words[-1])
print(words)
print(padding)

message = "Second word is " + words[1] + ","
print(message.title())
print(padding)

words[0] = '1'
print(words)
print(padding)

# 数组操作
print('数组操作')

# 末尾添加
print("末尾添加")

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
print(padding)

# 插入元素
print("插入元素")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
print(padding)

# 删除元素
print("删除元素")
del  motorcycles[1]
print(motorcycles)
print(padding)

# 使用pop()删除元素
print("使用pop()删除元素")
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda','yamaha','amadas','suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
print(padding)

# 弹出列表中任意位置的元素，当使用pop时，被弹出的元素就不再是
print('弹出列表中任意位置的元素，当使用pop时，被弹出的元素就不再是')
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
print(padding)

# 删除指定元素
print('删除指定元素')
print(motorcycles)
amadas = 'amadas'
motorcycles.remove(amadas)
print(motorcycles)

elements = ['harry','amanda','angle','zoo','jungle']
print(elements)
print(padding)

# 翻转list
print('翻转list')
elements.reverse()
print(elements)
print(padding)

# 翻转排序
print('翻转排序')
elements.sort(reverse = True)
print(elements)
print(padding)

# 不改变元list的排序
print('不改变元list的排序')
print(sorted(elements))
print(elements)
print(padding)

# 正序排序
print('正序排序')
elements.sort()
print(elements)
print(padding)

# list长度
print('list长度')
length = len(elements)
print(length)
print(padding)

# 打印最后一个元素
print('打印最后一个元素')
print(elements[-1])
print(padding)

def pointMessage():
    print('指定函数导入')
def importMessag():
    print("别名函数")