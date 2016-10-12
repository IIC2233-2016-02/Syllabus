from threading import Thread, Lock


# Este ejemplo es del material de clases, es para cuando se debe bloquear
# un recurso utilizado por TODAS las instancias pertenecientes a una Clase.
# En este caso, se busca bloquear el acceso a un solo archivo



class FileWriter(Thread):
    # Creamos el lock para bloquear el acceso de TODAS las instancias
    # al archivo que se esta escribiendo
    lock_file = Lock()
    
    def __init__(self, i, archivo):
        super().__init__()
        self.i = i
        self.archivo = archivo
    
    def run(self):
        with FileWriter.lock_file:
            self.archivo.write('Esta linea fue escrita por '
                               'el thread # {}\n'.format(self.i))
            
                
if __name__ == '__main__':
    num_threads = 15
    
    # Creamos un archivo para escribir una salida. Luego creamos los threads 
    # que escribirán dentro del archivo
    
    with open('salida.txt', 'w') as archivo:
        # Creamos los threads
        for i in range(num_threads):
            my_thread = FileWriter(i, archivo)
            my_thread.start() 