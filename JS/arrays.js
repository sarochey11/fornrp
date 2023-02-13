let secretMessage = ['Learning', 'is', 'not', 'about', 'what', 'you', 'get', 'easily', 'the', 'first', 'time,', 'it', 'is', 'about', 'what', 'you', 'can', 'figure', 'out.', '-2015,', 'Chris', 'Pine,', 'Learn', 'JavaScript'];

//console.log(secretMessage.length)

secretMessage.pop(); //removes last element

//console.log(secretMessage.length)

secretMessage.push('to', 'Program'); //adds elements to the end of the array

//console.log(secretMessage)

secretMessage[7] = 'right' //replaces element at index 7

//console.log(secretMessage)

secretMessage.shift(); //removes first element

//console.log(secretMessage)

secretMessage.unshift('Programming'); //adds element to the beginning of the array

//console.log(secretMessage)

secretMessage.splice(6, 5, 'know'); //removes 5 elements starting at index 6 and adds 'know' at index 6

console.log(secretMessage.join(' ')); //joins the elements of the array into a string