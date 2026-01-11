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
alias ptw='npx prettier --write' ```


```bash
127.0.0.1:6379> 
lpush books 'clean code'
lpush books 'code complete'
lpush books 'peopleware'

127.0.0.1:6379> llen books
(integer) 3

127.0.0.1:6379> lindex books 1
"code complete"

lrange books 0 1
lrange books 0 -1

lpop books
lrange books 0 -1
rpop books
lrange books 0 -1
```

---

```
hset movie 'title' 'The Godfather'
hmset movie 'year' 1972 'rating' 9.2 'watchers' 10000000
hincrby movie 'watchers' 3
hget movie 'title'
hmget movie 'title' 'watchers'
hdel movie 'watchers'
hgetall movie
hkeys movie
hvals movie
```

```bash
127.0.0.1:6379> hgetall movie
1) "title"
2) "The Godfather"
3) "year"
4) "1972"
5) "rating"
6) "9.2"
127.0.0.1:6379> hkeys movie
1) "title"
2) "year"
3) "rating"
127.0.0.1:6379> hvals movie
1) "The Godfather"
2) "1972"
3) "9.2"
```


```js
const redis = require("redis");

async function main() {
  const client = await redis.createClient();
  await client.connect();

  debugger;
  await saveLink(
    client,
    123,
    "dayvson",
    "Maxwell Dayvson's Github page",
    "https://github.com/dayvson",
  );
  await upVote(client, 123);
  await upVote(client, 123);
  await saveLink(
    client,
    456,
    "hltbra",
    "Hugo Travares's Github page",
    "https://github.com/hltbra",
  );
  await upVote(client, 456);
  await upVote(client, 456);
  await downVote(client, 456);

  showDetails(await getDetails(client, 123));
  showDetails(await getDetails(client, 456));

  await client.quit();
}

async function saveLink(client, id, auther, title, link) {
  await client.hmSet(
    `link:${id} auther ${auther} title ${title} link ${link} score 0`,
  );
}

async function upVote(client, id) {
  await client.hIncrby(`link:${id} score`, 1);
}

async function downVote(client, id) {
  await client.hIncrby(`link:${id} score`, -1);
}

async function getDetails(client, id) {
  return await client.hGetAll(`link:${id}`);
}

function showDetails(replies) {
  console.log(`Title: ${replies["title"]}`);
  console.log(`Author: ${replies["author"]}`);
  console.log(`Link: ${replies["link"]}`);
  console.log(`Score: ${replies["score"]}`);
  console.log(`--------------------------`);
}

