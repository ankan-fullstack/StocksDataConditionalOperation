from flask_restful import Api, Resource
from app import app
from .stocks import ReadCsvByName, RearrangeByOrder, HighestClosingPrice, MostVolatile

api = Api(app)
version = 'v1.0'

api.add_resource(ReadCsvByName,f"/api/{version}/readCsvByName")
api.add_resource(RearrangeByOrder,f"/api/{version}/rearrangeByOrder")
api.add_resource(HighestClosingPrice,f"/api/{version}/highestClosingPrice")
api.add_resource(MostVolatile,f"/api/{version}/mostVolatile")

