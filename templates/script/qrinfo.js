const getDomain = (url) => {
  const domain = url.match(/(?:http(?:s)?:\/\/)?(?:www\.)?([a-zA-Z0-9\-\.]+)/);
  return domain[1];
};

window.addEventListener("load", () => {
  fetch("../script/data.json")
    .then((response) => response.json())
    .then((json) => {
      const url = json.url;
      const info = json.data;

      const anchor = document.getElementById("site-name");
      anchor.href = url;
      anchor.innerText = getDomain(url);

      const element = document.getElementById("data");
      element.innerText = info;

      if (json.addedBy == "USER") {
        const noteContainer = document.getElementById("note-container");
        noteContainer.innerHTML = `
          <div class="button-container">
          <div id="edit" class="div-button">Edit</div>
          </div>`;

        const edit = document.getElementById("edit");
        edit.addEventListener("click", () => {
          edit.style["display"] = "none";

          const p = document.getElementById("data");
          p.innerHTML = '<textarea name="text" id="input"></textarea>';

          const input = document.getElementById("input");
          input.value = json.data;

          noteContainer.innerHTML = `<div id="note"></div>
          <div class="button-container">
          <div id="add-to-database-after-edit" class="div-button">
          Add To Database
          </div>
          </div>`;

          const addToDatabase = document.getElementById(
            "add-to-database-after-edit"
          );
          addToDatabase.addEventListener("click", () => {
            eel.add_info(input.value);

            p.innerText = input.value;

            note.innerText = "Updated information successfully";
            note.style["display"] = "inline-block";

            addToDatabase.style["display"] = "none";
          });
        });
      }

      if (json.infoFrom === "AI") {
        const noteContainer = document.getElementById("note-container");
        noteContainer.innerHTML = `<div id="note">
          The above information is created by an AI and is not stored in
          database.<br />If you believe that the above information is correct you
          can add it to the database.
          </div>
          <div class="button-container">
          <div id="edit" class="div-button">Edit</div>
          <div id="add-to-database-before-edit" class="div-button">Add to Database</div>
          </div>`;

        const addToDatabase = document.getElementById(
          "add-to-database-before-edit"
        );
        if (addToDatabase) {
          addToDatabase.addEventListener("click", () => {
            eel.add_info(json.data);

            const note = document.getElementById("note");
            note.innerText = "Information added to database";
            note.style["display"] = "inline-block";

            addToDatabase.style["display"] = "none";

            const edit = document.getElementById("edit");
            edit.style["display"] = "none";
          });
        }

        const edit = document.getElementById("edit");
        edit.addEventListener("click", () => {
          edit.style["display"] = "none";

          const note = document.getElementById("note");
          note.style["display"] = "none";

          const p = document.getElementById("data");
          p.innerHTML = '<textarea name="text" id="input"></textarea>';

          const input = document.getElementById("input");
          input.value = json.data;

          addToDatabase.id = "add-to-database-after-edit";
          addToDatabase.addEventListener("click", () => {
            eel.add_info(input.value);

            p.innerText = input.value;

            note.innerText = "Information added to database";
            note.style["display"] = "inline-block";

            addToDatabase.style["display"] = "none";
          });
        });
      }
    });
});
