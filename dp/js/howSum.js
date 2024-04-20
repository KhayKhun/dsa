function howSum(list,k){
    let res = []
    function explore(current,target){
        for(let i of list){
            const x = target - i
            if(x < 0) continue
            if(x === 0){
                res.push(current.concat([i]))
                continue
            }
            explore(current.concat([i]), x)
        }
    }
    explore([],k)
    return res
}

console.log(howSum([3,4,7],7))