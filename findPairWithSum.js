function findPairsWithSum(arr, targetSum) {
  const seenNumbers = new Map();
  const result = [];

  for (const currentNumber of arr) {
    const complement = targetSum - currentNumber;

    if (seenNumbers.has(complement)) {
      result.push([complement, currentNumber]);
    }

    seenNumbers.set(currentNumber, true);
  }

  // Remove duplicates by converting the result to a Set and then back to an array
  return Array.from(new Set(result));
}

// Example usage
const arr = [10, -4, 1, 5, 2, 4, 100, -94, 1, 2, 3, 4, 0];
const targetSum = 6;

const pairs = findPairsWithSum(arr, targetSum);
console.log(pairs); 
