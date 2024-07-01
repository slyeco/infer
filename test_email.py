import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

# Email alert configuration
EMAIL_ADDRESS = 'sly@sly.eco'
EMAIL_PASSWORD = 'zypa rmea xpjp rura'
ALERT_RECIPIENT = 'max@sly.eco'
ALERT_THRESHOLD = 12.5
ALERT_COOLDOWN = timedelta(minutes=30)
last_alert_time = datetime.min

def send_test_email():
    global last_alert_time
    pm2e5_value = 13.0  # Test value exceeding the threshold for demonstration

    msg = MIMEText(f"Alert: pm2e5 value exceeded threshold! Current value: {pm2e5_value}")
    msg['Subject'] = 'PM2.5 Alert Test'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ALERT_RECIPIENT

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, ALERT_RECIPIENT, msg.as_string())
        print("Test email sent successfully!")
    except Exception as e:
        print(f"Failed to send test email: {e}")

if __name__ == '__main__':
    send_test_email()
