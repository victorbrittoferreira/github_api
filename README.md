# GitHub Profile Pursuit Service

```text
This system takes basic data from a Github user and writes it to a txt file.
For this, the Github API is used to extract the data and then create a dictionary report.

It's only uses building libraries, therefore, it has no external dependency.
This is also lightweight and thread-safe, which makes it ideal for use in services and microservices.
```
****
## Summary


>[Deployment by venv](#deployment-by-virtualenv)

>[Deployment by docker](#deployment-by-docker)

>[Test Coverage](#test-coverage)

>[Safety Report](#safety-report)
****
## Tech Stack

**Back-end server:** Python(without framework)
****
## Deployment by VirtualEnv

--If you prefer just to run without docker, run the following cli, after deploying using your preferred virtualenv manager.

```bash
make pursuit_profile
```

- PS: The default virtualenv PIPENV

>[Back to sumary](#summary)
****
## Deployment by Docker

```console
docker-compose build
docker run -ti github_api_service:0.1
```
>[Back to sumary](#summary)
****

## How to use example
```text
You must create a .env file in the project`s root/app folder with a constant called GITHUB_USER_NAME=username.

If you don`t creat this, the system will require a nickname in the console input.
>>>Insert the user name:
...username

You will notice a .txt file created in project`s root/app folder called username.txt contening user data.
```
>[Back to sumary](#summary)
***

## Test Coverage

```text
Name                                                           Stmts   Miss  Cover
----------------------------------------------------------------------------------
config.py                                                          7      0   100%
src/__init__.py                                                    0      0   100%
src/entities/__init__.py                                           0      0   100%
src/entities/github_api_client.py                                 42      6    86%
src/entities/user_github.py                                        6      0   100%
src/main.py                                                       15      4    73%
src/services/__init__.py                                           0      0   100%
src/services/dump_data_processor.py                               19      0   100%
src/use_cases/__init__.py                                          0      0   100%
src/use_cases/github_profile_processor.py                         32      8    75%
tests/__init__.py                                                  0      0   100%
tests/conftest.py                                                 17      0   100%
tests/e2e/__init__.py                                              0      0   100%
tests/e2e/test_username_to_write_file.py                          11      6    45%
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
TOTAL                                                            260     39    85%
```

>[Back to sumary](#summary)
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
>[Back to sumary](#summary)
