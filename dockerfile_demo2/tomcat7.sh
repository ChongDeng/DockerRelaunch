#!/bin/bash

export JAVA_HOME=/usr/lib/jvm/java8/
export TOMCAT_HOME=/opt/tomcat7
export PATH=$JAVA_HOME/bin:$PATH

case $1 in
start)
    sh $TOMCAT_HOME/bin/startup.sh
    ;;
stop)
    sh $TOMCAT_HOME/bin/shutdown.sh
    ;;
restart)
    sh $TOMCAT_HOME/bin/startup.sh
    sh $TOMCAT_HOME/bin/shutdown.sh
    ;;
esac
