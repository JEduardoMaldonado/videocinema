import json

class cliente:  
    data = []

    def read(self):
        with open('clientes.json','r') as file:
            data = json.load(file)
            self.data = data['results'] 

    def getCliente(self): 
        clientes = []
        for row in self.data:
            cliente = row['nombre']
            if cliente not in clientes:
                clientes.append(cliente)
        return clientes

    
                
class peliculas:  
    peli = []

    def read(self):
        with open('peliculas.json','r') as file:
            peli = json.load(file)
            self.peli = peli['results'] 

    def getPelicula(self): 
        peliculas = []
        for row in self.peli:
            pelicula = row['nombre']
            if pelicula not in peliculas:
                peliculas.append(pelicula)
        return peliculas
        