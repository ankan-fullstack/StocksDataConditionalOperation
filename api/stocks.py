from flask import Flask, request, Response
from flask_restful import Resource
import pandas as pd

class GlobalFunctions():
    global readCsv
    def readCsv(fileName):
        chunk = pd.read_csv(f'./unprocessedFiles/{fileName}',chunksize=100000)
        df = pd.concat(chunk)
        return df

class ReadCsvByName(Resource):
    def post(self):
        #Retrieve Parameters
        json_data = request.get_json(force=True)

        fileName = json_data['fileName']

        pdDf = readCsv(fileName)                                                                #Reads CSV
        pdDf.sort_values(by='Name',inplace=True,ascending=True)                                 #Sorting Value by Name
        pdDf.to_csv(path_or_buf=f'./processedFiles/processed_{fileName}_readCsvByName.csv')     #Saving the file in local storage temporarily

        return Response(pdDf.to_json(orient='records', lines=True).splitlines(),mimetype='application/json',status=200)

class RearrangeByOrder(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        fileName = json_data['fileName']
        sortBy = json_data['sortBy']

        order = True
        if json_data['orderBy']=='desc':
            order = False

        pdDf = readCsv(fileName)                                                     
        pdDf.sort_values(by=sortBy,inplace=True,ascending=order)
        pdDf.to_csv(path_or_buf=f'./processedFiles/processed_{fileName}_rearrangeByOrder_{sortBy}.csv')       #Saving the file in local storage temporarily
   
        
        return Response(pdDf.to_json(orient='records', lines=True).splitlines(),mimetype='application/json',status=200)

class HighestClosingPrice(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        fileName = json_data['fileName']
        fromDate = json_data['fromDate']
        toDate = json_data['toDate']
        stockName = json_data['name']

        pdDf = readCsv(fileName)
        pdDf['date'] = pd.to_datetime(pdDf['date'])
        tempDf = pdDf[(pdDf["date"].isin(pd.date_range(fromDate, toDate))) & (pdDf['Name'] == stockName)]

        tempDf['date'] = tempDf['date'].astype(str)
        tempDf = tempDf[tempDf['close']==tempDf['close'].max()]
        if len(tempDf)==0:
            return Response('{"Message" : "No records Found"}',mimetype='application/json',status=200)
        tempDf.to_csv(path_or_buf=f'./processedFiles/processed_{fileName}_HighestClosingPrice_{stockName}.csv')
        return Response(tempDf.to_json(orient='records', lines=True).splitlines(),mimetype='application/json',status=200)
        
class MostVolatile(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        fileName = json_data['fileName']
        fromDate = json_data['fromDate']
        toDate = json_data['toDate']

        pdDf = readCsv(fileName)
        pdDf['date'] = pd.to_datetime(pdDf['date'])
        tempDf = pdDf[pdDf["date"].isin(pd.date_range(fromDate, toDate))]
        tempDf['volatileValue'] = (tempDf['close']-tempDf['open']).abs()
        tempDf = tempDf[tempDf['volatileValue']==tempDf['volatileValue'].max()]
        
        del tempDf['volatileValue']
        tempDf['date'] = tempDf['date'].astype(str)

        tempDf.to_csv(path_or_buf=f'./processedFiles/processed_{fileName}_mostVolatile_{fromDate}to{toDate}.csv')
        return Response(tempDf.to_json(orient='records', lines=True).splitlines(),mimetype='application/json',status=200)



