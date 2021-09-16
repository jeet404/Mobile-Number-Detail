import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileno = input("Enter Mobile Number with Country Code : ")
mobileno = phonenumbers.parse(mobileno)

# timezone of phone number
print(timezone.time_zones_for_number(mobileno))

# carrier of phone number
print(carrier.name_for_number(mobileno,"en"))

# region information
print(geocoder.description_for_number(mobileno,"en"))

# validating a phone number
print("Valid Mobile Number : ",phonenumbers.is_valid_number(mobileno))

# possibilty of a number
print("Possibility of a Number : ",phonenumbers.is_possible_number(mobileno))