FROM  registry.redhat.io/rhscl/python-38-rhel7

USER 0
RUN curl https://packages.microsoft.com/config/rhel/7/prod.repo > /etc/yum.repos.d/msprod.repo

RUN ACCEPT_EULA=Y yum -y install msodbcsql17 mssql-tools unixODBC-devel && yum clean all

RUN pip install pyodbc

USER 1001

RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
