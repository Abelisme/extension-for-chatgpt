const form = document.getElementById("form");
const input = document.getElementById("input");
const result = document.getElementById("result");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const message = input.value;
  const url = `http://127.0.0.1:5000/api/data/`;

  const payload = { message };

  fetch(url, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then((response) => response.json())
    .then((data) => {
      result.innerHTML = `The responses is ${data}.`;
    })
    .catch((error) => {
      result.innerHTML = "An error occurred while getting the chatgpt-response data.";
      console.error(error);
    });

});
