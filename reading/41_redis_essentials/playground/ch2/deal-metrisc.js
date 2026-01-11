const redis = require("redis");

async function main() {
  const client = redis.createClient();
  await client.connect();

  await markDealAsSent(client, "deal:1", "user:1");
  await markDealAsSent(client, "deal:1", "user:2");
  await markDealAsSent(client, "deal:2", "user:1");
  await markDealAsSent(client, "deal:2", "user:3");

  await sendDealIfNotSent(client, "deal:1", "user:1");
  await sendDealIfNotSent(client, "deal:1", "user:2");
  await sendDealIfNotSent(client, "deal:1", "user:3");

  await showUsersThatReceivedAllDeals(client, ["deal:1", "deal:2"]);
  await showUsersThatReceivedAtLeastOneOfTheDeals(client, ["deal:1", "deal:2"]);

  await client.quit();
}

async function markDealAsSent(client, dealId, userId) {
  await client.sAdd(dealId, userId);
}

async function sendDealIfNotSent(client, dealId, userId) {
  const reply = await client.sIsMember(dealId, userId);
  if (reply) {
    console.log(`Deal ${dealId} was already sent to user ${userId}`);
  } else {
    console.log(`Sending ${dealId} to user ${userId}`);
    markDealAsSent(client, dealId, userId);
  }
}

async function showUsersThatReceivedAllDeals(client, dealIds) {
  const reply = await client.sInter(dealIds);
  console.log(`${reply} received all of the deals: ${dealIds}`);
}

async function showUsersThatReceivedAtLeastOneOfTheDeals(client, dealIds) {
  const reply = await client.sUnion(dealIds);
  console.log(`${reply} received at least one of the deals: ${dealIds}`);
}

main();
