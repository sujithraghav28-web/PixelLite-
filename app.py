
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PixelLite - Image Compressor</title>

<style>
:root {
    --blue: #356df3;
    --dark: #101827;
    --bg: #f4f7fb;
    --text: #172033;
    --muted: #687386;
}

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: var(--bg);
    color: var(--text);
}

header {
    background: var(--dark);
    color: white;
    padding: 22px;
}

.nav {
    max-width: 1000px;
    margin: auto;
    font-size: 23px;
    font-weight: bold;
}

.nav span {
    color: #7fa4ff;
}

main {
    max-width: 850px;
    margin: 45px auto;
    padding: 20px;
}

.intro {
    text-align: center;
    margin-bottom: 30px;
}

.intro h1 {
    font-size: 42px;
    margin-bottom: 12px;
}

.intro p {
    color: var(--muted);
}

.panel {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 35px rgba(0,0,0,.06);
}

.dropzone {
    border: 2px dashed #b9c8e4;
    border-radius: 15px;
    padding: 35px 15px;
    text-align: center;
    background: #f8faff;
}

.dropzone.drag {
    background: #e8efff;
    border-color: var(--blue);
}

.dropzone h2 {
    font-size: 20px;
}

.dropzone p {
    color: var(--muted);
}

button, .file-label {
    display: inline-block;
    background: var(--blue);
    color: white;
    border: none;
    border-radius: 9px;
    padding: 12px 20px;
    font-size: 15px;
    font-weight: bold;
    cursor: pointer;
}

button:hover, .file-label:hover {
    background: #2457d4;
}

button:disabled {
    opacity: .5;
    cursor: not-allowed;
}

input[type="file"] {
    display: none;
}

.settings {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 25px;
}

.field label {
    display: block;
    font-weight: bold;
    margin-bottom: 10px;
}

input[type="number"], select {
    width: 100%;
    padding: 12px;
    border: 1px solid #d7deea;
    border-radius: 9px;
    font-size: 15px;
    background: white;
}

.hint {
    font-size: 13px;
    color: var(--muted);
    margin-top: 7px;
}

.actions {
    display: flex;
    gap: 10px;
    margin-top: 25px;
    flex-wrap: wrap;
}

.secondary {
    background: #edf1f7;
    color: var(--text);
}

.status {
    margin-top: 18px;
    color: var(--muted);
}

.error {
    color: #c33d4c;
}

.success {
    color: #16865b;
}

.results {
    display: none;
    margin-top: 25px;
    border-top: 1px solid #e5eaf1;
    padding-top: 22px;
}

.results.show {
    display: block;
}

.stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}

.stat {
    background: #f6f8fc;
    padding: 15px;
    border-radius: 10px;
}

.stat span {
    display: block;
    color: var(--muted);
    font-size: 13px;
    margin-bottom: 7px;
}

.preview {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
    margin-top: 20px;
}

.preview figure {
    margin: 0;
    border: 1px solid #e5eaf1;
    border-radius: 10px;
    padding: 10px;
}

.preview img {
    width: 100%;
    height: 180px;
    object-fit: contain;
    background: #f5f7fa;
}

.preview figcaption {
    font-size: 13px;
    margin-bottom: 10px;
}

.download {
    display: inline-block;
    background: #16865b;
    color: white;
    padding: 12px 18px;
    border-radius: 9px;
    text-decoration: none;
    font-weight: bold;
    margin-bottom: 15px;
}

footer {
    text-align: center;
    color: var(--muted);
    padding: 20px;
    font-size: 13px;
}

@media(max-width: 600px) {
    .intro h1 {
        font-size: 32px;
    }

    .settings, .preview, .stats {
        grid-template-columns: 1fr;
    }

    .panel {
        padding: 18px;
    }
}
</style>
</head>

<body>

<header>
    <div class="nav">
        Pixel<span>Lite</span>
    </div>
</header>

<main>

