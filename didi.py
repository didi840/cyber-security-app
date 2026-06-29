name = input("employee name: ")
antivirus = input("antivirus installed (yes/no): ")
firewall = input("firewall enabled (yes/no): ")
update = input("system updated (yes/no): ")
mfa = input("mfa enabled (yes/no): ")
password = input("enter password: ")
computer = input("is the system shared with other people (yes/no): ")

score = 0

if antivirus == "yes":
    score += 20
if firewall == "yes":
    score += 20
if update == "yes":
    score += 20
if mfa == "yes":
    score += 20
if len(password) >= 8:
    score += 20
if computer == "no":
    score += 20    
print("scanning....")

if score >= 80:
    print("\n SECURITY REPORT")
    print("employee:", name)
    print("score:",score)
    print("threat level: LOW")
    print("status: EXCELLENT")