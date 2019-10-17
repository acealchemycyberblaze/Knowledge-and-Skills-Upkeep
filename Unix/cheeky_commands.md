All users including UID and GID information    
```bash
for users in $(cat /etc/passwd | cut -f1 -d":"); do id $users; done
```

List all UID 0 (root) accounts   
```bash 
cat /etc/passwd | cut -f1,3,4 -d":" | grep"0:0" | cut -f1 -d":" | awk '{print $1}'
```

find readable users in .bash_history file    
```bash
find /home/* -name *.*history - print 2>/dev/null
```

find all cronjobs  
```bash 
find /etc/crontab && ls -als /etc/cron*
```

find world writable cron jobs   
```bash 
find /etc/cron* -type f -perm -o+w -exec ls -l {} \;
```
