import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
    """CREATE TABLE IF NOT EXISTS PERSON (
        ID SERIAL PRIMARY KEY, 
        NAME VARCHAR(50) UNIQUE NOT NULL, 
        AGE INTEGER, 
        GENDER VARCHAR(10), 
        HEIGHT INTEGER, 
        WEIGHT INTEGER
        )""",
    """CREATE TABLE IF NOT EXISTS JOBTITLES (
        ID SERIAL PRIMARY KEY, 
        JOBNAME VARCHAR(50) UNIQUE NOT NULL, 
        IS_EXECUTIVE BOOLEAN DEFAULT FALSE, 
        DEPARTMENT VARCHAR(20), 
        IS_ACTIVE BOOLEAN DEFAULT FALSE, 
        TO_BE_HIRED DEFAULT FALSE
        )""",
    """CREATE TABLE IF NOT EXISTS LEVEL (
        ID SERIAL PRIMARY KEY, 
        LEVELNAME VARCHAR(50) UNIQUE NOT NULL,
        EXPERIENCE_YEAR_NEEDED INTEGER,
        BONUS_SALARY INTEGER,
        IS_DIRECTOR BOOLEAN DEFAULT FALSE,
        IS_MANAGER BOOLEAN DEFAULT FALSE
        )""",
    """CREATE TABLE IF NOT EXISTS WORKCHART (
        PERSONID INTEGER REFERENCES PERSON (ID), 
        JOBID INTEGER REFERENCES JOBTITLES (ID), 
        LEVELID INTEGER REFERENCES LEVEL (ID), 
        SALARY INTEGER, 
        FOOD_BUDGET INTEGER,
        TOTAL_YEARS_WORKED INTEGER,
        YEARS_IN_COMPANY INTEGER,
        QUALIFIES_FOR_PENSION BOOLEAN DEFAULT FALSE,
        PRIMARY KEY (PERSONID))""",
    """CREATE TABLE IF NOT EXISTS SERVICE (
        ID SERIAL PRIMARY KEY, 
        TOWN VARCHAR(20), 
        CAPACITY INTEGER,
        CURRENT_PASSENGERS INTEGER,
        LICENCE_PLATE VARCHAR(15),
        DEPARTURE_HOUR VARCHAR(5)
        )""",
    """CREATE TABLE IF NOT EXISTS TRANSPORTATION (
        PERSONID INTEGER REFERENCES PERSON (ID),
        SERVICEID INTEGER REFERENCES SERVICE (ID), 
        USES_IN_MORNING BOOLEAN DEFAULT FALSE,
        USES_IN_EVENING BOOLEAN DEFAULT FALSE,
        SEAT_NUMBER INTEGER,
        SERVICE_FEE INTEGER,
        STOP_NAME VARCHAR(15),
        PRIMARY KEY (PERSONID))""",
]


def initialize(url):
    with dbapi2.connect(url) as connection: #connection context manager
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
