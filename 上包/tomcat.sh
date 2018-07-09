#!/bin/sh

cd  /opt/local/tomcat/bin
./shutdown.sh 2>&1 >/dev/null

tomcat_p=`ps -ef | grep tomcat | grep java | grep -v /bin/sh |awk '{print $2}'`
if [ $tomcat_p ]; then
kill -9 $tomcat_p
else
echo ">>>tomcat process doesn't exist"
fi

cd /opt/htdocs/logs
rm -rf *

module=${1}.war
if [ -e /opt/htdocs/new/${module} ]
then
echo '>>>war package exists.'
else
echo '>>>war package not exists.'
exit 1
fi

cd  /opt/htdocs/webapp
rm -rf  ${1}*

cd /opt/htdocs/new
mv *.war ../webapp/
cd /opt/htdocs/webapp

cd /opt/htdocs
rm -rf new

cd /opt/htdocs/webapp
chown -R upload:upload *

su -c /opt/local/tomcat/bin/startup.sh upload 2>&1 >/dev/null
if [ $? -eq 0 ]
then
echo '>>>tomcat start Success.' 
else
echo '>>>tomcat start Failed.'
exit 1
fi

tomcat_n=`ps -ef | grep tomcat | grep java | grep -v /bin/sh |awk '{print $2}'`
if [ $tomcat_p -eq $tomcat_n ]
then
echo '>>>tomcat restart Failed.'
else
echo ">>>tomcat resart Success."
fi




