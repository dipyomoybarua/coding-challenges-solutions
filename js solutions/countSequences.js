function countSequences(arr) {
    if (arr.length === 0) 
        return 0;

    let sequenceCount = 0; // Count of sequences found
    let inSequence = false; // Flag to indicate if it is in sequence

    for (let i = 1; i < arr.length; i++) { // Start from index 1 to compare with previous element
        if (arr[i] === arr[i - 1]) {
            // Current element matches the previous one
            if (!inSequence) {
                // Start of a new sequence
                sequenceCount++;
                inSequence = true;
            }
        } else {
            // Current element doesn't match the previous one
            inSequence = false;
        }
    }

    return sequenceCount;
}

console.log(countSequences([7, 7, 4, 7])); 
console.log(countSequences([7, 7, 8, 9, 7, 7])); 
console.log(countSequences([])); 
console.log(countSequences([1, 2, 3, 4, 5])); 
console.log(countSequences([1, 1, 2, 2, 3, 3])); 
console.log(countSequences([1, 1, 1, 2, 2, 3, 3, 3])); 