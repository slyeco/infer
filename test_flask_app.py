import unittest
from unittest.mock import patch
from flask_app import send_email_alert, update_device_parameters, appEUI

class TestFlaskApp(unittest.TestCase):
    
    @patch('smtplib.SMTP_SSL')
    def test_send_email_alert(self, mock_smtp):
        # Set up test data
        pm2e5_value = 18
        deveui = 'test_deveui'

        # Call the function
        send_email_alert(pm2e5_value, deveui)

        # Check if the SMTP server was called correctly
        mock_smtp.assert_called_with('smtp.gmail.com', 465)
        instance = mock_smtp.return_value
        instance.login.assert_called_with('sly@sly.eco', 'zypa rmea xpjp rura')
        instance.sendmail.assert_called_once()
        args = instance.sendmail.call_args[0]
        self.assertIn('max@sly.eco', args[1])
        self.assertIn('davide@sly.eco', args[1])
        self.assertIn('Alert: pm2e5 value exceeded threshold for sensor test_deveui! Current value: 18', args[2])

    @patch('urllib.request.urlopen')
    def test_update_device_parameters(self, mock_urlopen):
        # Test updating smk to 90
        params_to_update = [('smk', 90)]
        update_device_parameters(appEUI, 'test_deveui', params_to_update)
        
        # Verify the correct URL and data were used
        expected_url = f"http://15.160.194.92:58089/api/application/{appEUI}/nodes/test_deveui/tag/smk/value"
        expected_data = b'{"value": 90}'
        mock_urlopen.assert_called()
        request_instance = mock_urlopen.call_args[0][0]
        self.assertEqual(request_instance.full_url, expected_url)
        self.assertEqual(request_instance.data, expected_data)

        # Test updating smk to None
        params_to_update = [('smk', None)]
        update_device_parameters(appEUI, 'test_deveui', params_to_update)
        
        # Verify the correct URL and data were used
        expected_data = b'{"value": null}'
        mock_urlopen.assert_called()
        request_instance = mock_urlopen.call_args[0][0]
        self.assertEqual(request_instance.full_url, expected_url)
        self.assertEqual(request_instance.data, expected_data)

if __name__ == '__main__':
    unittest.main()
