#!/bin/bash

GNUMERIC="$1hello.gnumeric"
LOCALC="$1hello.ods"
LOWRITER="$1hello.odt"
passed=0
failed=0

if [[ "$#" -ne "1" ]]; then
    echo "Usage: $0 [save path]"
    exit 1;
fi

printf "Enabling gnumeric, localc and lowriter..."
sudo iacmodify --enable -a gnumeric
sudo iacmodify --enable -a lowriter
sudo iacmodify --enable -a localc
echo "Done."

printf "Attempting hello.gnumeric (gnumeric) ..."
cat hello-gnumeric.txt | sed -e "s|{path}|$GNUMERIC|g" | iaci
echo "Done. (Command: cat hello-gnumeric.txt | sed -e \"s|{path}|$GNUMERIC|g\" | iaci)"

printf "Attempting hello.ods (localc) ..."
cat hello-localc.txt | sed -e "s|{path}|$LOCALC|g" | iaci
echo "Done. (Command: cat hello-localc.txt | sed -e \"s|{path}|$LOCALC|g\" | iaci)"

printf "Attempting hello.odt (lowriter) ..."
cat hello-localc.txt | sed -e "s|{path}|$LOWRITER|g" | iaci
echo "Done. (Command: cat hello-localc.txt | sed -e \"s|{path}|$LOWRITER|g\" | iaci) "

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

printf "Disabling gnumeric, localc and lowriter..."
sudo iacmodify --disable -a gnumeric
sudo iacmodify --disable -a lowriter
sudo iacmodify --disable -a localc
echo "Done."

echo "Test Results"
echo "-----------------------"
echo ""
echo "Passed: $passed, Failed: $failed."

printf "Deleting $GNUMERIC, $LOCALC, $LOWRITER ..."
rm -rf $GNUMERIC $LOCALC $LOWRITER
echo "Done"
