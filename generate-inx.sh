#!/bin/bash
# Script to generate INX files from templates
# This runs 'make manual' which generates INX files from the templates/ directory

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

mkdir -p /tmp/inkstitch-bin
echo '#!/bin/bash' > /tmp/inkstitch-bin/python
echo 'exec python3 "$@"' >> /tmp/inkstitch-bin/python
chmod +x /tmp/inkstitch-bin/python

export PATH="/tmp/inkstitch-bin:$PATH"

echo "Generating INX files from templates..."

make manual
