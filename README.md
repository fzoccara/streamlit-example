### Start project 

Create new virtual env

`python3 -m venv venv`

Enable the virtual env

`source venv/bin/activate`

Install requirements from requirements.txt

`pip install --extra-index-url https://pypi.fury.io/arrow-nightlies/ --prefer-binary --pre pyarrow`

`pip install --no-cache-dir -r requirements.txt`

Exit virtual environment

`deactivate`

Set Jupyter to use virtual env kernel instead of default one