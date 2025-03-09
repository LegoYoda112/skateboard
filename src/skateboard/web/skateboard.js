

document.addEventListener("DOMContentLoaded", function () {
    
});

eel.expose(addHeader);
function addHeader(header_text, node_id, options) {
    const template = document.getElementById("headerTemplate");
    const newHeader = template.content.cloneNode(true);

    newHeader.querySelector("h2").textContent = header_text;
    newHeader.querySelector("div").id = node_id;

    document.getElementById("mainContainer").appendChild(newHeader);
}

eel.expose(addParagraph);
function addParagraph(paragraph_text, node_id, options) {
    const template = document.getElementById("paragraphTemplate");
    const newParagraph = template.content.cloneNode(true);

    newParagraph.querySelector("p").textContent = paragraph_text;
    newParagraph.querySelector("div").id = node_id;

    document.getElementById("mainContainer").appendChild(newParagraph);
}