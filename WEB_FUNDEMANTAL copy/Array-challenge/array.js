function alwaysHungry(arr) {
  let foundFood = false;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "food") {
      console.log("yummy!");
      foundFood = true;
    }
    if ("!foundFood") {
      console.log("im hungry!");
    }
  }
}
alwaysHungry([3.14,"food","pie","true","food"])
alwaysHungry("[4,1,5,7,21]")
    



// ass2

function betterThanAverage(arr){
    let sum =0;
    let count=0;
    for(let i=0;i<arr.lenght;i++){
        sum=sum+arr[i];
    }
       let avg=sum/arr.lenght;
       for(let i=0;i<arr.lenght;i++){
        if(arr[i]>average){
            count++
        }
       }
       return count;
}
var result=betterThanAverage([6,8,3,10,-2,5,9])
console.log(result);

// ass3

function highPass(arr,cutoff){
return arr.filter(num=>num>cutoff);
}
var result=highPass([6,8,3,10,2,5,9]);
    console.log(result);

// ass4
function reverse(arr){
    return arr.reverse();
}
var result=reverse(["a","b","c","d","e"]);
console.log(result);

//ass5

function fibonnacciArray(n){
    let fibArr=[0,1];
    for(let i=2;i<n;i++){
        fibArr[i]=fibArr[i-1]+fibArr[i-2];
    }
}return fibArr;
console.log(fibonacciArray(10));