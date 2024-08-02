// Given array
let arr = [1,2,5,6,10,12,17,100];

// Step 1: Create a set from the array
let numSet = new Set(arr);

// Step 2: Find the minimum and maximum values in the array
let min = Math.min(...arr);
let max = Math.max(...arr);

// Step 3: Find the missing numbers
let missingNumbers = [];
for (let i = min; i <= max; i++) {
  if (!numSet.has(i)) {
    missingNumbers.push(i);
  }
}

console.log(missingNumbers); 