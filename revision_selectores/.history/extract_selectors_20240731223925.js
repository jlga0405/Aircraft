const esprima = require('esprima');
const fs = require('fs');

// Define el nombre del archivo de scraping
const vendor_scrap = 'https://shop.boeing.com/aviation-supply/';  // Reemplaza con el nombre del archivo de scraping que desees analizar

// Lee el script de scraping en JavaScript
const script = fs.readFileSync(vendor_scrap, 'utf8');

// Agrega un registro para verificar que el script se ha leído correctamente
console.log(`Contenido del script ${vendor_scrap}:\n${script}`);

// Analiza el script y extrae los selectores
const parsed = esprima.parseScript(script);

// Agrega un registro para verificar el AST generado
console.log(`AST generado:\n${JSON.stringify(parsed, null, 2)}`);

const selectors = {};

// Función para recorrer el AST y encontrar selectores
const traverse = (node) => {
    if (node.type === 'CallExpression') {
        if (node.callee.property) {
            if (node.callee.property.name === 'querySelector' || node.callee.property.name === 'querySelectorAll') {
                const selector = node.arguments[0].value;
                if (selector) {
                    selectors[selector] = selector;
                    // Agrega un registro para cada selector encontrado
                    console.log(`Selector encontrado: ${selector}`);
                }
            }
            // Añade lógica para capturar selectores en $ y $eval
            if (['$', '$$', '$eval', '$$eval'].includes(node.callee.property.name)) {
                const selectorNode = node.arguments[0];
                if (selectorNode && selectorNode.type === 'Literal') {
                    const selector = selectorNode.value;
                    if (selector) {
                        selectors[selector] = selector;
                        // Agrega un registro para cada selector encontrado
                        console.log(`Selector encontrado: ${selector}`);
                    }
                }
            }
        }
    }

    for (const key in node) {
        if (node[key] && typeof node[key] === 'object') {
            traverse(node[key]);
        }
    }
};

// Recorre el AST del script de scraping
traverse(parsed);

// Guarda los selectores en un archivo JSON
fs.writeFileSync('selectors.json', JSON.stringify({ selectors }, null, 2));

// Agrega un registro para confirmar que el proceso ha terminado
console.log('Selectores extraídos y guardados en selectors.json');
