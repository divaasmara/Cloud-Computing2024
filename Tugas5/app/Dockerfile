FROM python:3-alpine3.15
# Environment variable for the user
ENV USER=appuser
# Add necessary packages
RUN apk add --no-cache shadow
# Create a system group and user
RUN groupadd -r $USER && useradd -r -g $USER $USER
# Set the working directory
WORKDIR /app
# Copy all files into the container
COPY . .
# Change ownership of the app directory to the app user
RUN chown -R $USER:$USER /app
# Install dependencies
RUN pip install -r requirements.txt
# Set the user to run the application
USER $USER
# Command to run the application with increased Gunicorn timeout
CMD [ "gunicorn", "--timeout", "120", "--bind", "0.0.0.0:5000", "wsgi:app" ]
