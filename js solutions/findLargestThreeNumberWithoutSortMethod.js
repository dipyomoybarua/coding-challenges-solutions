function findLargestThreeNumbers(arr) {
    let first = Number.NEGATIVE_INFINITY;
    let second = Number.NEGATIVE_INFINITY;
    let third = Number.NEGATIVE_INFINITY;

    for (let num of arr) {
        if (num > first) {
            third = second;
            second = first;
            first = num;
        } else if (num > second) {
            third = second;
            second = num;
        } else if (num > third) {
            third = num;
        }
    }

    return [first, second, third];
}

// Example usage
const numbers = [10, 5, 20, 30, 15];
const largestThree = findLargestThreeNumbers(numbers);
console.log("Largest three numbers:", largestThree);
