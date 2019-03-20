This will help you install and be able to run the system:

1. For the UI to work, you need internet
2. Internet will be used to pull current data from yahoo
3. [Click here to download stock data from yahoo](https://finance.yahoo.com/quote/DATA/history?p=DATA)
4. Add the DATA.csv to the stock-forecasting-js/data folder
5. You can also use a small data file from the same site to predict prices
6. Cd into the directory where you've downloaded the file eg. cd [name of project]
7. [ls] to view the the files in the folder
8. Make sure you can see [manage.py]
9. run [py manage.py makemigrations] to make migrations
10. run [py manage.py migrate] to migrate the tables
11. run [py manage.py runserver] to run the server
12. If the server starts visit [here](http://127.0.0.1:8000/)
13. Login to the website and start monitoring

How To:

1. Once logged inn click upload data and upload the data downloaded
2. Make sure you upload the right .csv file and click Suggest
3. On Suggest change [1000] to [2000] and [max buy unit] to 10 then click [Train]
4. Wait for the training to take place as computer may fail to respond
5. The view all the predictions below


Remember:
* Download large data that will be used to train the Bot

* Life is short
* Be nice to people, they

Alternatively,

* You can use javascript to display images produced
* Learn python language
