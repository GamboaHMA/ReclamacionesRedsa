function toggleFiles(id) {
    const files = document.getElementById(id);
    if (files.style.display === "none" || files.style.display === "") {
        files.style.display = "block";
    } else {
        files.style.display = "none";
    }
}