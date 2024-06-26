type Func = (...params: number[]) => number

function memoize(fn: Func): Func {
    const cache = {}
    return function(...args) {
        const s = args.toString();
        if(cache[s] != undefined) return cache[s]
        
        const result = fn(...args)
        cache[s] = result
        return result
        
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */