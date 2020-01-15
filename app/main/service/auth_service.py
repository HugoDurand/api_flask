from app.main.model.user import User
from ..service.blacklist_service import save_token


class Auth:

    @staticmethod
    def login_user(email, password):
        try:
            user = User.query.filter_by(email=email).first()
            if user and user.check_password(password):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    return auth_token.decode()
            else:
                raise Exception('email or password does not match.')

        except Exception as e:
            print(e)
            raise Exception('Try again')


    @staticmethod
    def logout_user(token):
        if token:
            auth_token = token.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                return save_token(token=auth_token)
            else:
                raise Exception('fail')
        else:
            raise Exception('Provide a valid auth token.')
  
    
    @staticmethod
    def get_logged_in_user(new_request):
            # get the auth token
            auth_token = new_request.headers.get('Authorization')
            if auth_token:
                resp = User.decode_auth_token(auth_token)
                if not isinstance(resp, str):
                    user = User.query.filter_by(id=resp).first()
                    response_object = {
                        'status': 'success',
                        'data': {
                            'user_id': user.id,
                            'email': user.email,
                            'admin': user.admin,
                            'registered_on': str(user.registered_on)
                        }
                    }
                    return response_object, 200
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Provide a valid auth token.'
                }
                return response_object, 401