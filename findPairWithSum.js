function findPairWithSum(arr, targetSum) {
    // Edge case: Handle empty array
    if (!arr || arr.length === 0) {
      return 'The array is empty.';
    }
  
    const seenNumbers = new Map();
  
    for (const num of arr) {
      const complement = targetSum - num;
  
      if (seenNumbers.has(complement)) {
        return `Pair found: (${complement}, ${num})`;
      }
  
      seenNumbers.set(num, true);
    }
  
    return 'No pair found that adds up to the target sum.';
  }
  
  // Example usage
  const arr = [2, 5, 6, 7, 10, 17];
  const targetSum = 7;
  
  console.log(findPairWithSum(arr, targetSum)); 
  console.log(findPairWithSum([], targetSum)); 
  console.log(findPairWithSum(arr, 20)); 
  