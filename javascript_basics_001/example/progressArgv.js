// console.log("Command line arguments:", process.argv);
// console.log("The process is:", process.pid);
// console.log("version of Nodjs:", process.versions.node);
const [, , firstName, lastName ] = process.argv;
console.log("Your name is ${firstname} ${lastName}");
