# ku-polls
[![Build Status](https://app.travis-ci.com/TaninDean/ku-polls.svg?branch=iteration2)](https://app.travis-ci.com/TaninDean/ku-polls)
[![codecov](https://codecov.io/gh/TaninDean/ku-polls/branch/main/graph/badge.svg?token=4JD0USTMF1)](https://codecov.io/gh/TaninDean/ku-polls)

Ku polls is a process to get comment from ku stuff or sutdent. The data from ku polls will be analyze to for making decision of event
or learning other preference idea.

The Polls will be of any sort, including Google Forms and SurveyMonkey, and will not be limited to internet polling.
### Install Packages
1. Clone this project repository to your machine.

    ```
    git clone https://github.com/TaninDean/ku-polls.git
    ```
2. Get into the directory of this repository.

    ```
    cd ku-polls
    ```
3. Create a virtual environment.

    ```
    python -m venv venv
    ```
4. Activate the virtual environment.

    - for Mac OS / Linux.   
    ```
    source venv/bin/activate
    ```
    - for Windows.   
    ```
    venv\Scripts\activate
    ```
5. Install all required packages.

    ```
    pip install -r requirements.txt
    ```
6. Create `.env` file in `mysite/` and write down:

    ```
    DEBUG=True
    SECRET_KEY=Your-Secret-Key
    ALLOWED_HOSTS=localhost,127.0.0.1
    ```
9. Run this command to migrate the database.

    ```
    python manage.py migrate --run-syncdb
    ```
10. Initialize data
    ```
    python3 manage.py loaddata users polls
    ```
12. Start running the server by this command.
    ```
    python manage.py runserver
    ```

## Running KU Polls

Users provided by the initial data (users.json):

| Username  | Password    |
|-----------|-------------|
| demo1     | pass12345    |
| demo2     | pass123456    |

# Wiki

[Home](../../wiki/Home)
 * [Requirement](../../wiki/Requirements)
 * [Vision Statement](../../wiki/Vision-Statement)

# Plan
[Iteration1 Plane](../../wiki/Iteration-1-Plan)    
[Iteration2 Plane](../../wiki/Iteration-2-Plan)    
[Iteration3 Plane](../../wiki/Iteration-3-Plan)
