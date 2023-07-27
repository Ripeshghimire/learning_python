
# # #Nested Loop 
# for i in range(1,13):
#     print("===================")
#     for j in range(1,11):
#         print(f'{i} * {j} ={(i*j)}')

# value1  = [1,2,4,5,6]
# value2 = [2,4,6,8,10]
# #wap to find the combinations of value1 and value 2 
# for i in value1:
#     for j in value2:
#         print(f'({i},{j})' )

myArray=[
    ["Ram","Shyam","Hari","Gopal"],
    ["Radhe","Sita","Geeta","Rita"]
]
for name in myArray:
    # print(name)
    for name1 in name:
        print(f'The name is  {name1}')