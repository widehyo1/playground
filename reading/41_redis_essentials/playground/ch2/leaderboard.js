const redis = require("redis");

async function main() {
  const client = redis.createClient();
  await client.connect();

  const leaderBoard = new LeaderBoard("game-score");
  await leaderBoard.addUser(client, "Arther", 70);
  await leaderBoard.addUser(client, "KC", 20);
  await leaderBoard.addUser(client, "Maxwell", 10);
  await leaderBoard.addUser(client, "Patrik", 30);
  await leaderBoard.addUser(client, "Ana", 60);
  await leaderBoard.addUser(client, "Felipe", 40);
  await leaderBoard.addUser(client, "Renata", 50);
  await leaderBoard.addUser(client, "Hugo", 80);

  await leaderBoard.removeUser(client, "Arther");

  await leaderBoard.getUserScoreAndRank(client, "Maxwell");

  await leaderBoard.showTopUsers(client, 3);

  const users = await leaderBoard.getUsersAroundUser(client, "Felipe", 5);
  console.log(`\nUsers around Felipe:`);
  users.forEach((user) =>
    console.log(`# ${user.rank} User: ${user.username}, score: ${user.score}`),
  );

  await client.quit();
}

function LeaderBoard(key) {
  this.key = key;
}

const lp = LeaderBoard.prototype;
lp.addUser = async function (client, username, score) {
  const replies = await client.zAdd(this.key, [{score, value: username}]);
  console.log(`User ${username} added to the leaderboard!`);
};

lp.removeUser = async function (client, username) {
  const replies = await client.zRem(this.key, username);
  console.log(`User ${username} removed successfully!`);
};

lp.getUserScoreAndRank = async function (client, username) {
  const leaderboardKey = this.key;
  const zscoreReply = await client.zScore(leaderboardKey, username);
  const zrevrankReply = await client.zRevRank(leaderboardKey, username);
  console.log(`\nDetails of ${username}:`);
  console.log(`Score: ${zscoreReply}, Rank: # ${zrevrankReply + 1}`);
};

lp.showTopUsers = async function (client, quantity) {
  const reply = await client.zRangeWithScores(
    this.key,
    0,
    quantity - 1,
    {REV: true},
  );
  console.log(`\nTop ${quantity} users:`);
  for (let i = 0; i < reply.length; i++) {
    console.log(`# ${i + 1} User: ${reply[i].value}, Score: ${reply[i].score}`);
  }
};

lp.getUsersAroundUser = async function (client, username, quantity) {
  const leaderboardKey = this.key;
  const zrevrankReply = await client.zRevRank(leaderboardKey, username);
  const startOffset = Math.max(Math.floor(zrevrankReply - quantity / 2 + 1), 0);
  const endOffset = startOffset + quantity - 1;
  const zrevrangeReply = await client.zRangeWithScores(
    leaderboardKey,
    startOffset,
    endOffset,
    {REV: true},
  );
  let users = [];
  for (let i = 0; i < zrevrangeReply.length; i++) {
    const user = {
      rank: startOffset + i,
      username: zrevrangeReply[i].value,
      score: zrevrangeReply[i].score,
    };
    users.push(user);
  }
  return users;
};

main();
