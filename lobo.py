from app import main

application = main.create_app('lobo')
if __name__ == "__main__":
    application.run()
