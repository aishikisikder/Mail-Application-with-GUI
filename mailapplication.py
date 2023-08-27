#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your password
    recipient_email = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", "end")

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "plain"))

        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()

        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI setup
root = tk.Tk()
root.title("Simple Email Application")

recipient_label = tk.Label(root, text="Recipient Email:")
recipient_label.pack()

recipient_entry = tk.Entry(root)
recipient_entry.pack()

subject_label = tk.Label(root, text="Subject:")
subject_label.pack()

subject_entry = tk.Entry(root)
subject_entry.pack()

message_label = tk.Label(root, text="Message:")
message_label.pack()

message_text = tk.Text(root, height=10, width=50)
message_text.pack()

send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.pack()

root.mainloop()


# In[ ]:




