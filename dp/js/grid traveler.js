function gridTraveler(a,b){
    const memo = {}
    function shrink(m,n){
        if(m === 0 || n === 0) return 0
        if(m === 1 && n === 1) return 1
        if(`${m},${n}` in memo) return memo[`${m},${n}`]
        memo[`${m},${n}`] =  shrink(m-1,n) + shrink(m,n-1)
        return memo[`${m},${n}`]
    }
    const res = shrink(a,b)
    return res
}

console.log(gridTraveler(18,18))