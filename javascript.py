function add(n1, n2) {
    return n1 + n2;
}

function subtract(n1, n2){
    return n1 - n2;
}

function divide(n1, n2){
    return n1 / n2;
}

function multiply(n1, n2){
    return n1 * n2;
}

const operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
};

function calculator() {
    let shouldAccumulate = true;
    let num1 = parseFloat(prompt("What is the first number?: "));

    while (should_accumulate) {
         // Display available operations
        let operationsList = "";
        for (let symbol in operations) {
            operationsList += '${symbol} ';
        }
        alert(`Available operations: ${operationsList.trim()}`);

         // Get user input for operation and the next number
        const operation_symbol = prompt("Pick an operation: ");
        const num2 = parseFloat(prompt("What is the next number?: "));
        const answer = operations[operation_symbol](num1, num2);

         // Display the result
        alert(`${num1} ${operationSymbol} ${num2} = ${answer}`);

        

         // Ask if the user wants to continue with the current result or start over
        const choice = prompt("Type 'yes' to continue calculating with ${answer}, or type 'no' to start again: ").toLowerCase()

        if (choice === 'yes'){
            num1 = answer;  // Update num1 to the current answer
        } else {
            should_accumulate = false;
            console.clear();
            calculator();
        }
};

calculator();
