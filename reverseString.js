function reverseString(str) {
    // Convert string to array
    let arr = [];
    for (let i = 0; i < str.length; i++) {
      arr[i] = str[i];
    }
  
    // Reverse the array
    let start = 0;
    let end = arr.length - 1;
    while (start < end) {
      let temp = arr[start];
      arr[start] = arr[end];
      arr[end] = temp;
  
      start++;
      end--;
    }
  
    // Convert array back to string
    let reversedStr = "";
    for (let i = 0; i < arr.length; i++) {
      reversedStr += arr[i];
    }
  
    return reversedStr;
  }
  
  let stringToReverse = "Hello, World!";
  console.log(reverseString(stringToReverse)); 
  