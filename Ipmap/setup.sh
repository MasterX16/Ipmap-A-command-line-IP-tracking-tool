#!/bin/bash
# MIT License
#
# Copyright (c) 2024 MasterX16
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# Get the directory where setup.sh is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Directory where ipmap.py is located
IPMAP_DIR="$SCRIPT_DIR"

# Check if the ipmap.py file exists in the directory
if [ ! -f "$IPMAP_DIR/ipmap.py" ]; then
    echo "Error: ipmap.py not found in $IPMAP_DIR."
    exit 1
fi

# Create a symbolic link to ipmap.py in /usr/local/bin/
ln -s "$IPMAP_DIR/ipmap.py" "/usr/local/bin/ipmap"

echo "Ipmap setup completed. You can now use 'ipmap' command to run your script."
