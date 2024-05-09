// Test case 1: Valid section
const text1 = "go to The Basics";
console.log(extractSection(text1)); // Output: "The Basics"

// Test case 2: Valid section with different case
const text2 = "Go To Exponents";
console.log(extractSection(text2)); // Output: "Exponents"

// Test case 3: Invalid section
const text3 = "go to Algebra";
console.log(extractSection(text3)); // Output: ""

// Test case 4: Empty text
const text4 = "";
console.log(extractSection(text4)); // Output: ""

// Test case 5: No section specified
const text5 = "go to";
console.log(extractSection(text5)); // Output: ""