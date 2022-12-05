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


