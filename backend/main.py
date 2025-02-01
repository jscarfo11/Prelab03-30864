

from database import db
from mobile import mobile_request_setup

def main():
    db_connection = db()
    # implement the rest of the function here

    if db_connection == "database connection":
        print("Database connection successful")
        mobile = mobile_request_setup()
    else:
        print("Database connection failed")
        


if __name__ == "__main__":
    main()