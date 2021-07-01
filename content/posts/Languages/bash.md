---
title: "Unix Shells"
date: 2021-01-02
author: Jeffrey A. Jalkio
---
# Comparison of shells

1. bash
2. dash
3. sh

# Command line parameters

$# - number of parameters
$0 - name of script executed
$1 ... $n - parameters
<https://www.redhat.com/sysadmin/arguments-options-bash-scripts>

# user input and communication

read foo
echo $foo

# conditional execution

if [$1 -ne foo]; then
	echo "not foo"
fi