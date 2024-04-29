type P = Promise<number>

async function addTwoPromises(promise1: P, promise2: P): P {
    return promise1.then(a => promise2.then(b => a + b))
};

async function sleep(millis: number): Promise<void> {
    return new Promise((res) => 
        setTimeout(()=> res(),millis)   
    )
}
