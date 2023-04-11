# GitHub Profile Pursuit Service

## About
```text
This system takes basic data from a Github user and writes it to a txt file.
For this, the Github API is used to extract the data and then create a dictionary report.

It's only uses building libraries, therefore, it has no external dependency.
This is also lightweight and thread-safe, which makes it ideal for use in services and microservices.
```
****
**Table of Contents**

>[Motivation](#motivation)

>[Deployment by docker](#deployment-by-docker)

>[Test Coverage](#test-coverage)

>[Safety Report](#safety-report)
****
## Motivation

* **Motivation:**
    My motivation for building the project may have been a desire to create
  a tool that simplifies the GitHubApi

* **Why did you build this project**:
    Study purpose

* **Problem-solving:**
    Simplify the GitHubApi

* **Learning:**
    I have learned about the process of building a web application using
  Python and implementing algorithm. Additionally, I may have gained experience
  software design and archtecture and user experience considerations.

## Requirements
* **[Python](https://www.python.org/)**


>[Back to Table of Contents](#table-of-contents)
****
## Deployment by Docker

```console
docker-compose up --build
```
>[Back to Table of Contents](#table-of-contents)
****

## How to use example
```text
You must create a .env file inside the project`s app folder with a constant called GITHUB_USER_NAME=username and
GITHUB_PERSONAL_ACCESS_TOKEN=access_token_key, like in .env_example.


And then just run the follow code

If you will run it outside of docker, so you must install the requirements with you favorite envorimont manager
```
More details about how to config a Github personal access token key, visit  **[Github Personal Access Token](https://docs.github.com/en/rest/overview/authenticating-to-the-rest-api?apiVersion=2022-11-28)**
```bash
python run.py
```


**You will notice a .txt file created in project`s root/app folder called username.txt contening user data.**

>[Back to Table of Contents](#table-of-contents)
```
***

## Test Coverage

```text
Name                                                           Stmts   Miss  Cover
----------------------------------------------------------------------------------
config.py                                                          7      0   100%
src/__init__.py                                                    0      0   100%
src/entities/__init__.py                                           0      0   100%
src/entities/github_api_client.py                                 42      2    95%
src/entities/user_github.py                                        6      0   100%
src/main.py                                                       15      2    87%
src/services/__init__.py                                           0      0   100%
src/services/dump_data_processor.py                               19      0   100%
src/use_cases/__init__.py                                          0      0   100%
src/use_cases/github_profile_processor.py                         32      5    84%
tests/__init__.py                                                  0      0   100%
tests/conftest.py                                                 17      0   100%
tests/e2e/__init__.py                                              0      0   100%
tests/e2e/test_username_to_write_file.py                          17      0   100%
tests/integration/__init__.py                                      0      0   100%
tests/integration/entities/__init__.py                             0      0   100%
tests/integration/entities/test_github_client.py                  34      8    76%
tests/integration/use_cases/__init__.py                            0      0   100%
tests/integration/use_cases/test_github_profile_processor.py      34      7    79%
tests/unit/__init__.py                                             0      0   100%
tests/unit/services/__init__.py                                    0      0   100%
tests/unit/services/test_dump_data_processor.py                   40      0   100%
tests/unit/test_config.py                                          3      0   100%
----------------------------------------------------------------------------------
TOTAL                                                            266     24    91%
```

>[Back to Table of Contents](#table-of-contents)
***

## Safety Report

```text
 REPORT

  Safety v2.3.2 is scanning for Vulnerabilities...
  Scanning dependencies in your files:

  -> /tmp/github_api-OZ2Vb7g7hco5mhl9_requirements.txt

  Found and scanned 46 packages
  Timestamp 2023-03-16 13:33:02
  0 vulnerabilities found
  0 vulnerabilities ignored
+===========================================================================================+
 No known security vulnerabilities found.
+===========================================================================================+
```
>[Back to Table of Contents](#table-of-contents)

## License
```text
This project is licensed under the terms of the MIT license.
```
