const API_URL = "http://localhost:8000";

async function callPower() {
    const base = document.getElementById("base").value;
    const exp = document.getElementById("exponent").value;
    try {
        const res = await fetch(`${API_URL}/power?base=${base}&exp=${exp}`);
        const data = await res.json();
        document.getElementById("powerResult").textContent = `Result: ${data.result}`;
    } catch {
        document.getElementById("powerResult").textContent = "⚠️ Error calculating power.";
    }
}

async function callFactorial() {
    const n = document.getElementById("factorialNum").value;
    try {
        const res = await fetch(`${API_URL}/factorial?n=${n}`);
        const data = await res.json();
        document.getElementById("factorialResult").textContent = `Result: ${data.result}`;
    } catch {
        document.getElementById("factorialResult").textContent = "⚠️ Error calculating factorial.";
    }
}

async function callFibonacci() {
    const n = document.getElementById("fibonacciNum").value;
    try {
        const res = await fetch(`${API_URL}/fibonacci?n=${n}`);
        const data = await res.json();
        document.getElementById("fibonacciResult").textContent = `Result: ${data.result}`;
    } catch {
        document.getElementById("fibonacciResult").textContent = "⚠️ Error calculating fibonacci.";
    }
}

async function clearPower() {
    document.getElementById("base").value = "";
    document.getElementById("exponent").value = "";
    document.getElementById("powerResult").textContent = "";
}

async function clearFactorial() {
    document.getElementById("factorialNum").value = "";
    document.getElementById("factorialResult").textContent = "";
}

async function clearFibonacci() {
    document.getElementById("fibonacciNum").value = "";
    document.getElementById("fibonacciResult").textContent = "";
}
