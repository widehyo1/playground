const redis = require("redis");

function Queue(queueName, redisClient) {
  this.queueName = queueName;
  this.redisClient = redisClient;
  this.queueKey = `queues:${queueName}`;
  this.timeout = 0;
}

Queue.prototype.size = async function () {
  return await this.redisClient.lLen(this.queueKey);
};

Queue.prototype.push = async function (data) {
  await this.redisClient.lPush(this.queueKey, data);
};

Queue.prototype.pop = async function () {
  const res = await this.redisClient.brPop(this.queueKey, String(this.timeout));
  return res?.element;
};

module.exports = { Queue };
