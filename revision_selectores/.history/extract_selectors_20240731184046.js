const esprima = require('esprima');
const fs = require('fs');

// Define el nombre del archivo de scraping
const vendor_scrap = 'index.js';  // Reemplaza con el nombre del archivo de scraping que desees analizar

// Lee el script de scraping en JavaScript
const script = fs.readFileSync(vendor_scrap, 'utf8');

// Analiza el script y extrae los selectores
const parsed = esprima.parseScript(script);
const selectors = {};

// Función para recorrer el AST y encontrar selectores
const traverse = (node) => {
    if (node.type === 'CallExpression' && node.callee.property && node.callee.property.name === 'querySelector') {
        const selector = node.arguments[0].value;
        if (selector) {
            selectors[selector] = selector;
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

console.log('Selectores extraídos y guardados en selectors.json');
