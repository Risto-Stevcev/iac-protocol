#!/bin/bash

RUNNING=$(ps ax | grep -E "(iacs|server.py)" | wc -l)
GNUMERIC="$1hello.gnumeric"
LOCALC="$1hello.ods"
LOWRITER="$1hello.odt"
passed=0
failed=0

if [[ "$#" -ne "1" ]]; then
    echo "Usage: $0 [save path]"
    exit 1;
fi

if [[ ! $(iacmodify -s | grep -E "(#.*gnumeric|#.*localc|#.*lowriter)" | wc -l) -eq "0" ]]; then
    echo "Enable gnumeric, lowriter and localc and restart the server to continue:"
    echo "sudo iacmodify --enable -a gnumeric"
    echo "sudo iacmodify --enable -a lowriter"
    echo "sudo iacmodify --enable -a localc"
    exit 1
fi

if [[ "$RUNNING" -lt "2" ]]; then
    echo "Please run the iac server (iacs or ./server.py)."
    exit 1
fi


printf "Attempting hello.gnumeric (gnumeric) ..."
./hello-gnumeric.sh 'A1' 'Hello, World' $GNUMERIC 
echo "Done. (Command: ./hello-gnumeric.sh 'A1' 'Hello, World' $GNUMERIC)"

printf "Attempting hello.ods (localc) ..."
./hello-localc.sh 'A1' 'Hello, World' $LOCALC
echo "Done. (Command: ./hello-localc.sh 'A1' 'Hello, World' $LOCALC)"

printf "Attempting hello.odt (lowriter) ..."
./hello-lowriter.sh 'Hello, World' $LOWRITER
echo "Done. (Command: ./hello-lowriter.sh 'Hello, World' $LOWRITER) "

sleep 3

if [ ! -f $GNUMERIC ]; then
    echo "Creating $GNUMERIC failed."
    failed=`expr $failed + 1`
else
    passed=`expr $passed + 1`
fi

if [ ! -f $LOCALC ]; then
    echo "Creating $LOCALC failed."
    failed=`expr $failed + 1`
else
    passed=`expr $passed + 1`
fi

if [ ! -f $LOWRITER ]; then
    echo "Creating $LOWRITER failed."
    failed=`expr $failed + 1`
else
    passed=`expr $passed + 1`
fi

echo "Test Results"
echo "-----------------------"
echo ""
echo "Passed: $passed, Failed: $failed."

printf "Deleting $GNUMERIC, $LOCALC, $LOWRITER ..."
rm -rf $GNUMERIC $LOCALC $LOWRITER
echo "Done"
