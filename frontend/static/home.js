
const facturacion_table = document.getElementById('facturacion_table');


function create_table(data, table){

    table.innerHTML = "";
  
    for (let data_ of data) {
  
      let row = Object.values(data_);
      let string_row = "";
  
      row.forEach(function(val) {
        string_row += `<td>${val}</td>`;
      });
  
      string_row += "</tr>";
      table.innerHTML += string_row;
  
    }
  }
  


async function get_data() {
    const apiUrl = 'http://localhost:8000/api/data';

    response = await fetch(apiUrl, {
        method: "GET",
        headers: {
            'Content-Type': 'application/json',
        }
    });

    const data = await response.json();
    console.log(data);

    const tableNames = Object.keys(data[0]);

    tableHead.innerHTML = "";
    for (let name of tableNames) {
      tableHead.innerHTML += `<th> <h4 class="data"> ${name} </h4> </th>`;
    }
  
    create_table(data, facturacion_table);
  
}


document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('button_query');

    button.addEventListener('click', function() {
        console.log('Button was clicked!');
        alert('Consultando los base de datos, espere un momento por favor');
        button.disabled = true;
        button.textContent = 'Consultando...'; 

        get_data();

    });
});