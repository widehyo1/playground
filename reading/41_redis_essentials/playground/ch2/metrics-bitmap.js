const redis = require("redis");

async function main() {
  const client = redis.createClient();
  await client.connect();

  await storeDailyVisit(client, "2015-01-01", "1");
  await storeDailyVisit(client, "2015-01-01", "2");
  await storeDailyVisit(client, "2015-01-01", "10");
  await storeDailyVisit(client, "2015-01-01", "55");

  await countVisits(client, "2015-01-01");
  await showUserIdsFromVisit(client, "2015-01-01");

  await client.quit();
}

async function storeDailyVisit(client, date, userId) {
  const key = `visits:daily:${date}`;
  const reply = await client.setBit(key, userId, 1);
  console.log(`User ${userId} visited on ${date}`);
}

async function countVisits(client, date) {
  const key = `visits:daily:${date}`;
  const reply = await client.bitCount(key);
  console.log(`${date} had ${reply} visits.`);
}

async function countVisits(client, date) {
  const key = `visits:daily:${date}`;
  const reply = await client.bitCount(key);
  console.log(`${date} had ${reply} visits.`);
}

async function showUserIdsFromVisit(client, date) {
  const key = `visits:daily:${date}`;
  console.log(key);
  console.log('flag0');
  const bitmapValue = await client.getBit(key);
  console.log('flag1');
  console.log(bitmapValue);
  console.log('flag2');
  const data = bitmapValue.toJSON().data;

  let userIds = [];
  console.log(data);
  data.forEach(function (byte, byteIndex) {
    for (let bitIndex = 7; bitIndex >= 0; bitIndex--) {
      const visited = (byte >> bitIndex) & 1;
      if (visited === 1) {
        const userId = byteIndex * 8 + (7 - bitIndex);
        userIds.push(userId);
      }
    }
  });
  console.log(`Users ${userIds} visited on ${date}`);
}

main();
