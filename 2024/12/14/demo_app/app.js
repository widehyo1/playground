function factorial(num) {
    if (num === 1) {
        return num;
    }
    return num * factorial(num - 1);
}

num = 5
console.log("=== App start ===");
result = factorial(num);
console.log(`result: ${result}`);
console.log("=== App end ===");
