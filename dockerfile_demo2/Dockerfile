# Pull base image  
FROM ubuntu  
  
MAINTAINER fqyang 
  
# update source  
#RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe"> /etc/apt/sources.list  
#RUN apt-get update  
  
# Install curl  
#RUN apt-get -y install curl  
  
# Install JDK 8  
WORKDIR /tmp
ADD jdk-8u181-linux-x64.tar.gz .
RUN mkdir -p /usr/lib/jvm  
RUN mv /tmp/jdk1.8.0_181/  /usr/lib/jvm/java8/  
  
ENV JAVA_HOME /usr/lib/jvm/java8/  
  
# Install tomcat7 
ADD apache-tomcat-7.0.91.tar.gz . 
RUN mv /tmp/apache-tomcat-7.0.91  /opt/tomcat7/  
  
ENV CATALINA_HOME /opt/tomcat7  
ENV PATH $PATH:$CATALINA_HOME/bin  
  
ADD tomcat7.sh /etc/init.d/tomcat7  
RUN chmod 755 /etc/init.d/tomcat7  
  
# Expose ports.  
EXPOSE 8080  
  
# Define default command.  
ENTRYPOINT service tomcat7 start && tail -f /opt/tomcat7/logs/catalina.out 
