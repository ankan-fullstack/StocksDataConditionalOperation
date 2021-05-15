The challenge is to develop a Python application with core features which perform the conditional operations on the given dataset.

    Technology Stack - Python, Flask, Pandas
    
    For running it on your local system please use these commands.

    pip install -r requirements.txt
    python app.py


    The "unprocessedFiles" stores the file which contains the dataset. And "processedFiles" folder contains the processed files which will be generated after the api call. 


    --Read the data from the CSV input file
    Open "api/stocks.py"
    Class Global Functions has a global function which reads the data from CSV file and return a Pandas dataframe.

    dataframe = readCsv(<filename>)



    --Write function 1 to retrieve stocks data sorted by company name by default

    API Endpoint =  POST <Hostname>/api/v1.0/readCsvByName

                    Content-Type: 'application/json'
	                fileName=test.csv

    Sample Input = {
	                    "fileName": "test.csv"
                    }



    --Write the second function which accepts input parameters to sort the stock data in ascending/descending order of company name or date range

    API Endpoint =  POST <Hostname>/api/v1.0/rearrangeByOrder

                    Content-Type: 'application/json'
	                fileName=test.csv
	                &sortBy=Name            # Name/date
	                &fromDate=2014-08-04 
	                &toDate=2015-02-09
	                &orderBy=desc           # asc/desc

    Sample Input = {
	                    "fileName": "test.csv",
	                    "sortBy": "Name",
	                    "fromDate": "2014-08-04", 
	                    "toDate" : "2015-02-09",
	                    "orderBy" : "desc"
                    }



    --Write a third function which retrieves the highest close value. Take company name and date range as input & return the highest close value in particular date range of the company

    API Endpoint =  POST <Hostname>/api/v1.0/highestClosingPrice

                    Content-Type: 'application/json'
	                fileName=test.csv
	                &name=AAL
	                &fromDate=2014-08-04 
	                &toDate=2015-02-09

    Sample Input = {
	                    "fileName": "test.csv",
	                    "name": "AAL",
	                    "fromDate": "2014-08-04", 
	                    "toDate" : "2015-02-09"
                    }

    --Find the most volatile company stock on a given date (Volatile stocks are those which have huge differences between 'open' & 'close' value)

    API Endpoint =  POST <Hostname>/api/v1.0/mostVolatile

                    Content-Type: 'application/json'
	                fileName=test.csv
	                &fromDate=2014-08-04 
	                &toDate=2015-02-09

    Sample Input = {
	                    "fileName": "test.csv",
	                    "fromDate": "2014-08-04", 
	                    "toDate" : "2015-02-09"
                    }

    --Output the results from the function into a CSV

    All of the api's stores a output csv file in "processedFile" folder on the root directory.