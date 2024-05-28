# infer

demo of flask -> streamlit microservice for cloud inference

#Commands to run applications:
Terminal 1: Run the Flask application
python flask_app.py

Terminal 2: Run the Streamlit application
streamlit run streamlit_app.py

#Setup dev environment
(base) max@laurie-latitude:~/infer$ python -m venv infenv
pip install flask streamlit requests influxdb pandas

Step 2: Set Up Your Development Environment

    Clone Your GitHub Repository Locally
        In Visual Studio Code, clone your GitHub repository:

        bash

    git clone https://github.com/your-username/iot-dashboard.git
    cd iot-dashboard

Create and Activate a Virtual Environment

bash

python3 -m venv venv
source venv/bin/activate

Install Dependencies

bash

pip install flask streamlit requests influxdb

Add a requirements.txt File

bash

pip freeze > requirements.txt

Push Changes to GitHub

bash

    git add .
    git commit -m "Initial setup"
    git push origin main

Step 3: Set Up the VM for Continuous Deployment

    Clone the Repository on the VM

    bash

git clone https://github.com/your-username/iot-dashboard.git
cd iot-dashboard

Install Python and Dependencies on the VM

bash

sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


#run apps
nohup python flask_app.py &
nohup streamlit run streamlit_app.py --server.port 8501 &