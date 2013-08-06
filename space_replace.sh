#!/bin/bash

tar -cvzf backup.tar.gz .
mod_date=`date "+%Y.%m.%d"`

mv backup.tar.gz backup.$mod_date.tar.gz

find . -depth -name '* *' | while IFS= read -r f ; do mv -i "$f" "$(dirname "$f")/$(basename "$f"|tr ' ' _)" ; done
