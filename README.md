# ResumeAndSocialQR
A command-line tool to generate QR codes for your resume and social links, with logging for timestamps, activity types, and device types. Privacy-focused and ideal for professional networking. Future plans include adding a user-friendly UI for broader accessibility.


# ResumeAndSocialQR

ResumeAndSocialQR is a command-line tool for generating personalized QR codes for your resume and social links. Designed for professional networking and conferences, it includes features to log scan activity while respecting user privacy. Future plans include a user-friendly UI to expand accessibility.

## Features
- **Multi-QR Generation**:
  - Generate QR codes for your resume, social links, or both.
  - Save QR codes with meaningful filenames in a dedicated folder.
- **Scan Activity Logging**:
  - Log timestamps, activity types (e.g., Resume, Social Links), and device types (e.g., Mobile, Tablet, Desktop).
  - Logs are saved in a CSV file for easy analysis.
- **Privacy-Focused**:
  - No IP addresses or personal identifiers are collected.
- **Future Expansion**:
  - Plans to add a user-friendly desktop or web-based UI.

## How It Works
1. Use the menu-driven interface to generate QR codes or log scan activity.
2. Share your QR codes at networking events or conferences.
3. Analyze scan data stored in `scan_logs.csv` to measure engagement.

## Setup
### Prerequisites
- Python 3.7+ installed on your system.
- A publicly accessible URL for your resume (e.g., Google Drive, Dropbox, or a personal website).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ResumeAndSocialQR.git
   cd ResumeAndSocialQR
   ```
2. Install the required library:
   ```bash
   pip install qrcode[pil]
   ```

### Running the Application
1. Run the script:
   ```bash
   python main.py
   ```
2. Choose from the menu options:
   - Generate a QR code for your resume.
   - Generate a QR code for your social links.
   - Generate both QR codes in one session.
   - Log scan activity (timestamp, activity type, device type).
   - Exit the application.

## File Outputs
- **QR Codes**: Saved in the `qr_codes/` folder.
  - Example: `resume_qr.png`, `social_qr.png`
- **Scan Logs**: Saved in `scan_logs.csv`.
  - Example format:
    ```csv
    Timestamp,Activity,Device Type
    2025-01-22 12:00:00,Resume,Mobile
    2025-01-22 12:05:00,Social Links,Desktop
    ```

## Example Workflow
1. Generate a QR code for your resume and share it at a networking event.
2. Log scan activity, noting when and on which device type the QR code was scanned.
3. Use the log file to analyze engagement.

## Future Plans
- **UI Development**: Add a user-friendly interface (desktop or web-based).
- **Advanced Analytics**: Summarize daily and device-based scan counts within the app.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Note
This is a private project intended for personal use. Contributions are not currently invited, but the project may become public in the future once additional features, such as a UI, are implemented.

