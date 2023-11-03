from datetime import datetime
import pytz  # for time zone information

# Get the current date and time
current_datetime = datetime.now()

# Format the date as per the specified format
formatted_date = current_datetime.strftime("%a %b %d %H:%M:%S %Z %Y")

# Get the time zone information (here, 'IST' for Indian Standard Time)
time_zone = pytz.timezone('Asia/Kolkata')  # 'Asia/Kolkata' is the time zone for IST
current_time_in_ist = current_datetime.astimezone(time_zone).strftime("%Z")

# Print the formatted date with time zone
print(formatted_date.replace("IST", current_time_in_ist))
