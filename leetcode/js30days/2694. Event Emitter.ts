type Callback = (...args: any[]) => any;
type Subscription = {
    unsubscribe: () => void
}

class EventEmitter {
    eventMap = {}
    subscribe(eventName: string, callback: Callback): Subscription {
        if(this.eventMap[eventName]) this.eventMap[eventName].push(callback)
        else this.eventMap[eventName] = [callback]

        return {
            unsubscribe: () => {
                this.eventMap[eventName] = this.eventMap[eventName].filter(x => x != callback)
                return undefined
            }
        };
    }
    emit(eventName: string, args: any[] = []): any[] {
        if(this.eventMap[eventName]) return this.eventMap[eventName].map(x => x(...args))
        else return []       
    }
}

const x = [1,setTimeout(()=> 2,3000)]

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */