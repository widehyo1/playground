const fn = () => {}
const array = [1, "string", fn];

console.log(typeof array);
console.log(Object.prototype.toString.call(array));
