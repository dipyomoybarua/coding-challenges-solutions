// Example of an idempotent function to increment a counter
let counter = 0;

function incrementCounter() {
    counter++;
    console.log("Counter:", counter);

}

// Performing the operation multiple times
incrementCounter();  // Output: Counter: 1
incrementCounter();  // Output: Counter: 2
incrementCounter();  // Output: Counter: 3
