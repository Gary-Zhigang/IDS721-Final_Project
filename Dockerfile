FROM python:3.10.4

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable for the Flask app
ENV FLASK_APP=app.py

# Expose the port on which the Flask app will run
EXPOSE 8080

# Run the command to start the Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]