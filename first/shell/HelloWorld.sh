#!/bin/bash
echo "Hello World!"

printvar="Hello"
echo $printvar

printcat1=""$printvar" World!"
printcat2="${printvar} World!"
echo $printcat1 $printcat2

