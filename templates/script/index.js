const getFileName = () => {
  try {
    fileName = new URL(url).pathname.split("/").pop();
  } catch (err) {
    console.error(err);
  }
  return fileName
};

const selectFile = document.getElementById("select-file");
if (selectFile) {
  selectFile.addEventListener("click", () => eel.select_file());
}


eel.expose(setAnchor);
function setAnchor() {
  const anchor = document.getElementById("change-page");
  anchor.href = "./pages/fetchinfo.html";
}

eel.expose(setImage);
function setImage(filePath) {
  const img = document.getElementById("qr");
  img.src = filePath;
}

eel.expose(addNote);
function addNote() {
  const note = document.getElementById("note-container");
  note.style["display"] = "block";
  note.style["textAlign"] = "center";
  note.innerText = "Fetching information...";
}

const scanButton = document.getElementById("scan-button");
if (scanButton) {
  scanButton.addEventListener("click", () => {
    eel.scan_qr();
  });
}

eel.expose(redirect);
function redirect() {
  fetch("../script/data.json")
    .then((response) => response.json())
    .then((json) => {
      const url = `../pages/${json.page}`;
      window.location.href = url;
    });
}


