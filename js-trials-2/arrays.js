"use strict";


// 1. printIndices
function printIndices(items) {
  // Replace this with your code
  for (const i in items){
  	console.log(items[i], i);
  }
}


// 2. everyOtherItem
function everyOtherItem(items) {
  // Replace this with your code
  let result = [];
  for (let i = 0; i < items.length ; i++ ){
  	if (i % 2 == 0){
  		result.push(items[i]);
  	}
  }
  
  console.log(result);
}


// 3. smallestNItems
function smallestNItems(items, n) {
  // Replace this with your code
  let sortedItems = items.sort((a, b) => a - b);
  sorted_n_items = sortedItems.slice(0, n);
  sorted_n_items.reverse;

  console.log(sorted_n_items)
  return(sorted_n_items);
}