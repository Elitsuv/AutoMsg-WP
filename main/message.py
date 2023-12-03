# Import libraries
import pywhatkit

# Define recipient number and message
recipient_number = "[no.]"
message = "Hello from Python!"

#set time 24 hrs. format
time_hour = 00
time_min = 00

try:
    pywhatkit.sendwhatmsg(recipient_number, message, time_hour, time_min)
    print("Message sent successfully!")
except Exception as e:
    print(f"Error sending message: {e}")
