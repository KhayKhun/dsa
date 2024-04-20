// O(2^n) time, O(n) space
// function fib(n){
//     if (n <= 2) return 1
//     return fib(n-1) + fib(n-2);
// }
// 0(n)
function fib(n,memo = {}){
    console.log(n,memo)
    if (n in memo) return memo[n]
    if (n <= 1) return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo);
    return memo[n]
}
console.log(fib(100))