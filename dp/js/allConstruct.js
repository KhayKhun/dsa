// O(n m^2) time, O(m^2) space
let memo = {}
let res = []
function allConstruct(current,target,words){
    if(target in memo) return memo[target]
    if(target === ''){
        res.push(current)
        return
    }

    for(let w of words){
        if(target.indexOf(w) === 0){
            const remain = target.slice(w.length)
            memo[remain] = allConstruct([...current, w], remain, words)
        }
    }
    return
}

console.log(allConstruct([],'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','e','eeeeeee','eeeee','eeeeeeeeeeeeeeeeeeeee']))
console.log(res)