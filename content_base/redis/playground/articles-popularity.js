const redis = require("redis");

async function upVote(id, client) {
  const key = `article:${id}:votes`;
  await client.incr(key);
}

async function downVote(id, client) {
  const key = `article:${id}:votes`;
  await client.decr(key);
}

async function showResults(id, client) {
  const headlineKey = `article:${id}:headline`;
  const voteKey = `article:${id}:votes`;
  const replies = await client.mGet([headlineKey, voteKey]);
  console.log(`The article ${replies[0]} has ${replies[1]} votes`);
}

async function main() {
  const client = redis.createClient();
  await client.connect();
  await upVote(12345, client);
  await upVote(12345, client);
  await upVote(12345, client);
  await upVote(10001, client);
  await upVote(10001, client);
  await downVote(10001, client);
  await upVote(60056, client);

  await showResults(12345, client);
  await showResults(10001, client);
  await showResults(60056, client);

  await client.quit();
}

main();