<section class="intro">
    <h1>Smaller images.<br>Same big moments.</h1>
    <p>Compress your images quickly, freely and privately.</p>
</section>

<section class="panel">

<div class="dropzone" id="dropzone">
    <h2>Choose an image to compress</h2>
    <p>JPG, PNG and WebP supported</p>

    <label class="file-label" for="fileInput">
        Choose Image
    </label>

    <input
        type="file"
        id="fileInput"
        accept="image/jpeg,image/png,image/webp"
    >
</div>

<div class="settings">

    <div class="field">
        <label for="targetSize">Target Size (KB)</label>
        <input
            type="number"
            id="targetSize"
            value="200"
            min="10"
            max="10000"
        >
        <div class="hint">Example: 200 KB</div>
    </div>

    <div class="field">
        <label for="format">Output Format</label>
        <select id="format">
            <option value="image/jpeg">JPG</option>
            <option value="image/webp">WebP</option>
        </select>
        <div class="hint">PNG transparency is not preserved.</div>
    </div>

</div>

<div class="actions">
    <button id="compressBtn" disabled>
        Compress Image
    </button>

    <button id="resetBtn" class="secondary">
        Reset
    </button>
</div>

<div id="status" class="status">
    Choose an image to begin.
</div>

<section class="results" id="results">

    <h2>Compression Result</h2>

    <a
        id="downloadBtn"
        class="download"
        href="#"
        download="pixellite-compressed.jpg"
    >
        Download Image
    </a>

    <div class="stats">

        <div class="stat">
            <span>Original Size</span>
            <strong id="originalSize">—</strong>
        </div>

        <div class="stat">
            <span>Compressed Size</span>
            <strong id="compressedSize">—</strong>
        </div>

        <div class="stat">
            <span>Space Saved</span>
            <strong id="saved">—</strong>
        </div>

    </div>

    <div class="preview">

        <figure>
            <figcaption>Original Image</figcaption>
            <img id="originalPreview" alt="Original preview">
        </figure>

        <figure>
            <figcaption>Compressed Image</figcaption>
            <img id="compressedPreview" alt="Compressed preview">
        </figure>

    </div>

    <p class="hint" id="resultNote"></p>

</section>

</section>
</main>

<footer>
    PixelLite — Your images stay on your device.
</footer>

<script>

const fileInput = document.getElementById("fileInput");
const dropzone = document.getElementById("dropzone");
const compressBtn = document.getElementById("compressBtn");
const resetBtn = document.getElementById("resetBtn");
const statusEl = document.getElementById("status");
const results = document.getElementById("results");

let selectedFile = null;
let originalURL = null;
let compressedURL = null;


// Format file size
function formatBytes(bytes) {
    if (bytes < 1024) return bytes + " B";
    return (bytes / 1024).toFixed(1) + " KB";
}


// Display messages
function showStatus(message, type = "") {
    statusEl.textContent = message;
    statusEl.className = "status " + type;
}


// Clear temporary image URLs
function clearURLs() {
    if (originalURL) URL.revokeObjectURL(originalURL);
    if (compressedURL) URL.revokeObjectURL(compressedURL);

    originalURL = null;
    compressedURL = null;
}


// Load selected image
function loadFile(file) {

    if (!file) return;

    const allowed = [
        "image/jpeg",
        "image/png",
        "image/webp"
    ];

    if (!allowed.includes(file.type)) {
        showStatus("Please select JPG, PNG or WebP.", "error");
        return;
    }

    clearURLs();

    selectedFile = file;
    originalURL = URL.createObjectURL(file);

    document.getElementById("originalPreview").src = originalURL;

    document.getElementById("originalSize").textContent =
        formatBytes(file.size);

    results.classList.remove("show");

    compressBtn.disabled = false;

    showStatus(
        "Selected: " + file.name +
        " (" + formatBytes(file.size) + ")"
    );
}


