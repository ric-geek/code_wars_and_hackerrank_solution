function highAndLow(numbers){
  
    let inputSplitted = numbers.split(" ");
  
    let arrayNumber = [];
  
    for (let index = 0; index < inputSplitted.length; index++) {
      
        arrayNumber.push(Number(inputSplitted[index]));
  
    }
    
    return Math.max.apply(0, arrayNumber) + " " + Math.min.apply(0, arrayNumber);
    
  }