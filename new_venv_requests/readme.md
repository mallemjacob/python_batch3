# create the project folder
mkdir myproject

# change into the project folder
cd myproject

# create a virtual environment
Linux: python3 -m venv myenv
Windows: python -m venv myenv

# Activate the environment
source myenv/bin/activate

# Download 3rd party packages from pypi.org
pip install requests

# create a new file
touch app.py

# import modules in the app.py file
import requests

# run app.py python file
Linux: python3 app.py
Windows: python app.py