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
You must create a .env file in the project`s root folder with a constant called GITHUB_USER_NAME=username. 

If you don`t creat this, the system will require a nickname in the console input.
>>>Insert the user name:
...username

You will notice a .txt file created in project`s root folder called username.txt contening user data.
```
>[Back to sumary](#summary)
***

## Test Coverage

```text

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
