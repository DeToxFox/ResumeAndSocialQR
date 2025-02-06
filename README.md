# ResumeAndSocialQR

ResumeAndSocialQR is a command-line tool for generating personalized QR codes for your resume and social links. Designed for professional networking and conferences, it includes features to log scan activity while respecting user privacy. The project is ideal for private use but can be extended to support public-facing applications with backend integration.

## Features

- **Multi-QR Generation**:
  - Generate QR codes for your resume, social links, or both.
  - Save QR codes with meaningful filenames in a dedicated folder.
- **Flexible File Management**:
  - Prompts users to overwrite existing files or create uniquely named files for each QR code.
- **Scan Activity Logging**:
  - Log timestamps, activity types (e.g., Resume, Social Links), and device types (e.g., Mobile, Tablet, Desktop).
  - Logs are saved in a CSV file for easy analysis.
- **Privacy-Focused**:
  - No IP addresses or personal identifiers are collected.
- **Future Expansion**:
  - Plans to add a user-friendly desktop or web-based UI.
  - Backend integration for real-time scan logging and analytics.

## How It Works

1. Use the menu-driven interface to:
   - Generate QR codes for your resume, social links, or both.
   - Log scan activity manually.
   - View saved logs and QR codes.
2. Share your QR codes at networking events or conferences.
3. Analyze scan data stored in `scan_logs.csv` to measure engagement.

## Setup

### Prerequisites

- Python 3.7+ installed on your system.
- A publicly accessible URL for your resume (e.g., Google Drive, Dropbox, or a personal website).

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/ResumeAndSocialQR.git
   cd ResumeAndSocialQR
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv .venv
   ```

   - **Windows:**
     ```bash
     .\.venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Run the script**:

   ```bash
   python main.py
   ```

2. **Choose from the menu options**:

   - Generate a QR code for your resume.
   - Generate a QR code for your social links.
   - Generate both QR codes in one session.
   - Log scan activity (timestamp, activity type, device type).
   - Exit the application.

### Data Storage

- **QR Codes:**
  - Saved in the `qr_codes/` folder.
  - Example: `resume_qr.png`, `social_qr.png`

- **Scan Logs:**
  - Saved in `scan_logs.csv`.
  - Example format (CSV):

    ```csv
    Timestamp,Activity,Device Type
    2025-01-22 12:00:00,Resume,Mobile
    2025-01-22 12:05:00,Social Links,Desktop
    ```

## Example Workflow

1. Generate a QR code for your resume and share it at a networking event.
2. Log scan activity manually, noting when and on which device type the QR code was scanned.
3. Use the log file to analyze engagement.

## Future Plans

### UI Development

- **Frontend Expansion:**
  - Add a user-friendly interface (desktop or web-based) to manage QR codes and view scan logs.
- **Backend Integration:**
  - Automate logging by creating backend endpoints that record scan events when a QR code is accessed.
  - Store data in a database and track additional metadata such as user agents (e.g., browser type, device).
- **Advanced Analytics:**
  - Display scan statistics in real-time using visualizations, such as charts and tables, accessible through the frontend.

### Advanced Logging

- Automate scan logging directly from QR code scans without manual input.
- Consider using third-party services (e.g., Google Analytics, Bitly) for enhanced tracking if a backend isn't developed.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Note

This is a private project intended for personal use. Contributions are not currently invited but may be considered in the future as the project expands.
