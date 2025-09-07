function pizzaOven(crustType,souseType,cheeseType,topping){
    let pizza={};
    pizza.crustType=crustType;
    pizza.souseType=souseType;
    pizza.cheeseType=cheeseType;
    pizza.topping=topping;
    return pizza;}

let p1=pizzaOven("hand tosted","marinara",["mozzeralla"],["pepperoni","sausage"]);
console.log("pizza1",p1);

let p2=pizzaOven("handtossed","marinara",["mozzarella","feta"],["mashroom","olives","onions"]);
console.log("pizza2",p2);

let p3=pizzaOven("thinCrust","pesto",["parmezan","mozzarella"],["chicken","tomato","basil"]);
console.log("pizza3",p3);
