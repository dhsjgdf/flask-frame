from apps.example.views import home


def register_blueprint(app):
    app.register_blueprint(home)
