type F<T> = () => Promise<T>

function promiseAll<T>(functions: F<T>[]): Promise<T[]> {
    const promises = functions.map(x => x())
    return new Promise((res,rej) => {
        Promise.all(promises)
        .then((outputs)=> {
            res(outputs)
        })
        .catch(()=>rej("Error"))
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */