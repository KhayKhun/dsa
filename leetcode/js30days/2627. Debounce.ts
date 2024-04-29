type F = (...args: number[]) => void

function debounce(fn: F, t: number = 0): F {
    let timer = setTimeout(() => 0,t)
    
    return async function(...args) {
        clearTimeout(timer)
        timer = setTimeout(() => fn(...args),t)
    }
};

/**
 * const log = debounce(console.log, 100);
 * log('Hello'); // cancelled
 * log('Hello'); // cancelled
 * log('Hello'); // Logged at t=100ms
 */