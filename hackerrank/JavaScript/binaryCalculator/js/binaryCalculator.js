function action(e) {
    /* Older IE browsers have a srcElement property,
    but other browsers have a 'target' property; 
    Set btn to whichever exists. */
    var btn = e.target || e.srcElement;
    
    // pushes 0 to res innerHTML
    if (btn.id == "btn0") {
        document.getElementById("res").innerHTML += 0;
    }
    // pushes 1 to res innerHTML
    if (btn.id == "btn1") {
        document.getElementById("res").innerHTML += 1;
    }
    // cleares innerHTML of res
    if (btn.id == "btnClr") {
        document.getElementById("res").innerHTML = "";
    }
    
    /*
      Gets the binary values and sign to be applied
      converts the binary values to int, does the operation
      then sets the value of res innerHTML to the binary value
      of the previous operation
    */
    if (btn.id == "btnEql") {
        const re = /\+|-|\*|\//;
        let binary_values = document.getElementById("res").innerHTML.split(re);
        let sign = document.getElementById("res").innerHTML.match(re)[0];
        let integer_vals = []
        for (let i of binary_values) {
            let temp = parseInt(i, 2);
            integer_vals.push(temp);
        }
        let result = 0;
        for (let i of integer_vals) {
            if (result == 0) {
                result = i;
            }
            else {
                result = eval(result + sign + i);
            }
        }
        document.getElementById("res").innerHTML = result.toString(2);
    }
    // pushes sign + to res innerHTML
    if (btn.id == "btnSum") {
        document.getElementById("res").innerHTML += "+";
    }
    // pushes sign - to res innerHTML
    if (btn.id == "btnSub") {
        document.getElementById("res").innerHTML += "-";
    }
    // pushes sign * to res innerHTML
    if (btn.id == "btnMul") {
        document.getElementById("res").innerHTML += "*";
    }
    // pushes sign / to res innerHTML
    if (btn.id == "btnDiv") {
        document.getElementById("res").innerHTML += "/";
    }
}

/* Set each button to call action(e) when clicked */
document.getElementById('btn0').onclick = action;
document.getElementById('btn1').onclick = action;
document.getElementById('btnClr').onclick = action;
document.getElementById('btnEql').onclick = action;
document.getElementById('btnSum').onclick = action;
document.getElementById('btnSub').onclick = action;
document.getElementById('btnMul').onclick = action;
document.getElementById('btnDiv').onclick = action;