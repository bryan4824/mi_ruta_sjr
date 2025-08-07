import reflex as rx
from WorkspaceWebPython.components.link_button import links_button
from WorkspaceWebPython.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Rutas de transporte público a sitios Plazas Comerciales:"),
        links_button(
            "Ruta 10",
            "Cerro Gordo a 5 de mayo, Centro / Coopel - Soriana - HEDRAUI - Plaza San Juan", 
            "https://www.google.com/maps/d/u/3/edit?mid=1EGC2hLRUNrC9YwcKZHZfIXkkXMJUF9M&usp=sharing"
        ),
        links_button(
            "Ruta 2",
            "Pedregoso a Vista Hermosa / CHEDRAUI - Plaza San Juan - Galerias - Coopel - Soriana", 
            "https://www.google.com/maps/d/u/3/edit?mid=1z1DTLutRmdlh66OIwS8NEuuIAZCAJDE&usp=sharing"
        ),
        links_button(
            "Ruta 4",
            "chedraui - coopel - proomoda - soriana - elektra", 
            "https://www.google.com/maps/d/u/3/edit?mid=1Jr_HJ4v9_WpOZgH-rQo5RUBq94LUGzA&usp=sharing"
        ),
        links_button(
            "Ruta 8",
            "OXXO - Coopel - Chedraui - Infonavit San Isidro - Mini Super - Los laureles",
            "https://www.google.com/maps/d/u/3/edit?mid=1hEQvhtDtvBMivlxykw-RlsOHg4sAgbY&usp=sharing"
        ),
        links_button(
            "Ruta 11",
            "Soriana - Coopel - Cinebox - El Zorro - Aurrera - Kimberly - Tienda Comex - Office Depot",
            "https://www.google.com/maps/d/u/3/edit?mid=1t2Chox0wYZmvppJeSLUEpODYmyvdajk&usp=sharing"
        ),
        links_button(
            "Ruta 16",
            "Super Q - El Zorro - Walmart - Bodega Aurrera - Mcdonald´s - The Home Depot - Chedraui",
            "https://www.google.com/maps/d/u/3/edit?mid=1Acsh2K9YjFXIrZzHr1WL0bO1B94H1lg&usp=sharing"
        ),
        links_button(
            "Ruta 20",
            "Walmartt - Aurrera - Office Depot - OXXO - The Home Depot - SAMS CLUB",
            "https://www.google.com/maps/d/u/3/edit?mid=1kdEZPC76M38ff0RBgZrpQc8da3pAJiI&usp=sharing"
        ),
         links_button(
            "Ruta 1",
            "Office Depot - Coppel Moctezuma – Chedraui - Plaza y tecnología SJR – Bazar CHINO - The Home Depot México",
            "https://www.google.com/maps/d/u/2/edit?mid=1WuHc_RLbhjmNWZ79xit4uChLBjDquNw&usp=sharing"
        ),
          links_button(
            "Ruta 39",
            "Banco del bienestar",
            "https://www.google.com/maps/d/u/2/edit?mid=1k2HMfaqwrdZcaOyr3LcGe7SBTwCCfaQ&usp=sharing"
        ),
          links_button(
            "Ruta 25",
            "The Home Depot México - Bodega Aurrera Express - Bazar CHINO - Coppel Moctezuma – Chedraui - Plaza y tecnología SJR",
            "https://www.google.com/maps/d/u/2/edit?mid=1MNSt1cir7x7sviSW0elcM1y0Kymvapc&usp=sharing"
        ),
        links_button(
            "Ruta 30",
            "The Home Depot – Walmart – Chedraui - H-E-B SJR",
            "https://www.google.com/maps/d/u/2/edit?mid=1YDvqiZEJudZ2_aiZ85VvB50jB23Fxeo&usp=sharing"
        ),
        links_button(
            "Ruta 41",
            "Chedraui - Tiendas 3B",
            "https://www.google.com/maps/d/u/2/edit?mid=1Lm-ucP2la1ZNlzC5VTkgnAfSk01dfS8&usp=sharing"
        ),
        links_button(
            "Ruta 42",
            "Mercado reforma",
            "https://www.google.com/maps/d/u/2/edit?mid=1M_E7erb4dHA_oPF7Rll9jzt7QgEbBl0&usp=sharing"
        ),
         links_button(
            "Ruta 43",
            "Chedraui - Soriana",
            "https://www.google.com/maps/d/u/2/edit?mid=1C-binontplecbBrLeQGiBvtaItlUpe8&usp=sharing"
        ),
          links_button(
            "Ruta 44",
            "Office depot – Chedraui - Bazar CHINO",
            "https://www.google.com/maps/d/u/2/edit?mid=1PnRwWbR6VyGVABM17w-sRd2YN7yc8MI&usp=sharing"
        ),
        
        title("Rutas de transporte público a sitios de salud:"),
        links_button(
            "Ruta 2",
            "Pedregoso a Vista Hermosa / Cruz Roja - Coscami - Hosp. San Jose", 
            "https://www.google.com/maps/d/u/3/edit?mid=1z1DTLutRmdlh66OIwS8NEuuIAZCAJDE&usp=sharing"
        ),
        links_button(
            "Ruta 4",
            "farmacias del ahorro - Unidad Médica No.7 - Farmacias Similares - Hospital Integral San Juan del Río", 
            "https://www.google.com/maps/d/u/3/edit?mid=1Jr_HJ4v9_WpOZgH-rQo5RUBq94LUGzA&usp=sharing"
        ),
        links_button(
            "Ruta 7",
            "Seguro - Cruz Verde - IMSS - Hospital Celular Juárez - Unidad de Atención Ciudadana", 
            "https://www.google.com/maps/d/u/3/edit?mid=1akCTFZR1TTdG4ty6IqsG_DndQh6pzrg&usp=sharing"
        ),
         links_button(
            "Ruta 8",
            "IMSS - Farmacias del Ahorro - Clinica Médica del Centro - Consultorio De Medicina Dental", 
            "https://www.google.com/maps/d/u/3/edit?mid=1hEQvhtDtvBMivlxykw-RlsOHg4sAgbY&usp=sharing"
        ),
         links_button(
            "Ruta 11",
            "Hospital General - Cruz Verde - Farmacias Similares - Cuz Roja", 
            "https://www.google.com/maps/d/u/3/edit?mid=1t2Chox0wYZmvppJeSLUEpODYmyvdajk&usp=sharing"
        ),
        links_button(
            "Ruta 16",
            "Farmacias Similares - Centro Médico Veterinario Canino", 
            "https://www.google.com/maps/d/u/3/edit?mid=1Acsh2K9YjFXIrZzHr1WL0bO1B94H1lg&usp=sharing"
        ),
           links_button(
            "Ruta 20",
            "Cruz Roja - Cruz Verde", 
            "https://www.google.com/maps/d/u/3/edit?mid=1kdEZPC76M38ff0RBgZrpQc8da3pAJiI&usp=sharing"
        ),
            links_button(
            "Ruta 28",
            "Farmacias de Genéricos Cruz Verde - Farmacia Guadalajara - Farmacia del Ahorro - Cruz Roja", 
            "https://www.google.com/maps/d/u/3/edit?mid=1ahDD1hERbD0-jbc_K2FBU_rwaBFv50k&usp=sharing"
        ),
            links_button(
            "Ruta 1",
            "Unidad de Medicina Familiar", 
            "https://www.google.com/maps/d/u/2/edit?mid=1WuHc_RLbhjmNWZ79xit4uChLBjDquNw&usp=sharing"
        ),
             links_button(
            "Ruta 39",
            "IMSS hospital general de zona 3 - Veterinaria Doctor KN - Farmacias similares - Farmacias SALUD-VITAL - Clínica dental Durango", 
            "https://www.google.com/maps/d/u/2/edit?mid=1k2HMfaqwrdZcaOyr3LcGe7SBTwCCfaQ&usp=sharing"
        ),
            links_button(
            "Ruta 25",
            "Cruz Roja SJR - Veterinaria HOMEVET", 
            "https://www.google.com/maps/d/u/2/edit?mid=1MNSt1cir7x7sviSW0elcM1y0Kymvapc&usp=sharing"
        ),
            links_button(
            "Ruta 30",
            "Salud Digna - Centro médico Veterinario Canino - Cruz Roja SJR", 
            "https://www.google.com/maps/d/u/2/edit?mid=1YDvqiZEJudZ2_aiZ85VvB50jB23Fxeo&usp=sharing"
        ),
            links_button(
            "Ruta 41",
            "Salud Digna - Farmacia Guadalajara - Clínica Veterinaria - Farmacias Gi-Pedregoso - Farmacias SALUD-VITAL - Farmacia Guadalajara de las Águilas", 
            "https://www.google.com/maps/d/u/2/edit?mid=1Lm-ucP2la1ZNlzC5VTkgnAfSk01dfS8&usp=sharing"
        ),
            links_button(
            "Ruta 37",
            "Farmacias similares - Hospital veterinario Punto Mascota", 
            "https://www.google.com/maps/d/u/2/edit?mid=1az87YhSHXsG5R5YrlLyRV7FtEsQ12lc&usp=sharing"
        ),
            links_button(
            "Ruta 40",
            "Dentista - Veterinaria Doctor KN - Consultorio Médico Farmaliz - IMSS Hospital General de zona 3 - Farmacia Guadalajara de las Águilas", 
            "https://www.google.com/maps/d/u/2/edit?mid=1GheGjY89rVVqQ-OVVr4WMqLvDkY3tHI&usp=sharing"
        ),
            links_button(
            "Ruta 42",
            "Farmacia GI - DR. Erick Rios Estrada - Radio Dental", 
            "https://www.google.com/maps/d/u/2/edit?mid=1M_E7erb4dHA_oPF7Rll9jzt7QgEbBl0&usp=sharing"
        ),
        



        title("Rutas de transporte público a sitios de escuelas:"),
        links_button(
            "Ruta 2",
            "Pedregoso a Vista Hermosa / Sec. RRO - Universidad UAQ - Primario Francisco Monroy Velez", 
            "https://www.google.com/maps/d/u/3/edit?mid=1z1DTLutRmdlh66OIwS8NEuuIAZCAJDE&usp=sharing"
        ),
        links_button(
            "Ruta 4",
            "Primaria Octavio Paz - UNIESQ - Primaria Amado Nervo - Preescolar y Maternal Cendi Renacimiento - Prepa IDEQ", 
            "https://www.google.com/maps/d/u/3/edit?mid=1Jr_HJ4v9_WpOZgH-rQo5RUBq94LUGzA&usp=sharing"
        ),
        links_button(
            "Ruta 7",
            "C.B.T.I.S - Tecnológico - Colegio Real de Santiago SJR - Preescolar Esperanza Cabrera - CUIEP", 
            "https://www.google.com/maps/d/u/3/edit?mid=1akCTFZR1TTdG4ty6IqsG_DndQh6pzrg&usp=sharing"
        ),
          links_button(
            "Ruta 8",
            "Preescolar Simon Bolivar - Primaria Jose Maria Arteaga - Instituto Universitario del Río - Preescolar Esperanza Cabrera - Preescolar Tomas Alva Edison", 
            "https://www.google.com/maps/d/u/3/edit?mid=1hEQvhtDtvBMivlxykw-RlsOHg4sAgbY&usp=sharing"
        ),
        links_button(
            "Ruta 11",
            "UAQ - Instituto del Bajío San Juan del Río - ALPES Centro de Estudios - Escuela Secundaria Técnica No. 11", 
            "https://www.google.com/maps/d/u/3/edit?mid=1t2Chox0wYZmvppJeSLUEpODYmyvdajk&usp=sharing"
        ),
         links_button(
            "Ruta 16",
            "Universidad Metropolitana y Preparatoria - Secundaria Antonio Caso - Preescolar Esperanza Cabrera", 
            "https://www.google.com/maps/d/u/3/edit?mid=1Acsh2K9YjFXIrZzHr1WL0bO1B94H1lg&usp=sharing"
        ),
           links_button(
            "Ruta 20",
            "Instituto del Bajío San Juan del Río ", 
            "https://www.google.com/maps/d/u/3/edit?mid=1kdEZPC76M38ff0RBgZrpQc8da3pAJiI&usp=sharing"
        ),
          links_button(
            "Ruta 23",
            "Tecnológico Nacional de México, CBTIS No.145, Grupo educativo CITEM, UNIESQ", 
            "https://www.google.com/maps/d/u/3/edit?mid=1zIIqvb6HsLC1ii9lYCNV6FD1HN6vsYw&usp=sharing"
        ),
          links_button(
            "Ruta 28",
            "Primaria Melchor Ocampo, INSTITUTO ISAIAS, Colegio Constantino, A.C.", 
            "https://www.google.com/maps/d/u/3/edit?mid=1ahDD1hERbD0-jbc_K2FBU_rwaBFv50k&usp=sharing"
        ),

        title("Rutas de transporte público a tiendas de ropa y estetica:"),
        links_button(
            "Ruta 7",
            "Estetica Efectos - Unisex Stahy - Gaby", 
            "https://www.google.com/maps/d/u/3/edit?mid=1akCTFZR1TTdG4ty6IqsG_DndQh6pzrg&usp=sharing"
        ),


        title("Rutas de transporte público a sitios Mantenimiento de Autos:"),
        links_button(
            "Ruta 4",
            "Taller Barron - Bike Center - Frenos y Embragues - Taller Automotriz Soto", 
            "https://www.google.com/maps/d/u/3/edit?mid=1Jr_HJ4v9_WpOZgH-rQo5RUBq94LUGzA&usp=sharing"
        ),
         links_button(
            "Ruta 11",
            "Materiales Equipos y Herramientas para Vulcanizadoras - llantas y rines Yokohama -  Refaccionaria AutoZone", 
            "https://www.google.com/maps/d/u/3/edit?mid=1t2Chox0wYZmvppJeSLUEpODYmyvdajk&usp=sharing"
        ),
          links_button(
            "Ruta 23",
            "Materiales Equipos y Herramientas para Vulcanizadoras - electrico El Pecas - Autolavado La Bella Cosa", 
            "https://www.google.com/maps/d/u/3/edit?mid=1zIIqvb6HsLC1ii9lYCNV6FD1HN6vsYw&usp=sharing"
        ),
         links_button(
            "Ruta 28",
            "Taller Mecánico Y Vulcanizadora El Chilango - Refaccionaria Charly", 
            "https://www.google.com/maps/d/u/3/edit?mid=1ahDD1hERbD0-jbc_K2FBU_rwaBFv50k&usp=sharing"
        ),


        title("Rutas de transporte público a sitios de entretenimiento:"),
        links_button(
            "Ruta 4",
            "cinebox - campo beisbol - parque Las Garzas - parque San Juan", 
            "https://www.google.com/maps/d/u/3/edit?mid=1Jr_HJ4v9_WpOZgH-rQo5RUBq94LUGzA&usp=sharing"
        ),
         links_button(
            "Ruta 7",
            "Nuevo Parque - Parque San Juan - Centro De La Tecnología - Jardín de la familia", 
            "https://www.google.com/maps/d/u/3/edit?mid=1akCTFZR1TTdG4ty6IqsG_DndQh6pzrg&usp=sharing"
        ),
         links_button(
            "Ruta 8",
            "Jardín de la Familia - Madness Training Center TRX - Tecnologías de Información - Balneario Santa Mónica Tranvía Turístico", 
            "https://www.google.com/maps/d/u/3/edit?mid=1hEQvhtDtvBMivlxykw-RlsOHg4sAgbY&usp=sharing"
        ),
          links_button(
            "Ruta 11",
            "Parque de las Garzas - Terraza Jardín La Fiesta - Tiger GYM, Parque de Paseo de Loma Alta - Parque Infonavit San Cayetano", 
            "https://www.google.com/maps/d/u/3/edit?mid=1t2Chox0wYZmvppJeSLUEpODYmyvdajk&usp=sharing"
        ),
           links_button(
            "Ruta 16",
            "Campo de Fútbol Santa Cruz Nieto - Jardín del Valle - Cancha de Futbol 7 Col. Jardines del Valle II", 
            "https://www.google.com/maps/d/u/2/edit?mid=1Acsh2K9YjFXIrZzHr1WL0bO1B94H1lg&usp=sharing"
        ),
            links_button(
            "Ruta 20",
            "Jardin de la Familia - Parque Infonavit San Cayetano - Plaza de toros del recinto ferial de San Juan del Río - Multideportivo San Juan del Río - Unidad Deportiva Norte", 
            "https://www.google.com/maps/d/u/2/edit?mid=1kdEZPC76M38ff0RBgZrpQc8da3pAJiI&usp=sharing"
        ),
              links_button(
            "Ruta 23",
            "Parque Quintas De Guadalupe - Parque Lomas Del Pedregal", 
            "https://www.google.com/maps/d/u/2/edit?mid=1zIIqvb6HsLC1ii9lYCNV6FD1HN6vsYw&usp=sharing"
        ),
        width="100%"  
    )
