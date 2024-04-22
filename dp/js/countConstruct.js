// O(n m^2) time, O(m^2) space
let memo = {}
function countConstruct(target,words){
    if(target in memo) return memo[target]
    if(target === '') return 1

    let count = 0

    for(let w of words){
        if(target.indexOf(w) === 0){
            const surfix = target.slice(w.length)
            count += countConstruct(surfix,words)
        }
    }
    memo[target] = count
    return count
}

console.log(countConstruct('abcdef',['abc','def']))
console.log(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['ef','ee','eee','e','eeeeeee','eeeee','eeeeeeeeeeeeeeeeeeeee']))