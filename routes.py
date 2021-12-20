from api.user import UsersApi
from api.auth import SignupApi, LoginApi

def init_routes(api):
	api.add_resource(UsersApi, "/api/users")
	api.add_resource(SignupApi, "/api/auth/signup")
	api.add_resource(LoginApi, "/api/auth/login")