#!/usr/bin/env bash
# Netcat: -u is for UDP, -c closes the connection on EOF

PORT=14733
if [[ $# -eq 3 ]]; then
    echo -e "gnumeric -> doc = new_document(1)\n" | nc -uc localhost $PORT 
    echo -e "gnumeric -> sheet = doc.get_sheet(0)\n" | nc -uc localhost $PORT
    echo -e "gnumeric -> cell = sheet.fetch_cell('$1')\n" | nc -uc localhost $PORT
    echo -e "gnumeric -> cell.set_text('$2')\n" | nc -uc localhost $PORT
    echo -e "gnumeric -> doc.save_as('$3')\n" | nc -uc localhost $PORT
else
    echo "Usage: $0 [cell] [string] [path]"
fi
