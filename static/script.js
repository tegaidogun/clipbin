function copyURL() {
    navigator.clipboard.writeText(window.location.href).then(() => {
        alert("URL copied to clipboard");
    });
}

function copyContent() {
    const lines = document.querySelectorAll('.code-table .codetext pre');
    const text = Array.from(lines).map(el => el.textContent).join('\n');
    navigator.clipboard.writeText(text).then(() => {
        alert("Content copied to clipboard");
    });
}

// fallback plain .txt download on clicking #download-btn
window.addEventListener("DOMContentLoaded", () => {
    const dlBtn = document.getElementById("download-btn");
    dlBtn.addEventListener("click", () => {
        const content = Array.from(document.querySelectorAll(".codetext pre"))
            .map(el => el.textContent).join("\n");
        const blob = new Blob([content], { type: "text/plain" });
        const link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = document.title.replace(" - PasteDump", "") + ".txt";
        link.click();
    });
});
