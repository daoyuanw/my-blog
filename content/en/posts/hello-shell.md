---
title: "Hello, Shell!"
date: 2025-10-29T02:36:52+08:00
author: "Daoyuan"
slug:
draft: false
toc: false
---
# Why Shell?
1. The shell helps you unlock the full potential of your computer. It lets you run programs outside of the graphical user interface and gives you more control over your system.
2. The shell increases productivity by automating repetitive tasks. For example, when I first started updating my blog, I had to type several Git commands each time. After learning shell scripting, I could simply put those commands into one script and update my blog with a single command.
3. The shell also helps you understand how computers work at a deeper level, such as file management, piping, and permission control. These concepts are fundamental for learning operating systems and data structures later on.

# Hello Shell!
- `$`: indicates that you're in a regular shell session, not logged in as the root user
- `date`: prints the current date and time
- `echo`: prints whatever you type
- `$PATH`: shows the directories the shell searches when running a program
- `which`: shows the exact file being executed for a given command

```
bash-3.2$ echo $PATH
/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/opt/homebrew/bin
bash-3.2$ which echo
bin/echo
bash-3.2$ which date
/bin/date
bash-3.2$ 
```

# Navigation
- `/`: the root of the file system (like the root of a tree — every directory and file branches out from here)
- `pwd`: prints the current working directory
- `cd`: changes the working directory 
- `.`: represents the current directory
- `..`: represents the parent directory
``` 
bash-3.2$ pwd
/Users/daoyuan
bash-3.2$ cd desktop
bash-3.2$ pwd
/Users/daoyuan/desktop
bash-3.2$ cd ..
bash-3.2$ pwd
/Users/daoyuan
```

- `ls`: lists all contents in the current directory
```
bash-3.2$ ls
Desktop		Downloads	Movies		Pictures	WeChatProjects
Documents	Library		Music		Public		test
bash-3.2$ cd ..
bash-3.2$ ls
Shared	daoyuan
bash-3.2$ cd ..
bash-3.2$ ls
Applications	Volumes		etc		sbin
Library		bin		home		tmp
System		cores		opt		usr
Users		dev		private		var
```
-`ls -l`: shows a detailed list with more imformation about each file or directory
```
    bash-3.2$ ls -l /home
    lrwxr-xr-x  1 root  wheel  25 Oct 27 09:34 /home -> /System/Volumes/Data/home
```

What does each part mean?
- `l`: indicates the file type (here, `l` means a symbolic link)
- `rwxr-xr-x`: file permissions  
  - owner can read, write, execute  
  - group can read and execute  
  - others can read and execute
- `1`: number of hard links
- `root`: file owner
- `wheel`: default administrative group on macOS
- `25`: file size in bytes
- `Oct 27 09:34`: last modified time
- `/home -> /System/Volumes/Data/home`: where the directory actually points to

Other useful commands:
- `mv`: move or rename a file
- `cp`: copy a file
- `mkdir`: make a new directory