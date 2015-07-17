#!/bin/sh
DIR=`dirname $0`
java -jar $DIR/checkstyle-all.jar $*
