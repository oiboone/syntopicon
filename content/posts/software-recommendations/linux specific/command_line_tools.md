---
title: "Command Line Linux Utilities"
date: 2021-01-02
author: Jeffrey A. Jalkio
---
# Core Utils - don't organize by coreutils, but indicate which commands are in coreutils and other groups.
https://www.gnu.org/software/coreutils/manual/html_node/index.html#SEC_Contents

## System information

### Help on system commands

type [command]
: Find out if command is built into shell or an executable file

which [command]
: shows path to executable

man [command]
: display man page for the command

whatis [command]
: displays one line command description

apropos [topic]
: displays one line summary of commands whose descriptions include topic

info [command]
: display texinfo page for command.

### System configuraiton

df [file]

: size of, and space available on, partition containing file. If no file is given, summary of all partitions.

uname
: informaiton regardign system. uname 
-s shows kernel name
-n network node hostname
-r kernel release
-v kernel version
-m machine hardware name
-p processor type
-i hardware platform
-o operating system
-a shows all of the above in that order

ps
: ps shows current processes
-A shows all processes on system
-t [terminal] shows processes associated with a particular terminal (ours by default)
-C [command list] shows processes whose executable in in command list.
-p [pid list] shows processes wiht particular id #
-U show based on real user name
-u show based on effective user name
add flags for what to display for these processes

who
: shows all current users. who -a shows lots of system information.

## process management

at
: execute command at specific time

sleep [seconds]
: wait a specified number of seconds

kill
: sends signal to a process

time
: display time to execute command

wait [process id]
: wait for process id to finish

nohup
:

nice
:

renice
:

batch
:

fg
:

bg
:

jobs
:

fuser
:

## Programming

cc
: C compiler, gcc, clang

make
:

lex
: (flex)

yacc
: (bison)

### Binutils

as
: (gas) assembler

ld
: linker

saveral others <https://www.gnu.org/software/binutils/>


## File Utils

### directory listing

Only ls is needed

ls
: list files in directory. -a flag includes hidden files. -l flag gives all info.

dir:
: brief lisitng

vdir
: verbose listing

### Basic file operations
cp
: copy file

mv			
: move file

rm
: remove

shred
: secure deletion

dd
: copy and convert file - used to create bootable thumb drives, etc.

install			
: copy file and set attributes


### Commands for working with Special File types

link
: make hard link via link syscall

ln
: link file, hard or soft links

mkdir
: make new directory

mkfifo
: creates named pipe

mknod
: create special file (device driver)

mktemp

readlink		print value of symlink or canonical filename

rmdir

unlink			remove fiels via unlink syscall

### Changing File Attributes

chown			change owner and group of file
chgrp			change only group (not strictly needed but safer than chown)
chmod			change file permissions
touch			change timestamps

## Disk Usage
df			disk free
du			estimate file space usage
stat			info about an inode (shell util)
sync			syncronize cached writes
truncate		shrink or extend file

realpath		returns resolved path

## Text Utils
### Reformat
base32		base32 encoding - converts binary to ascii and vice versa
base64		base64 encoding - converts binary to ascii and vice versaq
od		octal dump
tr		convert characters
expand	convert tabs to spaces
unexpand	spaces to tabs

### Combine Files
cat
tac		reverse cat
nl		number lines
join		

### Output parts of files
split		splits files into parts of equal length  PART01, PART02....
tail		print final N lines or characters of file
csplit		split file into sections based on patterns
head		print first n line or characters of file

### Edit lines of files
cut		remove sections of each line of file based on delimiters, column, or characters
paste		merge lines of files
join		joint two files based on common field

### Formatting text files
fmt		simple formating of paragraphs
fold		wrap each line to fit in specified width
pr		paginate or columnate for printing

### Summarize Files
wc		line, word, and byte counts and filename
chsum		CRC checksum and byte count
sum		checksum and block count
md5sum
sha1sum
sha256sum
sha512sum

### File Sorting
shuf		shuffle
sort		
uniq		remove duplicated lines
comm		compare two sorted files line by line
ptx?

## Shell Utils
Printing Text
echo
printf
yes
Conditions
false
true
test
expr

## Redirection
tee

## File Name Manipulation
basename
dirname
pathcheck
mktemp(fileutil)
realpath(fileutil)

## Working Context
pwd
stty
printenv
tty

## User Information
id
logname
whoami
groups
users
who

## System Context
date
arch
nproc
uname
hostname
hostid
uptime

## SELinux context
chcon
runcon

## Apparmor
aa-enabled (1)       - test whether AppArmor is enabled
aa-exec (1)          - confine a program with the specified AppArmor profile
aa-remove-unknown (8) - remove unknown AppArmor profiles
aa-status (8)        - display various information about the current AppArmor policy.
aa-teardown (8)      - unload all AppArmor profiles
apparmor.d (5)       - syntax of security profiles for AppArmor.
apparmor.vim (5)     - vim syntax highlighting file for AppArmor profiles
apparmor_parser (8)  - loads AppArmor profiles into the kernel
apparmor_status (8)  - display various information about the current AppArmor policy.

## Modified Command Invocation
chroot
env
nice
nohup
stdbuf
timeout



## Numeric Operations

bc
dc
factor
numfmt
seq

## Communications

write
wall
mesg

## Other cool commands

find
grep
ed
sed
awk
cal
calendar