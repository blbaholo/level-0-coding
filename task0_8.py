def number_to_time(number):
    hours=number//60
    minutes=number%60
    if 2<=number<=59:
        display_message="0 hours, {minutes} minutes". format(minutes=number)
        print(display_message)
    elif (minutes==1 and hours==1):
        print(str(hours) + " hour, " + str(minutes) + " minute ") 
    elif hours==1:
        print(str(hours) + " hour," + str(minutes) + " minutes ")
    elif minutes==1:
        print(str(hours) + " hours, " + str(minutes) + " minute ")
    else:
        print(str(hours) + " hours, " + str(minutes) + " minutes ")

number_to_time(15)
