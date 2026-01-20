print("==windows System Check ===")
hostname = input("Enter Hostname: ")
print("Begining System Scan of:", hostname)

ram =int(input("How much Ram (GB) is installed? "))
print("Half of RAM for test:", ram / 2)

uptime = int(input("how many days ago did you last restart?"))
hours = uptime * 24
print("uptime hours:", hours)

age = int(input("Enter age:"))

age = 47
attempts = int(input("Enter number of login attempts:"))
if attempts > 3:

    print("Account Locked")
else:
    print("Access allowed")
for i in range(3):
    print("Scanning System...")    