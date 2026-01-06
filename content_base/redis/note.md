[Install Redis on Linux](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-linux/)

```bash
74410  2026-01-06_08:37:41 sudo apt-get install lsb-release curl gpg
74411  2026-01-06_08:37:52 curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
74412  2026-01-06_08:38:00 sudo chmod 644 /usr/share/keyrings/redis-archive-keyring.gpg
74413  2026-01-06_08:38:08 echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
74414  2026-01-06_08:38:16 sudo apt-get update
74415  2026-01-06_08:38:44 sudo apt-get install redis
74416  2026-01-06_08:39:07 sudo systemctl start redis-server
```

```bash
# redis
alias redis='redis-cli'
```

```bash
74443  2026-01-06_08:51:34 npm install --save-dev prettier
74444  2026-01-06_08:51:37 npx prettier --write a.js
```

```bash
# node
alias ptw='npx prettier --write'
```

