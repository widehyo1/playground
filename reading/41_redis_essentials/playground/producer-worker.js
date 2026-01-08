const redis = require("redis");
const queue = require("./queue");

async function main() {
  const client = await redis.createClient();
  await client.connect();
  const logsQueue = new queue.Queue("logs", client);
  const MAX = 5;
  for (let i = 0; i < MAX; i++) {
    await logsQueue.push(`Hello world #${i}`);
  }
  console.log(`Created ${MAX} logs`);
  await client.quit();
}

main();
