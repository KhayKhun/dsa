class TimeLimitedCache {
    store = {} // values -> [val , timeout] [] [] []
    constructor() {}
    
    set(key: number, value: number, duration: number): boolean {
        // existed => true (overwrite -> value, duration)
        if(this.store[key]){
            this.store[key] = [value, setTimeout(()=>0,duration)]
            return true
        }else{
            this.store[key] = [value, setTimeout(()=>0,duration)]
            return false
        }
    }
    
    get(key: number): number { // return value, else -1
        if(this.store[key] && this.store[key][1]._destroyed === false){ // exists and not destoryed
            return this.store[key][0]
        }
        else return -1
    }
    
    count(): number { // count of available keys
        const exists = Object.values(this.store).filter((x:any) => !x[1]._destroyed)
        return exists.length
    }
}

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */