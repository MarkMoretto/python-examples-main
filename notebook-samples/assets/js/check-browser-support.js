/**
 * Check ECMAScript 6 and 100 compatibility for a given browser.
 * This will allow for adjusting code, as necessary, or simply avoiding usage of 
 * new or outdated features when creating new scripts.
 * 
 * This will use an arrow / anonymous function
 * :reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions
*/


// Declare variables; Default to `true`

let supportsES6 = true;
let supportsES100 = true;

/**
 * Arrow function
 * :param verbose - Output results to console.
*/
((verbose=false) => {

    // Check ES6
    try {
        var k = new Map();
    } catch(err) {
        supportsES6 = false;
    }

    // Chek ES100    
    try {
        var k = new HashMap();
    } catch(err) {
        supportsES100 = false;
    }

    // Output results, if desired.
    if (verbose)  {
        if (supportsES6) {
            console.log(`ECMAScript 6 supported!`);
        }
        if (supportsES100) {
            console.log(`ECMAScript 100 supported!`);
        }           
    }  
})();