// File picker
fileInput.addEventListener("change", function() {
    loadFile(fileInput.files[0]);
});


// Drag and drop
["dragenter", "dragover"].forEach(eventName => {
    dropzone.addEventListener(eventName, event => {
        event.preventDefault();
        dropzone.classList.add("drag");
    });
});

["dragleave", "drop"].forEach(eventName => {
    dropzone.addEventListener(eventName, event => {
        event.preventDefault();
        dropzone.classList.remove("drag");
    });
});

dropzone.addEventListener("drop", event => {
    loadFile(event.dataTransfer.files[0]);
});


// Convert canvas to image file
function canvasBlob(canvas, format, quality) {
    return new Promise(resolve => {
        canvas.toBlob(resolve, format, quality);
    });
}


// Main compression function
async function compressImage() {

    if (!selectedFile) return;

    const targetKB = Number(
        document.getElementById("targetSize").value
    );

    if (!Number.isFinite(targetKB) ||
        targetKB < 10 || targetKB > 10000) {

        showStatus("Enter a target between 10 and 10000 KB.", "error");
        return;
    }

    compressBtn.disabled = true;

    showStatus("Compressing image...");

    results.classList.remove("show");

    let bitmap;

    try {

        bitmap = await createImageBitmap(selectedFile);

        const canvas = document.createElement("canvas");
        const context = canvas.getContext("2d", {
            alpha: false
        });

        const format = document.getElementById("format").value;
        const targetBytes = targetKB * 1024;

        let quality = 0.92;
        let scale = 1;
        let blob = null;
        let attempts = 0;

        while (attempts < 50) {

            canvas.width = Math.max(
                1,
                Math.round(bitmap.width * scale)
            );

            canvas.height = Math.max(
                1,
                Math.round(bitmap.height * scale)
            );

            context.clearRect(
                0, 0, canvas.width, canvas.height
            );

            context.drawImage(
                bitmap,
                0, 0,
                canvas.width,
                canvas.height
            );

            blob = await canvasBlob(
                canvas,
                format,
                quality
            );

            if (!blob) {
                throw new Error("Image encoding failed.");
            }

            if (blob.size <= targetBytes) {
                break;
            }

            if (quality > 0.25) {
                quality = Math.max(0.25, quality - 0.08);
            } else {
                scale *= 0.85;
                quality = 0.88;
            }

            attempts++;
        }

        if (!blob || blob.size > targetBytes) {
            throw new Error(
                "Could not reach target size. Try a larger target."
            );
        }

        if (compressedURL) {
            URL.revokeObjectURL(compressedURL);
        }

        compressedURL = URL.createObjectURL(blob);

        const extension =
            format === "image/webp" ? "webp" : "jpg";

        const downloadBtn =
            document.getElementById("downloadBtn");

        downloadBtn.href = compressedURL;

        downloadBtn.download =
            "pixellite-compressed." + extension;

        document.getElementById("compressedPreview").src =
            compressedURL;

        document.getElementById("compressedSize").textContent =
            formatBytes(blob.size);

        const saved =
            Math.max(0, (1 - blob.size / selectedFile.size) * 100);

        document.getElementById("saved").textContent =
            saved.toFixed(1) + "%";

        document.getElementById("resultNote").textContent =
            "Output dimensions: " +
            canvas.width + " × " + canvas.height;

        results.classList.add("show");

        showStatus(
            "Compression completed successfully!",
            "success"
        );

    } catch (error) {

        showStatus(error.message, "error");

    } finally {

        if (bitmap) bitmap.close();

        compressBtn.disabled = !selectedFile;
    }
}


// Compress button
compressBtn.addEventListener(
    "click",
    compressImage
);


// Reset button
resetBtn.addEventListener("click", function() {

    clearURLs();

    selectedFile = null;
    fileInput.value = "";

    compressBtn.disabled = true;

    results.classList.remove("show");

    showStatus("Choose an image to begin.");
});

</script>

</body>
</html>
