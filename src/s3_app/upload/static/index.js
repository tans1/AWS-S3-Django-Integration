const uploadFile = (event) => {
  event.preventDefault();
  var fileInput = document.getElementById("inputGroupFile");
  if (fileInput.files.length === 0) {
    alert("Please select a file.");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);
  const csrfToken = document.querySelector(
    "input[name=csrfmiddlewaretoken]"
  ).value;
  formData.append("csrfmiddlewaretoken", csrfToken);
  fetch("/file/upload/", {
    method: "POST",
    headers: {
      "X-CSRFToken": csrfToken
    },
    body: formData
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Upload failed.");
      }
      window.location.reload();
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

const downloadBLob = (url) => {
  const link = document.createElement("a");
  link.href = url;
  document.body.appendChild(link);
  link.download = "download";
  link.click();
};

const downloadFile = (fileName) => {
  const csrfToken = document.querySelector(
    "input[name=csrfmiddlewaretoken]"
  ).value;
  fetch("/file/download/", {
    method: "POST",
    headers: {
      "X-CSRFToken": csrfToken,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ fileName: fileName })
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data.presigned_url);
      downloadBLob(data.presigned_url);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

const deleteFile = (fileName) => {
  const csrfToken = document.querySelector(
    "input[name=csrfmiddlewaretoken]"
  ).value;
  fetch("/file/delete/", {
    method: "POST",
    headers: {
      "X-CSRFToken": csrfToken,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ fileName: fileName })
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Delete failed.");
      }
      window.location.reload();
    })
    .catch((error) => {
      console.error("Error:", error);
    });
};

// document.getElementById('uploadForm').addEventListener('submit', function(event) {
//     event.preventDefault();
//     uploadFile(event);
// });
