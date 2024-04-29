type Fn = (...params: any[]) => Promise<any>;

function timeLimit(fn: Fn, t: number): Fn {
    
    return async function(...args) {
        return new Promise((res,rej) => {
            const timer = setTimeout(()=>{
                rej("Time Limit Exceeded")
            },t)
            fn(...args).then((output)=>{
                clearTimeout(timer)
                res(output)
            }).catch((message)=>{
                clearTimeout(timer)
                rej(message)
            })
        })
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */