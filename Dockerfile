FROM registry.redhat.io/rhscl/python-38-rhel7

# Add application sources
ADD --chown=1001:0 app-src .

# Install the dependencies
RUN pip install -r requirements.txt &&\ 
    pip install pyodbc 
      
    
   # python manage.py collectstatic --noinput && \
   # python manage.py migrate

# Run the application
#CMD python manage.py runserver 0.0.0.0:8080
