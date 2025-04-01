Dynamic QR Code Generator
Overview
The Dynamic QR Code Generator is an advanced web application that allows users to generate and customize QR codes for URLs with features such as:

Custom shapes and styles

Gradient colors

Logos and labels

Multi-URL redirection based on device type

Password protection and expiry dates

Scan tracking and analytics

Bulk QR code generation from CSV files

It also includes a user-friendly interface with real-time previews, download options, and QR code storage for future retrieval.

Features
1️⃣ Advanced QR Code Features
Custom Shapes & Styles – Customize the QR code’s eye shapes, patterns, and styles.

Gradient Colors – Choose gradient colors for the QR code.

Frame & Labels – Add decorative frames or labels around the QR code.

Multi-URL QR Code – Generate QR codes that redirect to different URLs based on conditions like device type or location.

Password-Protected QR Codes – Option to secure QR codes with a password.

QR Code Expiry & Auto-Deletion – Set expiry dates for QR codes and auto-delete them from the database.

2️⃣ Enhanced User Experience
Dark Mode Support – Switch between light and dark modes for a sleek UI.

Real-time Preview – View a live preview of the QR code before downloading.

Animated QR Codes – Generate QR codes as animated GIFs.

Bulk QR Code Generation – Upload a CSV file with multiple URLs and generate QR codes in bulk.

3️⃣ Security & Analytics
Scan Tracking & Analytics – Track the number of scans for each QR code.

Location-Based Analytics – Log scan locations based on IP geolocation.

Time-Based Analytics – View trends in QR code scans over time.

QR Code Access Logs – Capture details such as scan time and device information.

Webhook Integration – Send scan events to third-party applications via webhooks.

4️⃣ Storage & Sharing
User Authentication – Allow users to sign up and save their QR codes for future use.

Cloud Storage (Firebase/AWS) – Store QR codes in the cloud for easy retrieval.

Social Media Sharing – Easily share QR codes on social media platforms.

Dynamic URL Editing – Edit the URL of a QR code without regenerating the image.

Installation
Prerequisites
Python 3.x

Streamlit

pyshorteners

qrcode

Pillow

sqlite3 (for database functionality)

Steps to Install
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-repo/qr-code-generator.git
cd qr-code-generator
Create a virtual environment and activate it:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit application:

bash
Copy
Edit
streamlit run app.py
Open the application in your browser at http://localhost:8501.

How to Use
Enter URL: Paste the URL for which you want to generate the QR code.

Customize QR Code: Choose colors, size, and upload a logo if desired.

Set Expiry & Password Protection: Choose an expiry period for the QR code, and enable password protection if needed.

Generate QR Code: Click the button to generate your QR code.

Download & Share: Download the generated QR code or share it directly on social media.

Contributing
Contributions are welcome! If you want to contribute to this project, follow these steps:

Fork the repository.

Create your feature branch (git checkout -b feature-name).

Commit your changes (git commit -m 'Add new feature').

Push to the branch (git push origin feature-name).

Open a pull request.

License
THIS PROJECT IS OWNED BY DATTA MANAS