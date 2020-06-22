// CFPB data test
// https://cfpb.github.io/api/hmda/basics.html


// var staticUrl = 'https://ksjazzguitar.github.io/data/techs.json';
// $.getJSON(staticUrl, function(data) {
//   console.log("This is an example of a static JSON file being served by a web server.")
//   console.log(data);
// });

// Check browser support
// https://stackoverflow.com/questions/1634268/explain-the-encapsulated-anonymous-function-syntax
let supportsES6 = true;
let supportsES100 = true;

(() => {
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
})();




const cfpbUrl = "https://api.consumerfinance.gov:443/data";



fetch('http://example.com/movies.json')
  .then(response => response.json())
  .then(data => console.log(data));


// https://stackoverflow.com/questions/901115/how-can-i-get-query-string-values-in-javascript

let sampler = "https://api.consumerfinance.gov/data/hmda/slice/hmda_lar.json?%24select=agency_code%2C+agency_name%2C+applicant_ethnicity%2C+applicant_ethnicity_name%2C+applicant_income_000s&%24where=&%24group=&%24orderBy=&%24limit=10&%24offset=0&%24format=json";
let urlParams = {};



let [base, query] = sampler.split("?");

// Alternative
// var arr = sampler.split("?"), base = arr[0], query = arr[1];


(window.onpopstate = function () {
    let match,
        pl = /\+/g,  // Regex for replacing addition symbol with a space
        search = /([^&=]+)=?([^&]*)/g,
        decode = function (s) {
            return decodeURIComponent(s.replace(pl, " "));
        },
        query = window.location.search.substring(1);

    while (match = search.exec(query)) {
        if (decode(match[1]) in urlParams) {
            if (!Array.isArray(urlParams[decode(match[1])])) {
                urlParams[decode(match[1])] = [urlParams[decode(match[1])]];
            }
            urlParams[decode(match[1])].push(decode(match[2]));
        } else {
            urlParams[decode(match[1])] = decode(match[2]);
        }
    }
})();