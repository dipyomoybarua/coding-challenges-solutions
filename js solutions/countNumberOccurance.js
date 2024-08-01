// Step 1: Initialize the Array
let contents = [1, 2, 1, 1, 2, 3, 4];

// Step 2: Initialize a Counter Object
let countObject = {};

// Step 3: Iterate through the Array
for (let num of contents) {
  // Step 4: Update Counts
  if (countObject[num]) {
    countObject[num]++;
  } else {
    countObject[num] = 1;
  }
}

// Step 5: Return the Count Object
console.log(countObject);
