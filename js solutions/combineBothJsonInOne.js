// Step 1: Initialize the JSON Objects
let fruits = {'apple': 2, 'banana': 3, 'orange': 1};
let card = {'egg': 1, 'watermelon': 2, 'coconut': 1};

// Step 2: Create a New Object
let combinedJson = {};

// Step 3: Merge Properties
combinedJson = { ...fruits, ...card };

// Step 4: Return the Combined Object
console.log(combinedJson);
