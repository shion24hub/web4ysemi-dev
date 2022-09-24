
// reportType checkbox validation
let fin = document.getElementById("reportType-financials");
let bs = document.getElementById("reportType-bs");
let pl = document.getElementById("reportType-pl");
let cf = document.getElementById("reportType-cf");

function reportTypeValidation(event) {

    if (!(fin.checked || bs.checked || pl.checked || cf.checked)) {

        window.alert("Please select at least one of report type.");
        event.stopPropagation();
        event.preventDefault();
    }
}

let reportType = document.getElementById("reportType");
reportType.addEventListener("click", reportTypeValidation);


// period validation
let l3y = document.getElementById("last3years");
let lq = document.getElementById("lastQuarter");

function periodValidation(event) {

    if (!(l3y.checked || lq.checked)) {

        window.alert("Please select at least one of period.");
        event.stopPropagation();
        event.preventDefault();
    }
}

let period = document.getElementById("period");
period.addEventListener("click", periodValidation);


// done
function doneConfirm(event) {
    let result = window.confirm("Do you really want to submit input?");

    if (!result) {
        event.stopPropagation();
        event.preventDefault();
    }
}

let done = document.getElementById("done");
done.addEventListener("click", doneConfirm);


// init
function initConfirm(event) {
    let result = window.confirm("Do you really want to initialize the input?");

    if (!result) {
        event.stopPropagation();
        event.preventDefault();
    }
}

let form = document.getElementById("init");
form.addEventListener("click", initConfirm);