main();
```

```bash
$ node hash-voting-system.js 
/home/widehyo/gitclone/playground/content_base/redis/playground/hash-voting-system.js:35
  await client.hmSet(
               ^

TypeError: client.hmSet is not a function
    at saveLink (/home/widehyo/gitclone/playground/content_base/redis/playground/hash-voting-system.js:35:
16)
    at main (/home/widehyo/gitclone/playground/content_base/redis/playground/hash-voting-system.js:8:9)
    at process.processTicksAndRejections (node:internal/process/task_queues:95:5)

Node.js v22.3.0
```


debug> p Object.getPrototypeOf(client)
debug> p Reflect.ownKeys(Object.getPrototypeOf(client))
p Object.getPrototypeOf(client)
p Reflect.ownKeys(Object.getPrototypeOf(client))


debug> p client.command().then(console.log)
Promise

debug> p client.command().then(r => r.length)
p client.command().then(r => r.length)

const repl = require('repl');

debugger;

repl.start({ prompt: '> ' }).context.client = client;

```js
const util = require("util");
const redis = require("redis");

async function main() {
  const client = await redis.createClient();
  await client.connect();

  const commands = await client.command();
  console.log(util.inspect(commands));
  console.log(util.inspect(commands, { showHidden: true, depth: 2 }));
}
```

```log
[
  {
    name: 'cf.count',
    arity: 3,
    flags: Set(3) { 'readonly', 'module', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(2) { '@read', '@cuckoo' }
  },
  {
    name: 'zrangebylex',
    arity: -4,
    flags: Set(1) { 'readonly' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@sortedset', '@slow' }
  },
  {
    name: 'FT.DEL',
    arity: -1,
    flags: Set(2) { 'write', 'module' },
    firstKeyIndex: 2,
    lastKeyIndex: 2,
    step: 1,
    categories: Set(2) { '@write', '@search' }
  },
  {
    name: 'lset',
    arity: 4,
    flags: Set(2) { 'write', 'denyoom' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@list', '@slow' }
  },
  {
    name: 'cf.scandump',
    arity: 3,
    flags: Set(3) { 'readonly', 'module', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(2) { '@read', '@cuckoo' }
  },
  {
    name: 'VCARD',
    arity: 2,
    flags: Set(3) { 'readonly', 'module', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(0) {}
  },
  {
    name: 'getrange',
    arity: 4,
    flags: Set(1) { 'readonly' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@string', '@slow' }
  },
  {
    name: 'FT.EXPLAIN',
    arity: -1,
    flags: Set(2) { 'readonly', 'module' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(1) { '@search' }
  },
  {
    name: 'hexpireat',
    arity: -6,
    flags: Set(2) { 'write', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@hash', '@fast' }
  },
  {
    name: 'hpexpire',
    arity: -6,
    flags: Set(2) { 'write', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@hash', '@fast' }
  },
  {
    name: 'bzpopmin',
    arity: -3,
    flags: Set(3) { 'write', 'blocking', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: -2,
    step: 1,
    categories: Set(4) { '@write', '@sortedset', '@fast', '@blocking' }
  },
  {
    name: 'zrange',
    arity: -4,
    flags: Set(1) { 'readonly' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@sortedset', '@slow' }
  },
  {
    name: 'xclaim',
    arity: -6,
    flags: Set(2) { 'write', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@stream', '@fast' }
  },
  {
    name: 'spublish',
    arity: 3,
    flags: Set(4) { 'pubsub', 'loading', 'stale', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(2) { '@pubsub', '@fast' }
  },
  {
    name: 'FT.AGGREGATE',
    arity: -1,
    flags: Set(2) { 'readonly', 'module' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(2) { '@read', '@search' }
  },
  {
    name: 'lindex',
    arity: 3,
    flags: Set(1) { 'readonly' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@list', '@slow' }
  },
  {
    name: 'ssubscribe',
    arity: -2,
    flags: Set(4) { 'pubsub', 'noscript', 'loading', 'stale' },
    firstKeyIndex: 1,
    lastKeyIndex: -1,
    step: 1,
    categories: Set(2) { '@pubsub', '@slow' }
  },
  {
    name: 'tdigest.create',
    arity: -2,
    flags: Set(3) { 'write', 'denyoom', 'module' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@fast', '@tdigest' }
  },
  {
    name: 'cms.merge',
    arity: -4,
    flags: Set(3) { 'write', 'denyoom', 'module' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(2) { '@write', '@cms' }
  },
  {
    name: 'bitpos',
    arity: -3,
    flags: Set(1) { 'readonly' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@bitmap', '@slow' }
  },
  {
    name: 'sintercard',
    arity: -3,
    flags: Set(2) { 'readonly', 'movablekeys' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(3) { '@read', '@set', '@slow' }
  },
  {
    name: 'topk.count',
    arity: -3,
    flags: Set(2) { 'readonly', 'module' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(2) { '@read', '@topk' }
  },
  {
    name: 'json.clear',
    arity: -1,
    flags: Set(2) { 'write', 'module' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(2) { '@write', '@json' }
  },
  {
    name: 'json.objlen',
    arity: -1,
    flags: Set(2) { 'readonly', 'module' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(2) { '@read', '@json' }
  },
  {
    name: 'sscan',
    arity: -3,
    flags: Set(1) { 'readonly' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@set', '@slow' }
  },
  {
    name: 'xadd',
    arity: -5,
    flags: Set(3) { 'write', 'denyoom', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@stream', '@fast' }
  },
  {
    name: 'tdigest.byrevrank',
    arity: -3,
    flags: Set(2) { 'readonly', 'module' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@fast', '@tdigest' }
  },
  {
    name: 'rpush',
    arity: -3,
    flags: Set(3) { 'write', 'denyoom', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@list', '@fast' }
  },
  {
    name: 'pfdebug',
    arity: 3,
    flags: Set(3) { 'write', 'denyoom', 'admin' },
    firstKeyIndex: 2,
    lastKeyIndex: 2,
    step: 1,
    categories: Set(5) {
      '@write',
      '@hyperloglog',
      '@admin',
      '@slow',
      '@dangerous'
    }
  },
  {
    name: 'keys',
    arity: 2,
    flags: Set(1) { 'readonly' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(4) { '@keyspace', '@read', '@slow', '@dangerous' }
  },
  {
    name: 'FT.CONFIG',
    arity: -1,
    flags: Set(2) { 'readonly', 'module' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(2) { '@admin', '@search' }
  },
  {
    name: 'VGETATTR',
    arity: 3,
    flags: Set(3) { 'readonly', 'module', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(0) {}
  },
  {
    name: 'xinfo',
    arity: -2,
    flags: Set(0) {},
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(1) { '@slow' }
  },
  {
    name: 'FT.DROP',
    arity: -1,
    flags: Set(2) { 'write', 'module' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(4) { '@write', '@slow', '@dangerous', '@search' }
  },
  {
    name: 'unlink',
    arity: -2,
    flags: Set(2) { 'write', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: -1,
    step: 1,
    categories: Set(3) { '@keyspace', '@write', '@fast' }
  },
  {
    name: 'flushall',
    arity: -1,
    flags: Set(1) { 'write' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(4) { '@keyspace', '@write', '@slow', '@dangerous' }
  },
  {
    name: 'append',
    arity: 3,
    flags: Set(3) { 'write', 'denyoom', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@string', '@fast' }
  },
  {
    name: 'memory',
    arity: -2,
    flags: Set(0) {},
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(1) { '@slow' }
  },
  {
    name: 'FT.DROPINDEX',
    arity: -1,
    flags: Set(2) { 'write', 'module' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(4) { '@write', '@slow', '@dangerous', '@search' }
  },
  {
    name: 'zpopmin',
    arity: -2,
    flags: Set(2) { 'write', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@sortedset', '@fast' }
  },
  {
    name: 'sinter',
    arity: -2,
    flags: Set(1) { 'readonly' },
    firstKeyIndex: 1,
    lastKeyIndex: -1,
    step: 1,
    categories: Set(3) { '@read', '@set', '@slow' }
  },
  {
    name: 'zscore',
    arity: 3,
    flags: Set(2) { 'readonly', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@sortedset', '@fast' }
  },
  {
    name: 'bitfield',
    arity: -2,
    flags: Set(2) { 'write', 'denyoom' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@bitmap', '@slow' }
  },
  {
    name: 'lrange',
    arity: 4,
    flags: Set(1) { 'readonly' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@list', '@slow' }
  },
  {
    name: 'renamenx',
    arity: 3,
    flags: Set(2) { 'write', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 2,
    step: 1,
    categories: Set(3) { '@keyspace', '@write', '@fast' }
  },
  {
    name: 'bf.madd',
    arity: -3,
    flags: Set(3) { 'write', 'denyoom', 'module' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(2) { '@write', '@bloom' }
  },
  {
    name: 'ts.decrby',
    arity: -3,
    flags: Set(3) { 'write', 'denyoom', 'module' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(2) { '@write', '@timeseries' }
  },
  {
    name: 'punsubscribe',
    arity: -1,
    flags: Set(4) { 'pubsub', 'noscript', 'loading', 'stale' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(2) { '@pubsub', '@slow' }
  },
  {
    name: 'FT.HYBRID',
    arity: -1,
    flags: Set(2) { 'readonly', 'module' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(2) { '@read', '@search' }
  },
  {
    name: 'ts.get',
    arity: -2,
    flags: Set(2) { 'readonly', 'module' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@fast', '@timeseries' }
  },
  {
    name: 'psetex',
    arity: 4,
    flags: Set(2) { 'write', 'denyoom' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@string', '@slow' }
  },
  {
    name: 'object',
    arity: -2,
    flags: Set(0) {},
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(1) { '@slow' }
  },
  {
    name: 'georadiusbymember',
    arity: -5,
    flags: Set(3) { 'write', 'denyoom', 'movablekeys' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@geo', '@slow' }
  },
  {
    name: 'bf.reserve',
    arity: -4,
    flags: Set(3) { 'write', 'denyoom', 'module' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@fast', '@bloom' }
  },
  {
    name: 'hstrlen',
    arity: 3,
    flags: Set(2) { 'readonly', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@hash', '@fast' }
  },
  {
    name: 'config',
    arity: -2,
    flags: Set(0) {},
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(1) { '@slow' }
  },
  {
    name: 'brpop',
    arity: -3,
    flags: Set(2) { 'write', 'blocking' },
    firstKeyIndex: 1,
    lastKeyIndex: -2,
    step: 1,
    categories: Set(4) { '@write', '@list', '@slow', '@blocking' }
  },
  {
    name: 'delex',
    arity: -2,
    flags: Set(2) { 'write', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@string', '@fast' }
  },
  {
    name: 'discard',
    arity: 1,
    flags: Set(5) { 'noscript', 'loading', 'stale', 'fast', 'allow_busy' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(2) { '@fast', '@transaction' }
  },
  {
    name: 'bf.card',
    arity: 2,
    flags: Set(3) { 'readonly', 'module', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@fast', '@bloom' }
  },
  {
    name: 'zrandmember',
    arity: -2,
    flags: Set(1) { 'readonly' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@sortedset', '@slow' }
  },
  {
    name: 'hset',
    arity: -4,
    flags: Set(3) { 'write', 'denyoom', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@hash', '@fast' }
  },
  {
    name: 'FT.SYNADD',
    arity: -1,
    flags: Set(3) { 'write', 'denyoom', 'module' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(1) { '@search' }
  },
  {
    name: 'xtrim',
    arity: -4,
    flags: Set(1) { 'write' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@stream', '@slow' }
  },
  {
    name: 'lrem',
    arity: 4,
    flags: Set(1) { 'write' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@list', '@slow' }
  },
  {
    name: 'randomkey',
    arity: 1,
    flags: Set(1) { 'readonly' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(3) { '@keyspace', '@read', '@slow' }
  },
  {
    name: 'cf.del',
    arity: 3,
    flags: Set(3) { 'write', 'module', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(2) { '@write', '@cuckoo' }
  },
  {
    name: 'wait',
    arity: 3,
    flags: Set(1) { 'blocking' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(3) { '@slow', '@blocking', '@connection' }
  },
  {
    name: 'info',
    arity: -1,
    flags: Set(2) { 'loading', 'stale' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(2) { '@slow', '@dangerous' }
  },
  {
    name: 'digest',
    arity: 2,
    flags: Set(2) { 'readonly', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@string', '@fast' }
  },
  {
    name: 'lpushx',
    arity: -3,
    flags: Set(3) { 'write', 'denyoom', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@list', '@fast' }
  },
  {
    name: 'cms.initbydim',
    arity: 4,
    flags: Set(3) { 'write', 'denyoom', 'module' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@fast', '@cms' }
  },
  {
    name: 'FT._DROPIFX',
    arity: -1,
    flags: Set(2) { 'write', 'module' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(2) { '@write', '@search' }
  },
  {
    name: 'zrevrank',
    arity: -3,
    flags: Set(2) { 'readonly', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@sortedset', '@fast' }
  },
  {
    name: 'debug',
    arity: -2,
    flags: Set(4) { 'admin', 'noscript', 'loading', 'stale' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(3) { '@admin', '@slow', '@dangerous' }
  },
  {
    name: 'FT.ALIASUPDATE',
    arity: -1,
    flags: Set(3) { 'write', 'denyoom', 'module' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(1) { '@search' }
  },
  {
    name: 'ts.info',
    arity: -2,
    flags: Set(2) { 'readonly', 'module' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@fast', '@timeseries' }
  },
  {
    name: 'pexpireat',
    arity: -3,
    flags: Set(2) { 'write', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@keyspace', '@write', '@fast' }
  },
  {
    name: 'hincrby',
    arity: 4,
    flags: Set(3) { 'write', 'denyoom', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@hash', '@fast' }
  },
  {
    name: 'getdel',
    arity: 2,
    flags: Set(2) { 'write', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@string', '@fast' }
  },
  {
    name: 'FT._ALIASADDIFNX',
    arity: -1,
    flags: Set(3) { 'write', 'denyoom', 'module' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(1) { '@search' }
  },
  {
    name: 'xpending',
    arity: -3,
    flags: Set(1) { 'readonly' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@stream', '@slow' }
  },
  {
    name: 'hdel',
    arity: -3,
    flags: Set(2) { 'write', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@hash', '@fast' }
  },
  {
    name: 'linsert',
    arity: 5,
    flags: Set(2) { 'write', 'denyoom' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@list', '@slow' }
  },
  {
    name: 'fcall_ro',
    arity: -3,
    flags: Set(6) {
      'readonly',
      'noscript',
      'stale',
      'skip_monitor',
      'no_mandatory_keys',
      'movablekeys'
    },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(2) { '@slow', '@scripting' }
  },
  {
    name: 'topk.query',
    arity: -3,
    flags: Set(2) { 'readonly', 'module' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(2) { '@read', '@topk' }
  },
  {
    name: 'incrbyfloat',
    arity: 3,
    flags: Set(3) { 'write', 'denyoom', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@string', '@fast' }
  },
  {
    name: 'VINFO',
    arity: 2,
    flags: Set(3) { 'readonly', 'module', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(0) {}
  },
  {
    name: 'tdigest.cdf',
    arity: -3,
    flags: Set(2) { 'readonly', 'module' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@fast', '@tdigest' }
  },
  {
    name: 'pfmerge',
    arity: -2,
    flags: Set(2) { 'write', 'denyoom' },
    firstKeyIndex: 1,
    lastKeyIndex: -1,
    step: 1,
    categories: Set(3) { '@write', '@hyperloglog', '@slow' }
  },
  {
    name: 'save',
    arity: 1,
    flags: Set(4) { 'admin', 'noscript', 'no_async_loading', 'no_multi' },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(3) { '@admin', '@slow', '@dangerous' }
  },
  {
    name: 'msetnx',
    arity: -3,
    flags: Set(2) { 'write', 'denyoom' },
    firstKeyIndex: 1,
    lastKeyIndex: -1,
    step: 2,
    categories: Set(3) { '@write', '@string', '@slow' }
  },
  {
    name: 'zrem',
    arity: -3,
    flags: Set(2) { 'write', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@sortedset', '@fast' }
  },
  {
    name: 'zcard',
    arity: 2,
    flags: Set(2) { 'readonly', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@sortedset', '@fast' }
  },
  {
    name: 'ts.create',
    arity: -2,
    flags: Set(3) { 'write', 'denyoom', 'module' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@fast', '@timeseries' }
  },
  {
    name: 'zrevrangebyscore',
    arity: -4,
    flags: Set(1) { 'readonly' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@sortedset', '@slow' }
  },
  {
    name: 'get',
    arity: 2,
    flags: Set(2) { 'readonly', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@read', '@string', '@fast' }
  },
  {
    name: 'auth',
    arity: -2,
    flags: Set(6) {
      'noscript',
      'loading',
      'stale',
      'fast',
      'no_auth',
      'allow_busy'
    },
    firstKeyIndex: 0,
    lastKeyIndex: 0,
    step: 0,
    categories: Set(2) { '@fast', '@connection' }
  },
  {
    name: 'blmove',
    arity: 6,
    flags: Set(3) { 'write', 'denyoom', 'blocking' },
    firstKeyIndex: 1,
    lastKeyIndex: 2,
    step: 1,
    categories: Set(4) { '@write', '@list', '@slow', '@blocking' }
  },
  {
    name: 'rpop',
    arity: -2,
    flags: Set(2) { 'write', 'fast' },
    firstKeyIndex: 1,
    lastKeyIndex: 1,
    step: 1,
    categories: Set(3) { '@write', '@list', '@fast' }
  },
  ... 313 more items
]
```

```log
  const commands = await client.command();
  console.log(commands.map(c => c.name))
[
  'cf.count',       'zrangebylex',       'FT.DEL',
  'lset',           'cf.scandump',       'VCARD',
  'getrange',       'FT.EXPLAIN',        'hexpireat',
  'hpexpire',       'bzpopmin',          'zrange',
  'xclaim',         'spublish',          'FT.AGGREGATE',
  'lindex',         'ssubscribe',        'tdigest.create',
  'cms.merge',      'bitpos',            'sintercard',
  'topk.count',     'json.clear',        'json.objlen',
  'sscan',          'xadd',              'tdigest.byrevrank',
  'rpush',          'pfdebug',           'keys',
  'FT.CONFIG',      'VGETATTR',          'xinfo',
  'FT.DROP',        'unlink',            'flushall',
  'append',         'memory',            'FT.DROPINDEX',
  'zpopmin',        'sinter',            'zscore',
  'bitfield',       'lrange',            'renamenx',
  'bf.madd',        'ts.decrby',         'punsubscribe',
  'FT.HYBRID',      'ts.get',            'psetex',
  'object',         'georadiusbymember', 'bf.reserve',
  'hstrlen',        'config',            'brpop',
  'delex',          'discard',           'bf.card',
  'zrandmember',    'hset',              'FT.SYNADD',
  'xtrim',          'lrem',              'randomkey',
  'cf.del',         'wait',              'info',
  'digest',         'lpushx',            'cms.initbydim',
  'FT._DROPIFX',    'zrevrank',          'debug',
  'FT.ALIASUPDATE', 'ts.info',           'pexpireat',
  'hincrby',        'getdel',            'FT._ALIASADDIFNX',
  'xpending',       'hdel',              'linsert',
  'fcall_ro',       'topk.query',        'incrbyfloat',
  'VINFO',          'tdigest.cdf',       'pfmerge',
  'save',           'msetnx',            'zrem',
  'zcard',          'ts.create',         'zrevrangebyscore',
  'get',            'auth',              'blmove',
  'rpop',
  ... 313 more items
]
```

```js
node hash-voting-system.js

const util = require("util");
const redis = require("redis");

async function main() {
  const client = await redis.createClient();
  await client.connect();

  const commands = await client.command();
  console.log(
    util.inspect(
      commands.map((c) => c.name),
      { maxArrayLength: null },
    ),
  );
}

[
  'cf.count',
  'zrangebylex',
  'FT.DEL',
  'lset',
  'cf.scandump',
  'VCARD',
  'getrange',
  'FT.EXPLAIN',
  'hexpireat',
  'hpexpire',
  'bzpopmin',
  'zrange',
  'xclaim',
  'spublish',
  'FT.AGGREGATE',
  'lindex',
  'ssubscribe',
  'tdigest.create',
  'cms.merge',
  'bitpos',
  'sintercard',
  'topk.count',
  'json.clear',
  'json.objlen',
  'sscan',
  'xadd',
  'tdigest.byrevrank',
  'rpush',
  'pfdebug',
  'keys',
  'FT.CONFIG',
  'VGETATTR',
  'xinfo',
  'FT.DROP',
  'unlink',
  'flushall',
  'append',
  'memory',
  'FT.DROPINDEX',
  'zpopmin',
  'sinter',
  'zscore',
  'bitfield',
  'lrange',
  'renamenx',
  'bf.madd',
  'ts.decrby',
  'punsubscribe',
  'FT.HYBRID',
  'ts.get',
  'psetex',
  'object',
  'georadiusbymember',
  'bf.reserve',
  'hstrlen',
  'config',
  'brpop',
  'delex',
  'discard',
  'bf.card',
  'zrandmember',
  'hset',
  'FT.SYNADD',
  'xtrim',
  'lrem',
  'randomkey',
  'cf.del',
  'wait',
  'info',
  'digest',
  'lpushx',
  'cms.initbydim',
  'FT._DROPIFX',
  'zrevrank',
  'debug',
  'FT.ALIASUPDATE',
  'ts.info',
  'pexpireat',
  'hincrby',
  'getdel',
  'FT._ALIASADDIFNX',
  'xpending',
  'hdel',
  'linsert',
  'fcall_ro',
  'topk.query',
  'incrbyfloat',
  'VINFO',
  'tdigest.cdf',
  'pfmerge',
  'save',
  'msetnx',
  'zrem',
  'zcard',
  'ts.create',
  'zrevrangebyscore',
  'get',
  'auth',
  'blmove',
  'rpop',
  'cf.insert',
  'georadiusbymember_ro',
  'json.mset',
  'VRANDMEMBER',
  'script',
  'decr',
  'scan',
  'ts.queryindex',
  'zcount',
  'ts.deleterule',
  'FT._LIST',
  'FT.SUGLEN',
  'tdigest.add',
  'echo',
  'bzmpop',
  'ts.mget',
  'select',
  'reset',
  'dbsize',
  'VSIM',
  'hget',
  'role',
  'FT.MGET',
  'zunionstore',
  'json.arrinsert',
  'bgrewriteaof',
  'ts.revrange',
  'FT.ALTER',
  'setbit',
  'smove',
  'psubscribe',
  'brpoplpush',
  'replconf',
  'zdiffstore',
  'xackdel',
  'hrandfield',
  'hexpiretime',
  'setrange',
  'bf.loadchunk',
  'hkeys',
  'zmscore',
  'setex',
  'FT.SEARCH',
  'sdiffstore',
  'topk.incrby',
  'replicaof',
  'hpexpireat',
  'mset',
  'ts.createrule',
  'tdigest.max',
  'pexpiretime',
  'cf.reserve',
  'pubsub',
  'zincrby',
  'json.set',
  'bf.insert',
  'latency',
  'hpersist',
  'FT.GET',
  'VISMEMBER',
  'json.del',
  'ts.mrange',
  'lastsave',
  'time',
  'readonly',
  'json.debug',
  'geohash',
  'FT.SAFEADD',
  'json.toggle',
  'hlen',
  'sinterstore',
  '_FT.DEBUG',
  'VREM',
  'lcs',
  'ts.range',
  'lmove',
  'hpttl',
  'expire',
  'FT.SUGDEL',
  'blmpop',
  'zrank',
  'cms.info',
  'json.forget',
  'bitfield_ro',
  'georadius_ro',
  'FT.SUGGET',
  'georadius',
  '_FT.CONFIG',
  'ts.alter',
  'cf.compact',
  'strlen',
  'bf.debug',
  'tdigest.merge',
  'VLINKS',
  'llen',
  'blpop',
  'module',
  'flushdb',
  'scard',
  'eval_ro',
  'failover',
  'getset',
  'hmget',
  'search.CLUSTERINFO',
  'lpop',
  'hmset',
  'geosearchstore',
  'json.arrindex',
  'hexists',
  'zpopmax',
  'persist',
  'topk.add',
  'expireat',
  'evalsha_ro',
  'json.strappend',
  'FT.TAGVALS',
  'xautoclaim',
  'zrevrange',
  'bzpopmax',
  'hgetall',
  'slowlog',
  'unwatch',
  'psync',
  'VSETATTR',
  'hvals',
  'cf.add',
  'FT.DICTADD',
  'json.type',
  'FT.SYNDUMP',
  'json.arrpop',
  'dump',
  'FT._ALTERIFNX',
  'json.arrappend',
  'hpexpiretime',
  'tdigest.byrank',
  'trimslots',
  'getbit',
  'VDIM',
  'pexpire',
  'zmpop',
  'touch',
  'bgsave',
  'zremrangebylex',
  'geodist',
  'FT.ADD',
  'hsetex',
  'xdel',
  'geopos',
  'FT.SYNUPDATE',
  'zdiff',
  'VADD',
  'ltrim',
  'decrby',
  'setnx',
  'json.get',
  'shutdown',
  'tdigest.revrank',
  'xsetid',
  'FT._ALIASDELIFX',
  'cf.mexists',
  'json.mget',
  'pfcount',
  'exec',
  'FT._DROPINDEXIFX',
  'mget',
  'smismember',
  'hexpire',
  'incr',
  'client',
  'pfadd',
  'copy',
  'cf.debug',
  'zremrangebyscore',
  'asking',
  'lpos',
  'json.objkeys',
  'tdigest.trimmed_mean',
  'readwrite',
  'bf.exists',
  'ts.del',
  'lpush',
  'hincrbyfloat',
  'cf.loadchunk',
  'bitop',
  'sdiff',
  'xlen',
  'search.CLUSTERREFRESH',
  'xgroup',
  'ttl',
  'hsetnx',
  'tdigest.rank',
  'FT.ALIASDEL',
  'type',
  'publish',
  'tdigest.min',
  'ts.madd',
  'acl',
  'sismember',
  'getex',
  'hgetdel',
  'unsubscribe',
  'restore',
  'cms.incrby',
  'FT.PROFILE',
  'exists',
  'zremrangebyrank',
  'tdigest.info',
  'zrevrangebylex',
  'FT.SUGADD',
  'evalsha',
  'tdigest.quantile',
  'migrate',
  'zintercard',
  'VEMB',
  'srem',
  'xack',
  'msetex',
  'lolwut',
  'incrby',
  'xread',
  'tdigest.reset',
  'rename',
  'topk.reserve',
  'smembers',
  'FT.DICTDUMP',
  'bf.info',
  'zrangestore',
  'topk.info',
  'eval',
  'pfselftest',
  'FT._CREATEIFNX',
  'function',
  'xrevrange',
  'json.resp',
  'del',
  'zinter',
  'json.merge',
  'sort_ro',
  'VRANGE',
  'geoadd',
  'multi',
  'bf.scandump',
  'search.CLUSTERSET',
  'set',
  'sadd',
  'watch',
  'restore-asking',
  'FT.ALIASADD',
  'FT.CREATE',
  'timeseries.REFRESHCLUSTER',
  'httl',
  'cms.initbyprob',
  'json.numincrby',
  'sort',
  'srandmember',
  'bf.add',
  'expiretime',
  'topk.list',
  'json.numpowby',
  'zunion',
  'FT.DICTDEL',
  'zrangebyscore',
  'FT.EXPLAINCLI',
  'zadd',
  'zscan',
  'cms.query',
  'geosearch',
  'ts.add',
  'cf.exists',
  'xdelex',
  'FT.CURSOR',
  'bitcount',
  'cluster',
  'spop',
  'sunsubscribe',
  'swapdb',
  'waitaof',
  'pttl',
  'fcall',
  'json.arrlen',
  'sunion',
  'FT.SPELLCHECK',
  'move',
  'bf.mexists',
  'sunionstore',
  'ts.mrevrange',
  'xrange',
  'cf.info',
  'rpoplpush',
  'monitor',
  'ts.incrby',
  'json.arrtrim',
  'json.strlen',
  'sync',
  'hello',
  'json.nummultby',
  'rpushx',
  'hgetex',
  'zlexcount',
  'quit',
  'ping',
  'FT.INFO',
  'slaveof',
  'zinterstore',
  'xreadgroup',
  'substr',
  'hscan',
  'cf.addnx',
  'timeseries.CLUSTERSET',
  'lmpop',
  'command',
  'subscribe',
  'cf.insertnx'
]
```


```js
~/gitclone/playground/content_base/redis/playground $ !!
node hash-voting-system.js
Title: Maxwell Dayvson's Github page
Author: undefined
Link: https://github.com/dayvson
Score: 2
--------------------------
Title: Hugo Travares's Github page
Author: undefined
Link: https://github.com/hltbra
Score: 1
--------------------------
~/gitclone/playground/content_base/redis/playground $ cat !$
cat hash-voting-system.js
const util = require("util");
const redis = require("redis");

async function main() {
  const client = await redis.createClient();
  await client.connect();

  // const commands = await client.command();
  // console.log(
  //   util.inspect(
  //     commands.map((c) => c.name),
  //     { maxArrayLength: null },
  //   ),
  // );

  await saveLink(
    client,
    123,
    "dayvson",
    "Maxwell Dayvson's Github page",
    "https://github.com/dayvson",
  );
  await upVote(client, 123);
  await upVote(client, 123);
  await saveLink(
    client,
    456,
    "hltbra",
    "Hugo Travares's Github page",
    "https://github.com/hltbra",
  );
  await upVote(client, 456);
  await upVote(client, 456);
  await downVote(client, 456);

  showDetails(await getDetails(client, 123));
  showDetails(await getDetails(client, 456));

  await client.quit();
}

async function saveLink(client, id, auther, title, link) {
  await client.hSet(`link:${id}`, { auther, title, link, score: 0 });
}

async function upVote(client, id) {
  await client.hIncrBy(`link:${id}`, `score`, 1);
}

async function downVote(client, id) {
  await client.hIncrBy(`link:${id}`, `score`, -1);
}

async function getDetails(client, id) {
  return await client.hGetAll(`link:${id}`);
}

function showDetails(replies) {
  console.log(`Title: ${replies["title"]}`);
  console.log(`Author: ${replies["author"]}`);
  console.log(`Link: ${replies["link"]}`);
  console.log(`Score: ${replies["score"]}`);
  console.log(`--------------------------`);
}

main();
```

```bash
SADD user:max:favorite_artists "Arcade Fire" "Arctic Monkeys" "Belle & Sebastian" "Lenine"
SADD user:hugo:favorite_artists "Daft Punk" "The Kooks" "Arctic Monkeys"

SINTER user:max:favorite_artists user:hugo:favorite_artists
SDIFF user:max:favorite_artists user:hugo:favorite_artists
SDIFF user:hugo:favorite_artists user:max:favorite_artists
SUNION user:hugo:favorite_artists user:max:favorite_artists
SRANDMEMBER user:hugo:favorite_artists
SISMEMBER user:hugo:favorite_artists "Arctic Monkeys"
SCARD user:max:favorite_artists
SMEMBERS user:max:favorite_artists
```

```
ZADD leaders 100 'Alice'
ZADD leaders 100 'Zed'
ZADD leaders 102 'Hugo'
ZADD leaders 101 'Max'

ZREVRANGE leaders 0 -1
ZREVRANGE leaders 0 -1 WITHSCORES

ZREM leaders 'Hugo'

SETBIT visits:2015-01-01 10 1
SETBIT visits:2015-01-01 15 1
SETBIT visits:2015-01-02 10 1
SETBIT visits:2015-01-02 11 1

GETBIT visits:2015-01-01 10
GETBIT visits:2015-01-02 15

BITCOUNT visits:2015-01-01
BITCOUNT visits:2015-01-02

BITOP OR total_users visits:2015-01-01 visits:2015-01-02
BITCOUNT total_users
```
