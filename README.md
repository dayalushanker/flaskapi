Please use the following steps

Step 1:- Create .env file in root directory and put following 

debug=True

export FLASK_APP = fapp.py

export FLASK_ENV = development

export FLASK_RUN_HOST=localhost

export FLASK_RUN_PORT=8888

Step 2:- Create virtual environment
 $virtualenv venv
 
Activate it by following commond
$ source venv/bin/activate

Step 3:- Install all the python library

pip3 install -r requrirements.txt


Step 4: Please set the Mysql database in config.py

Step 5: Finally use commond "flask run" enjoy ...


