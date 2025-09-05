
var sum = 0;
var fact = 1;
for (let i = 0; i < 10; i++) {
if (i % 2 !== 0) {
    console.log(i + "odd numbers from one to ten");
}
}
for ( i<100 ; i >= 0 ; i--) {
if (i % 3 === 0) {
    console.log(i + "decreasing-multiple of 3");
}
}
for (let i = 4; i > -3.5; i -= 1.5) {
console.log(i);
}
for (let i = 0; i < 100; i++) {
sum += i;
console.log(sum + "sum");
}
for (let i = 1; i <= 12; i++) {
  fact *= i;
console.log(fact + "factorial");
}
