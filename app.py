from app import AppFactory

application = AppFactory.create_app()

if __name__ == '__main__':
    application.run(debug=True)
