

document.addEventListener("DOMContentLoaded", function () {

});

eel.expose(updateHeader);
function updateHeader(header_text, node_id, options) {
    const {node: node, is_template: is_template} = findTemplateOrCreate("headerTemplate", node_id);

    node.querySelector("h2").textContent = header_text;

    if(is_template)
        document.getElementById("mainContainer").appendChild(node);
}

eel.expose(updateParagraph);
function updateParagraph(paragraph_text, node_id, options) {
    const {node: node, is_template: is_template} = findTemplateOrCreate("paragraphTemplate", node_id);

    node.querySelector("p").textContent = paragraph_text;

    if(is_template)
        document.getElementById("mainContainer").appendChild(node);
}

function findTemplateOrCreate(template_id, node_id){
    
    // Check if element exists
    if(node_id != "null" && document.getElementById(node_id) ){
        console.log("updating existing element");
        // Return existing element
        const existingNode = document.getElementById(node_id)
        return {node: existingNode, is_template: false};
    } else {
        console.log("adding new element");
        // otherwise, make new element
        const template = document.getElementById(template_id);
        const newNode = template.content.cloneNode(true);
        newNode.querySelector('div').id = node_id;
        return {node: newNode, is_template: true}
    }
}