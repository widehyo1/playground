const redis = require("redis");

async function main() {
  const client = redis.createClient();
  await client.connect();
  await client.set("my_key", "Hello world using node.js and redis");
  const value = await client.get("my_key", redis.print);
  console.log(value);
  await client.quit();
}

main();
