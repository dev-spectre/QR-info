window.addEventListener("load", () => {
  fetch("../script/data.json")
    .then((response) => response.json())
    .then((json) => {
      const element = document.getElementById("data");
      element.innerText = json.data;
    });
});
