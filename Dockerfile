FROM  registry.redhat.io/rhscl/python-38-rhel8

# Add application sources
ADD --chown=1001:0 / .

USER 0
RUN curl https://packages.microsoft.com/config/rhel/7/prod.repo > /etc/yum.repos.d/msprod.repo

RUN ACCEPT_EULA=Y yum -y install msodbcsql17 mssql-tools unixODBC-devel && yum clean all

RUN pip install pyodbc &&\
    pip install -r requirements.txt

USER 1001

RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

# Run the application
CMD python app.py runserver 0.0.0.0:8080
	# Run as the root user
