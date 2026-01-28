import pywhatkit

phone_number = input("Enter phone number(+countrycode): ")
msg = input("Enter your message: ")
# hour = int(input("Enter hour(24-hour format): "))
# minute = int(input("Enter minute: "))

# pywhatkit.sendwhatmsg(phone_number, msg, hour, minute)
pywhatkit.sendwhatmsg_instantly(phone_number, msg, wait_time=45, tab_close=False)

print("Message scheduled successfully ")


