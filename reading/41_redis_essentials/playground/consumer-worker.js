const redis = require("redis");
const queue = require("./queue");

async function main() {
  const client = await redis.createClient();
  await client.connect();
  const logsQueue = new queue.Queue("logs", client);

  await logMessages(logsQueue);
}

async function logMessages(logsQueue) {
  const message = await logsQueue.pop();
  console.log(`[consumer] got log: ${message}`);

  const size = await logsQueue.size();
  console.log(`${size} logs left`);

  logMessages(logsQueue);
}

main();
