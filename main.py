import qrcode
import csv
import os
from datetime import datetime

import qrcode.constants

# Paths
QR_Codes_Folder = "qr_codes"
Log_File = "scan_logs.csv"

# Check All Folders And Files Exist
os.makedirs(QR_Codes_Folder, exist_ok=True)
if not os.path.exists(Log_File):
    with open(Log_File, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Activity", "Device Type"]) # Headers for the log file

# Menu Options
def menu():
    print("n--- Resume and Social QR Code Generator ---")
    print("1. Generate QR Code for Resume")
    print("2. Generate QR Code for Social Links")
    print("3. Generate Both QR Codes (for Resume and Social Links)")
    print("4. Log Scan Activity")
    print("5. Exit")

# Generate A QR Code And Save It To The qr_codes Folder
def generate_qr(data, filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4, )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", black_color="white")
    img_path = os.path.join(QR_Codes_Folder, filename)
    img.save(img_path)
    print(f"QR Code Saved To {img_path}")

# Log Scan Activity Of Resume/Socials QR Code to scan_logs.csv
def log_scan(activity, device_type):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(Log_File, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, activity, device_type])
    print(f"Logged Activity: {activity}, Device: {device_type}, Timestamp {timestamp}")

#Main
def main():
    while True:
        menu()
        choice = input("Enter Your Choice: ").strip()
        
        if choice == "1":
            while True:
                resume_url = input("Enter the URL for Your Resume (or type 'back' to return to the main menu): ").strip()
                if resume_url.lower() == "back":
                    break
                generate_qr(resume_url, "resume_qr.png")
                print("Resume QR Code generated successfully!\n")
                break  # Exit the loop after generating

        elif choice == "2":
            while True:
                social_links = input("Enter the URL for Your Social Links (or type 'back' to return to the main menu): ").strip()
                if social_links.lower() == "back":
                    break
                generate_qr(social_links, "social_qr.png")
                print("Social Links QR Code generated successfully!\n")
                break  # Exit the loop after generating

        elif choice == "3":
            while True:
                resume_url = input("Enter the URL for Your Resume (or type 'back' to return to the main menu): ").strip()
                if resume_url.lower() == "back":
                    break
                social_links = input("Enter the URL for Your Social Links (or type 'back' to return to the main menu): ").strip()
                if social_links.lower() == "back":
                    break
                generate_qr(resume_url, "resume_qr.png")
                generate_qr(social_links, "social_qr.png")
                print("Both QR Codes generated successfully!\n")
                break  # Exit the loop after generating

        elif choice == "4":
            while True:
                activity = input("Enter the activity type (e.g., Resume, Social Links) (or type 'back' to return to the main menu): ").strip()
                if activity.lower() == "back":
                    break
                device_type = input("Enter the device type (e.g., Mobile, Tablet, Desktop) (or type 'back' to return to the main menu): ").strip()
                if device_type.lower() == "back":
                    break
                log_scan(activity, device_type)
                print("Activity logged successfully!\n")
                break  # Exit the loop after logging

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    
if __name__ == "__main__":
    main()