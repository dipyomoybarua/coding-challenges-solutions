let L1 = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5, 6, 4, 5, 6];

// Step 2: Use a Set to Remove Duplicates
let uniqueSet = new Set(L1);


uniqueSet.forEach(element => {
    console.log('Unique elements using Set:', element);
});


