function highAndLow(numbers){
    var arr = numbers.split(' ');
    var max = Math.max.apply(null, arr);
    var min = Math.min.apply(null, arr);
    return max + ' ' + min;
};