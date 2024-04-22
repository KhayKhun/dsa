// O(n m^2) time, O(m^2) space
let memo = {}
function canConstruct(target,words){
    if(target in memo) return memo[target]
    if(target === '') return true

    for(let w of words){
        if(target.indexOf(w) === 0){
            const remain = target.slice(w.length)
            if(canConstruct(remain,words)){
                memo[remain] = true
                return true
            }
        }
    }
    memo[target] = false
    return false
}

console.log(canConstruct('abcdef',['abc','df']))
console.log(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','e','eeeeeee','eeeee','eeeeeeeeeeeeeeeeeeeee']))