#!/bin/sh
THIS_DIR=`dirname $0`
java -cp $(echo $THIS_DIR/_schemacrawler/lib/*.jar | tr ' ' ':') schemacrawler.Main $*
