from lib.server.api.user import UsersApi
from lib.server.api.auth import SignupApi, LoginApi
from lib.server.api.inference import InferenceApi

def init_routes(api):
	api.add_resource(UsersApi, "/api/users")
	api.add_resource(SignupApi, "/api/auth/signup")
	api.add_resource(LoginApi, "/api/auth/login")
	api.add_resource(InferenceApi, "/api/inference")