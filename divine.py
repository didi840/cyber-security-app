"""DIVINE ASUOMA SYSTEM DICTATE"""

import time


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"yes", "y"}:
            return True
        if answer in {"no", "n"}:
            return False
        print('Please answer "yes" or "no".')


def ask_brand(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"macbook", "windows"}:
            return answer
        print('Please enter "macbook" or "windows".')


def evaluate_score(system, update, brand, shared, fraud, hacking):
    score = 0
    score += 10 if system else 0
    score += 10 if update else 0
    score += 10 if brand == "macbook" else 0
    score += 10 if not shared else 0
    score += 10 if not fraud else 0
    score += 10 if not hacking else 0
    return score


def threat_level(score):
    if score >= 50:
        return "LOW", "EXCELLENT", "SECURE"
    if score >= 35:
        return "MEDIUM", "GOOD", "STABLE"
    return "HIGH", "AT RISK", "UNSAFE"


def build_report(system, update, brand, shared, fraud, hacking, score, level, rating, status):
    lines = [
        "DIVINE ASUOMA SYSTEM DICTATE REPORT",
        "====================================",
        f"System version 11: {'yes' if system else 'no'}",
        f"System updated: {'yes' if update else 'no'}",
        f"Brand: {brand}",
        f"Shared system: {'yes' if shared else 'no'}",
        f"Involved in fraud: {'yes' if fraud else 'no'}",
        f"Previously hacked: {'yes' if hacking else 'no'}",
        f"Score: {score}/60",
        f"Threat level: {level}",
        f"Rating: {rating}",
        f"System status: {status}",
        "====================================",
    ]

    if score >= 50:
        lines.append("Your system is in very good condition.")
    elif score >= 35:
        lines.append("Your system is reasonably safe, but review the areas marked.")
    else:
        lines.append("Your system may be at risk. Please improve security settings.")

    return "\n".join(lines)


def valid_filename(name):
    filename = name.strip()
    if not filename:
        return None
    if not filename.lower().endswith('.txt'):
        filename += '.txt'
    return filename


def save_report(report_text, filename=None):
    if filename is None:
        timestamp = time.strftime('%Y%m%d_%H%M%S')
        filename = f"divine_report_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as report_file:
        report_file.write(report_text)
    return filename


def run_scanner():
    print("DIVINE ASUOMA SYSTEM DICTATE")
    print("====================================")

    system = ask_yes_no("Is it an 11 version system? (yes/no) ")
    update = ask_yes_no("Is your system updated? (yes/no) ")
    brand = ask_brand("What is the brand of the system? (macbook/windows) ")
    shared = ask_yes_no("Is your system shared with other users? (yes/no) ")
    fraud = ask_yes_no("Has your system been used in a fraudulent act? (yes/no) ")
    hacking = ask_yes_no("Have you ever been hacked before? (yes/no) ")

    score = evaluate_score(system, update, brand, shared, fraud, hacking)

    print()
    print("Scanning 1.....")
    time.sleep(0.4)
    print("Scanning 2.........")
    time.sleep(0.4)
    print("Scanning 3 ..........")
    time.sleep(0.4)
    print("Scanning 4 ............")
    time.sleep(0.4)
    print("Done scanning.")
    print()

    level, rating, status = threat_level(score)
    report_text = build_report(system, update, brand, shared, fraud, hacking, score, level, rating, status)

    print(report_text)
    print()

    if ask_yes_no("Save this report to a file? (yes/no) "):
        filename_input = input("Enter a filename or press Enter to use the default: ").strip()
        filename = None
        if filename_input:
            validated = valid_filename(filename_input)
            if validated:
                filename = validated
            else:
                print("Invalid filename entered. Using default filename instead.")
        filename = save_report(report_text, filename)
        print(f"Report saved to {filename}")
    else:
        print("Report was not saved.")


if __name__ == "__main__":
    run_scanner()
            