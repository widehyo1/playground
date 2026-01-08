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

async function saveLink(client, id, author, title, link) {
  await client.hSet(`link:${id}`, { author, title, link, score: 0 });
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
