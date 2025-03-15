from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import grpc
import api.requests.v1.requests_pb2 as requests_pb2
import api.requests.v1.requests_grpc as requests_grpc

app = Flask(__name__)
api = Api(app)

class RequestsResource(Resource):
    def get(self):
        # Placeholder for fetching request list
        return jsonify({"requests": []})

    def post(self):
        data = request.json
        request_obj = requests_pb2.Request(id="123", data=data["data"], created_at="2025-02-26")
        return jsonify({"id": request_obj.id, "data": request_obj.data, "created_at": request_obj.created_at})

class RequestResource(Resource):
    def post(self, request_id):
        data = request.json
        request_obj = requests_pb2.Request(id=request_id, data=data["data"], created_at="2025-02-26")
        return jsonify({"id": request_obj.id, "data": request_obj.data})

class RequestStatusResource(Resource):
    def get(self, request_id):
        status_obj = requests_pb2.RequestStatus(id=request_id, status="pending")
        return jsonify({"id": status_obj.id, "status": status_obj.status})

class HealthResource(Resource):
    def get(self):
        return jsonify("ok")

api.add_resource(RequestsResource, "/requests")
api.add_resource(RequestResource, "/requests/<string:request_id>")
api.add_resource(RequestStatusResource, "/requests/<string:request_id>/status")
api.add_resource(HealthResource, "/health")


if __name__ == "__main__":
    app.run(debug=True)
