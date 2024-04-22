function allConstruct(target,words){
    if(target === '') return [[]]
    const res = []
    for(let w of words){
        if(target.indexOf(w) === 0){
            const remain = target.slice(w.length)
            const ways = allConstruct(remain,words)
            const results = ways.map(way => [w, ...way])
            res.push(...results) // push results's items
        }
    }
    return res
}

console.log(allConstruct('eeeeeee',['e','ee','eee','e','eeeeeee','eeeee','eeeeeeeeeeeeeeeeeeeee']))
console.log(allConstruct('purple',['purp','p','ur','le','purpl']))