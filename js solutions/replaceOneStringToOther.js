function replaceSubstring(originalString, oldSubstring, newSubstring) {
    // Step 2: Use `replaceAll` Method
    const resultString = originalString.replaceAll(oldSubstring, newSubstring);
    
    // Step 3: Return the Result
    return resultString;
  }
  
  // Example usage
  const originalString = "Marry";
  const oldSubstring = "Marry";
  const newSubstring = "Army";
  
  const replacedString = replaceSubstring(originalString, oldSubstring, newSubstring);
  console.log(replacedString);
  