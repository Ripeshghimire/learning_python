# Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point 
# and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”

# def checkSpeed(speed):
#     count_Point = 0
#     if speed < 70:
#         print("Ok ")
#     if speed > 70 :
#         speed = speed - 70 
#         remaining_speed  = speed // 5 
#         print(remaining_speed)
#         points = remaining_speed  
#         print(f'The number of points you have gained is {points}')
#     if points > 12 :
#         print("Liscence suspended")

# checkSpeed(900)
