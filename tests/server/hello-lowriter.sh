#!/usr/bin/env bash
# Netcat: -u is for UDP, -c closes the connection on EOF

PORT=14733
if [[ $# -eq 2 ]]; then
    echo -e "lowriter -> doc = new_document()\n" | nc -uc localhost $PORT
    echo -e "lowriter -> text = doc.get_document_text()\n" | nc -uc localhost $PORT
    echo -e "lowriter -> text.set_text('$1')\n" | nc -uc localhost $PORT
    echo -e "lowriter -> doc.save_as('$2')\n" | nc -uc localhost $PORT
else
    echo "Usage: $0 [string] [path]"
fi
