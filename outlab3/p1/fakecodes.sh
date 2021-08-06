#! /bin/bash
c=$(</dev/urandom tr -dc [A-Z]U[0-9] | head -c3)
sed -e "s/[A-Z][A-Z][0-9]/$c/g" $1

