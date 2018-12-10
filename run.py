import os
from app.db_config import create_tables

from app import create_app

app = create_app()

if __name__ == '__main__':
    create_tables
    app.run()
    
