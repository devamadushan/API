import os

APP_ENV = os.getenv('APP_ENV', 'development')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'Deva')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'sio')
DATABASE_HOST = os.getenv('DATABASE_HOST', '8080')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'utilisateurs')
TEST_DATABASE_NAME = os.getenv('TEST_DATABASE_NAME', 'utilisateurs_test')

