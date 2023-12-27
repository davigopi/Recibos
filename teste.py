# # arqListValue = open('listValue', 'r')
# arqListValue = open('listValue.txt', 'r')
# print(str(arqListValue))
# n = 10
# x = 0
# lista = [ (x+=1) for _ in range(n)]

# print(lista)
from connect import Connect


import ast


connect = Connect()

with open('listValue.txt', "r") as arquivo:
	listValue = arquivo.read()


listValue = ast.literal_eval(listValue)

connect.removeEmpty = listValue
listValue = connect.removeEmpty
connect.addNone = listValue
listValue = connect.addNone
connect.addEndValue = listValue
listValue = connect.addEndValue
connect.formatLineToColumn = listValue
listValue = connect.formatLineToColumn
# listValue = connect.formatListEqualValueLineTable(listValue=listValue)

# print(listValue)


for value in listValue:
	print(value)
	# for x in value:
	#     print(x)
# listValue = listValue.split()
# listValue = listValue.replace('"', '')
# 
# listValue = list(listValue)

# def noEmpty(x):
#     return x != ""
# # str = '0.4350    0.8798    0.0099         1';
# print (list(filter(noEmpty, listValue.split(" "))));



# print(listValue, type(listValue))