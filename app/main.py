from flask import Flask
from flask_restplus import Resource, Api
from app import app,api

ns = api.namespace('helloworld', description='Operations related to Hello World')

@ns.route('/get')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    