#!/usr/bin/env bash
# Netcat: -u is for UDP, -c closes the connection on EOF

PORT=14733
if [[ $# -eq 3 ]]; then
    echo -e "localc -> doc = new_document()\n" | nc -uc localhost $PORT
    echo -e "localc -> sheet = doc.current_sheet()\n" | nc -uc localhost $PORT
    echo -e "localc -> cell = sheet.fetch_cell('$1')\n" | nc -uc localhost $PORT
    echo -e "localc -> cell.set_text('$2')\n" | nc -uc localhost $PORT
    echo -e "localc -> doc.save_as('$3')\n" | nc -uc localhost $PORT
else
    echo "Usage: $0 [cell] [string] [path]"
fi
