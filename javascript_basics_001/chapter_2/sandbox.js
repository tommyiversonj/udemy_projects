// alert('Hello, World!');

/*let age = 25;
let year = 2019;

console.log(age, year); */

// 
/*const points = 100;
console.log(points); */

// String DataType
console.log('Hello, World');

let email = 'johnsoniverson@gmail.com';
console.log(email);

// Sting Concatenation
let firstName = 'Johnson'
let lastName = 'Sanderson';
console.log(firstName + ' ' + lastName)

//Getting characters
console.log(firstName[3])

// String length
console.log(firstName.length)

// String methods
console.log(firstName.toUpperCase());

let result = firstName.toLocaleLowerCase();
console.log(result);

let index = email.indexOf('@');
console.log(index);

// Common string methods
let email2 = 'tommyiversonj@gmail.com'
// let result2 = email2.lastIndexOf('n');
//let result2 = email2.slice(0,10);
//let result2 = email2.substring(4,10)
let result2 = email.replace('j', 'm');
console.log(result2);

// Number DataType
let radius = 10;
const pi = 3.14;

console.log(radius, pi)

//Math operators +, -, *, /, **, %
console.log(10 /2);

let result3 = radius % 3;
console.log(result3);

let result4 = pi * radius**2
console.log(result4);

// Order of operation - BIDMAS
let results = 5 * (10-3)**2;
console.log(results);

let likes = 10;
//likes = likes + 1;
//likes++;
//likes--;
//likes += 10;
//like -= 5;
//likes *= 2;
likes /= 2;
console.log(likes);
