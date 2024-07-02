import unittest
from flask_app import send_email_alert

class TestIntegrationFlaskApp(unittest.TestCase):

    def test_actual_send_email_alert(self):
        # Set up test data
        pm2e5_value = 18
        deveui = '3A6E00000000A017'
        
        # Call the function
        send_email_alert(pm2e5_value, deveui)
        print("Email sent. Check your inbox to verify.")
        
if __name__ == '__main__':
    unittest.main()
