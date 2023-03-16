# version args
ARG base=python
ARG tag=3.11.1

# pull official base image
FROM $base:$tag

ARG base
ARG tag
LABEL baseimage=$base:$tag
LABEL maintainer=victorbrittoferreira@gmail.com

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create the appropriate directories
WORKDIR /github_api_profiler

# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . . 

CMD ["python", "run.py" ]
