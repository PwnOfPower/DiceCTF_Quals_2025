import time

# Define the range
start_timestamp = 1740000000  # Updated timestamp range
end_timestamp = int(time.time())  # Current timestamp

# Possible locales (updated list)
locales = ["LC_CT", "LC_ALL", "en_US"]
username = "hacker"

# Output file
output_file = "password_list.txt"

with open(output_file, "w") as f:
    for timestamp in range(start_timestamp, end_timestamp + 1):
        #seconds_mod_60 = timestamp % 60
        for locale in locales:
            password = f"{timestamp}{locale}{username}\n"
            f.write(password)

print(f"Password list generated: {output_file}")
