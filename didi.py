import time

# ============================================

# IFYBUGSY CYBER SECURITY THREAT DETECTOR

# ============================================

print("=" * 50)

print("      IFYBUGSY CYBER SECURITY CENTER")

print("        COMPUTER SECURITY SCANNER")

print("=" * 50)

# Function to get yes/no input

def get_yes_no(question):

    while True:

        answer = input(question + " (yes/no): ").strip().lower()

        if answer == "yes":

            return True

        elif answer == "no":

            return False

        else:

            print("Please enter only yes or no.")

# Employee Information

employee = input("\nEmployee Name: ")

antivirus = get_yes_no("Is Antivirus Installed?")

firewall = get_yes_no("Is Firewall Enabled?")

updated = get_yes_no("Is Windows Updated?")

mfa = get_yes_no("Is Multi-Factor Authentication (MFA) Enabled?")

shared = get_yes_no("Is the Computer Shared with Other People?")

password = input("Enter your password: ")

# ============================================

# PASSWORD CHECK

# ============================================

strong_password = False

if len(password) >= 8:

    has_number = False

    has_upper = False

    for char in password:

        if char.isdigit():

            has_number = True

        if char.isupper():

            has_upper = True

    if has_number and has_upper:

        strong_password = True

# ============================================

# SECURITY SCORE

# ============================================

score = 0

if antivirus:

    score += 20

if firewall:

    score += 20

if updated:

    score += 20

if strong_password:

    score += 20

if mfa:

    score += 20

# Shared computer reduces security

if shared:

    score -= 20

# Keep score between 0 and 100

if score < 0:

    score = 0

if score > 100:

    score = 100

# ============================================

# THREAT LEVEL

# ============================================

if score >= 90:

    threat = "SAFE"

    status = "EXCELLENT SECURITY"

elif score >= 70:

    threat = "MEDIUM"

    status = "NEEDS IMPROVEMENT"

else:

    threat = "HIGH RISK"

    status = "IMMEDIATE ACTION REQUIRED"

# ============================================

# SCANNING ANIMATION

# ============================================

print("\nScanning...")

for i in range(1, 6):

    print(f"Scanning...{i}")

    time.sleep(0.5)

# ============================================

# REPORT

# ============================================

print("\n" + "=" * 40)

print("        SECURITY REPORT")

print("=" * 40)

print(f"Employee: {employee}")

print(f"Antivirus Installed : {antivirus}")

print(f"Firewall Enabled    : {firewall}")

print(f"Windows Updated     : {updated}")

print(f"Strong Password     : {strong_password}")

print(f"MFA Enabled         : {mfa}")

print(f"Shared Computer     : {shared}")

print("-" * 40)

print(f"Security Score : {score}")

print(f"Threat Level   : {threat}")

print(f"System Status  : {status}")

print("=" * 40)