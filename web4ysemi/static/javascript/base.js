
// 
let fin = document.getElementById("reportType-financials");
let bs = document.getElementById("reportType-bs");
let pl = document.getElementById("reportType-pl");
let cf = document.getElementById("reportType-cf");
let reportType = document.getElementById("reportType");

let l3y = document.getElementById("last3years");
let lq = document.getElementById("lastQuarter");
let period = document.getElementById("period");

let search = document.getElementById("search");

let done = document.getElementById("done");

let init = document.getElementById("init");


// able / disable change color
function buttonColorChange(documentObj) {
    if (documentObj.disabled) {
        documentObj.style.color = "gray";
    } else {
        documentObj.style.color = "black"
    }
}

buttonColorChange(reportType);
buttonColorChange(period);
buttonColorChange(search);
buttonColorChange(done);

// if (reportType.disabled) {
//     reportType.style.color = "gray";
// } else {
//     reportType.style.color = "black";
// }

// if (period.disabled) {
//     period.style.color = "gray";
// } else {
//     period.style.color = "black";
// }

// reportType checkbox validation
function reportTypeValidation(event) {

    if (!(fin.checked || bs.checked || pl.checked || cf.checked)) {

        window.alert("Please select at least one of report type.");
        event.stopPropagation();
        event.preventDefault();
    }
}

reportType.addEventListener("click", reportTypeValidation);


// period validation
function periodValidation(event) {

    if (!(l3y.checked || lq.checked)) {

        window.alert("Please select at least one of period.");
        event.stopPropagation();
        event.preventDefault();
    }
}

period.addEventListener("click", periodValidation);


// done
function doneConfirm(event) {
    let result = window.confirm("Do you really want to submit input?");

    if (!result) {
        event.stopPropagation();
        event.preventDefault();
    }
}

done.addEventListener("click", doneConfirm);


// init
function initConfirm(event) {
    let result = window.confirm("Do you really want to initialize the input?");

    if (!result) {
        event.stopPropagation();
        event.preventDefault();
    }
}

init.addEventListener("click", initConfirm);