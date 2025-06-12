document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("claimForm");
  const resultDiv = document.getElementById("result");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const claimAmount = parseFloat(document.getElementById("claimAmount").value);
    const numAccidents = parseInt(document.getElementById("numAccidents").value);

    const payload = {
      claim_amount: claimAmount,
      num_of_accidents: numAccidents,
    };

    try {
      const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const data = await response.json();

      if (response.ok) {
        resultDiv.innerHTML = `
          <p><strong>Prediction:</strong> ${data.prediction}</p>
          <p><strong>Confidence:</strong> ${(data.confidence * 100).toFixed(2)}%</p>
        `;
      } else {
        resultDiv.innerHTML = `<p class="error">Error: ${data.error}</p>`;
      }
    } catch (error) {
      resultDiv.innerHTML = `<p class="error">Something went wrong. Please try again.</p>`;
    }
  });
});
