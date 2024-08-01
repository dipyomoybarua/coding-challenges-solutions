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

// // Given array
// let arr = [1, 2, 5, 6, 10, 12];

// // Step 1: Find the minimum and maximum values in the array
// let min = arr[0];
// let max = arr[0];

// for (let i = 1; i < arr.length; i++) {
//   if (arr[i] < min) {
//     min = arr[i];
//   }
//   if (arr[i] > max) {
//     max = arr[i];
//   }
// }

// // Step 2: Create a function to check if a number is in the array
// function isInArray(number, array) {
//   for (let i = 0; i < array.length; i++) {
//     if (array[i] === number) {
//       return true;
//     }
//   }
//   return false;
// }

// // Step 3: Find the missing numbers
// let missingNumbers = [];
// for (let i = min; i <= max; i++) {
//   if (!isInArray(i, arr)) {
//     missingNumbers.push(i);
//   }
// }

// console.log(missingNumbers); 
