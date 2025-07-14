# 🛡️ Login Script with Lockout System

This Python script prompts the user for a password and limits login attempts with increasing lockout times after repeated failures.

## 🔧 Features

- Passwords are hashed using SHA-256.
- Allows 3 failed attempts before blocking.
- Lockout time increases after each block:
  - 1st block: 10 seconds  
  - 2nd block: 1 minute  
  - 3rd block: 5 minutes  
  - 4th and beyond: 30 minutes

