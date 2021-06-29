---
description: are you ready to feel like a REAL hacker yet?
---

# System Attacks

## Intro

There is a series of different styles of attacks you will need to know well on the system level. Being able to navigate metasploit will absolutely serve you for the better so I recommend re-watching the meterpreter and metasploit videos from the PTS course. Additionally, I would also be comfortable with using tools to bruteforce your way into a service.

![when you get your first reverse shell connection](../../.gitbook/assets/giphy-3-.gif)

## Helpful system locations

* you can find a lot of wordlists for password attacks in /usr/share/&lt;program name&gt;
* you can find a lot of third party pen testing tools like impacket in /opt/
* if you need to transfer a shell try putting it in /tmp that storage empties after reboot
* shadow and passwd are both in /etc \(/etc/passwd & /etc/shadow\)

## **Password Attacks**

### **unshadow**

```javascript
unshadow passwd shadow > hashtocrack
```

* used on the shadow and passwd file to prepare it for a password attack tool like hashcat or john the ripper

### **john the ripper \(john\)**

```javascript
john --wordlist <path to wordlist> hashfiletocrack
```

* a common wordlist to use is located in /usr/share/john/password.lst 
* I recommend [SecLists](https://github.com/danielmiessler/SecLists) on github for more password list options
  * once this is installed, you can find the new lists in /usr/share/seclists
* john --show hashes shows the cracked passwords

### **hydra**

\*\*\*\*

\*\*\*\*

\*\*\*\*

