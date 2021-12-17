from blueprints.user import UsersApi

def init_routes(api):
	api.add_resource(UsersApi, "/api/users")