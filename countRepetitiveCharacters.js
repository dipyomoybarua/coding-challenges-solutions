//Initialize the String
let inputString = "https://www.cricbuzz.com/";

// object to store character counts
let charCount = {};

//Iterate through the String
for (let char of inputString) {
    // Step 4: Update Counts
    if (charCount[char]) {
      charCount[char]++;
    } else {
      charCount[char] = 1;
    }
  }
  

// Print Results
for (let char in charCount) {
  if (charCount[char] > 1) {
    console.log(`Character: '${char}' appears ${charCount[char]} times`);
  }
}
