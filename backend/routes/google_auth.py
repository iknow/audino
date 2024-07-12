from authlib.integrations.flask_client import OAuth
from flask import redirect, url_for, session, jsonify
from backend import app, db, redis_client
from backend.models import User
from flask_jwt_extended import create_access_token, get_jti

SCOPE = ['openid', 'https://www.googleapis.com/auth/userinfo.email',
         'https://www.googleapis.com/auth/userinfo.profile']

oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=app.config['GOOGLE_CLIENT_ID'],
    client_secret=app.config['GOOGLE_CLIENT_SECRET'],
    server_metadata_url=app.config['GOOGLE_DISCOVERY_URL'],
    client_kwargs={
        'scope': ' '.join(SCOPE),
    }
)


@app.route('/auth/google')
def google_login():
    redirect_uri = url_for('google_callback', _external=True)
    print(redirect_uri)
    return google.authorize_redirect(redirect_uri)


@app.route('/auth/callback')
def google_callback():
    token = google.authorize_access_token()
    user_info = google.parse_id_token(token)
    print(user_info)
    email = user_info['email']
    username = email.split('@')[0]

    user = User.query.filter_by(username=username).first()
    if not user:
        # Assuming role_id 2 isor regular users
        user = User(username=username, password=f"oauth:google", role_id=2)
        db.session.add(user)
        db.session.commit()

    is_admin = True if user.role.role == "admin" else False
    access_token = create_access_token(
        identity={
            "username": username,
            "is_admin": is_admin,
            "user_id":  user.id
        },
        fresh=True,
        expires_delta=app.config["JWT_ACCESS_TOKEN_EXPIRES"],
    )
    access_jti = get_jti(encoded_token=access_token)
    redis_client.set(access_jti, "false",
                     app.config["JWT_ACCESS_TOKEN_EXPIRES"] * 1.2)

    # Redirect to frontend with access token using hash fragment
    return redirect(f"/#access_token={access_token}")
