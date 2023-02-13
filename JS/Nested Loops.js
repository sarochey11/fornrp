// Write your code below

let bobsFollowers = ['James', 'Alex', 'John', 'Tom'];
let tinasFollowers = ['Oliver', 'James', 'Sean', 'Tom'];
let mutualFollowers = [];

for (let i = 0; i < bobsFollowers.length; i++){
    for (let j = 0; j < tinasFollowers.length; j++){
        if (bobsFollowers[i] === tinasFollowers[j]) {
            mutualFollowers.push(bobsFollowers[i]);
        }
    }
};