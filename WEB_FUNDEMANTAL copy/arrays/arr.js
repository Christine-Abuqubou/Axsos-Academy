function alwaysHungry(arr){
    let count = 0;
    var string = ""
    for(let i = 0; i < arr.length; i++){
        if(arr[i] === "food"){
            string+= "yummy, ";
            count++;
        }
    }

    if(count === 0){console.log("I'm hungry")}
    else
        console.log(string);
}

function highPass(arr, cutoff){
    let newArr = [];
    for(let i = 0; i < arr.length; i++){
        if(arr[i] > cutoff){
            newArr.push(arr[i]);
        }
    }

    return newArr;
}

function betterThanAverage(arr){
    let count =0;
    let avg = 0;
    let sum = 0;
    for(let i = 0; i < arr.length; i++){
        sum += arr[i];
    }
    avg = sum / arr.length;
    for(let i = 0; i < arr.length; i++){
        if(arr[i] > avg) count++;
    }

    return count;
}


function reverse(arr){
    let newArr = [];
    for(let i = arr.length-1; i >= arr.length; i++){
        newArr.push(arr[i]);
    }

    return newArr;
}

function fibonacciArray(n){
    var arr = [0, 1];
    let sum = 0;
    let num = 2;
    for(let i = 0 ; i < arr.length && num < n; i++){
        sum += arr[i]+(arr[i+1]);
        arr.push(sum);
        sum = 0;
        num++;
    }

    return arr;
}


console.log("Always Hungry")

alwaysHungry([3.14, "food", "pie", true, "food"]);
alwaysHungry([4, 1, 5, 7, 2]);

console.log("High Pass Filter")

var result1 = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result1);

console.log("Better Than Avarage")

var result2= betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result2);

console.log("Array Reverse")

var result3 = reverse(["a", "b", "c", "d", "e"]);
console.log(result3);

console.log("Fibonacci Array")

var result4 = fibonacciArray(10);
console.log(result4);