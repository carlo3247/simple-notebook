# Dockerfile

# FROM directive instructing base image to build upon
FROM python:2-onbuild

# COPY startup script into known file location in container
COPY start.sh /start.sh

# ENV set environment directory tree
ENV PROJECT=mysite
ENV CONTAINER_HOME=/opt
ENV CONTAINER_PROJECT=$CONTAINER_HOME/$PROJECT

# set project WORKDIR
WORKDIR $CONTAINER_PROJECT

# COPY project to container directory
COPY . $CONTAINER_PROJECT

# get modules
RUN pip install requirements.txt

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
CMD ["/start.sh"]
# done!
