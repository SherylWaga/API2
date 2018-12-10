import os
from app.db_config import create_tables

from app import create_app
# config_name = os.getenvgit add ('APP_SETTINGS') #config_name="development"
app = create_app()

if __name__ == '__main__':
    create_tables
    app.run()
    