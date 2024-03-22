Used django and djangorestframework for this project

first i setup the database for setting up database i used pandas to load data from csv file and create objects and used bulk_create option so write in database

then i setup to get api endpoints one for getting banks and other for getting branch specific details

it approximately took around 3 hours to complete assignment

# setup
# install python3 and pip
# pip3 install -r requirements.txt
# go to localhost:8000 and click on setup database it will approximately take 2-3minutes because of inserting more than 1lac 27 thousand records

# hit endpoint /api/v1/getbanks/ to get bank details api
# hit endpoint /api/v1/ifsc/<ifsc code for branch>/ to get branch specific details

# to run tests run command python3 manage.py test

