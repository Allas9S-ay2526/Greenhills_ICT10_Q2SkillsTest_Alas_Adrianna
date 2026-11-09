#
from pyscript imposrt display, document


    def countries_capital(e):
        documnet.getElementById('output').innerHTML = ''
        user_input = document.getElementById('input1').value.capitalize().strip()

        Elements = {
        'H': {'name': 'Hydrogen', 'symbol':'H', 'number': 1, 'mass': 1.008},
        'C': {'name': 'Carbon','symbol':'C', 'number': 6, 'mass': 12.011},
        'N': {'name': 'Nitrogen','symbol':'N', 'number': 7, 'mass': 14.001},
        'He': {'name': 'Helium','symbol':'He', 'number': 2, 'mass': 4.0026},
        'Ne': {'name': 'Neon','symbol':'Ne', 'number': 10, 'mass': 20.180},
        'Ar': {'name': 'Argon','symbol':'Ar', 'number': 18, 'mass': 39.948},
        'Kr': {'name': 'Krypton','symbol':'Kr', 'number': 36, 'mass': 83.798},
        'Xe': {'name': 'Xenon','symbol':'Xe', 'number': 54, 'mass': 131.29},
        'Rn': {'name': 'Radon','symbol':'Rn', 'number': 86, 'mass': 222}
        'O': {'name': 'Oxygen','symbol':'O', 'number': 8, 'mass': 16.000},
        'F': {'name': 'Fluorine','symbol':'F', 'number': 9, 'mass': 19.000},
        'P': {'name': 'Phosphorus','symbol':'P', 'number': 15, 'mass': 30.974},
        'S': {'name': 'Sulfur','symbol':'S', 'number': 16, 'mass': 32.06},
        'Cl': {'name': 'Chlorine','symbol':'Cl', 'number': 17, 'mass': 35.45},
        'Se': {'name': 'Selenium','symbol':'Se' 'number': 34, 'mass': 78.971},
        'Br': {'name': 'Bromine','symbol':'Br', 'number': 35, 'mass': 79.904},
        'I': {'name': 'Iodine','symbol':'I', 'number': 53, 'mass': 126.90},
        
       }

    element_checker = user_input in Elements
    display_message = (f'Sorry, no {user_input} in the list', f'{user_input} is in the list')display(display_message[element_checker], target='output')