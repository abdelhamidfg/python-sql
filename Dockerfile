FROM registry.redhat.io/rhscl/python-38-rhel7

# Add application sources
ADD --chown=1001:0 / .

# Install the dependencies
USER root

#yum install rh-python36-python-devel
RUN  yum install --disableplugin=subscription-manager -y  rh-python36-python-devel

RUN pip install -r requirements.txt &&\ 
    pip install pyodbc 
      
    
   # python manage.py collectstatic --noinput && \
   # python manage.py migrate

# Run the application
#CMD python manage.py runserver 0.0.0.0:8080
	# Run as the root user
 
