class Pelicula:
    '''
    Clase abstracta para una película.
    La clase tiene como atributos el director, título, año de estreno y puntuación media
    de la película.

    Attributes
    ----------
    titulo : str
     Título de la película.
    director : str
     Director de la película.
    anho_estreno : int
     Año de estreno de la película.
    puntuacion_media : int
     Puntuación media de la película.

    Methods
    -------
    __init__(self, director:str, titulo:str, anho_estreno:int, puntuacion_media:float) -> None:
        Asigna atributos al objeto.
    
    __str__(self) -> str:
        Implementación del método mágico "str".
        Imprime un string informativo de la película.
    
    __eq__(self, pelicula:'Pelicula') -> bool:
        Implementación del método mágico "==".
    
    __gt__(self, pelicula:'Pelicula') -> bool:
        Implementación del método mágico ">".

    __lt__(self, pelicula:'Pelicula') -> bool:
        Implementación del método mágico "<".

    __ge__(self, pelicula:'Pelicula') -> bool:
        Implementación del método mágico ">=".
    '''
    
    def __init__(self, director:str, titulo:str, anho_estreno:int, puntuacion_media:float) -> None:       
        '''
        Método mágico que asigna atributos al objeto.

        Parameters
        ----------
        titulo : str
         Título de la película.
        director : str
         Director de la película.
        anho_estreno : int
         Año de estreno de la película.
        puntuacion_media : int
         Puntuación media de la película.
        '''
        self._director = director
        self._titulo = titulo
        self._anho_estreno = anho_estreno
        self._puntuacion_media = puntuacion_media
    
    def __str__(self) -> str:
        '''
        Implementación del método mágico "str".
        Imprime un string informativo de la película.

        Returns
        -------
        str
         String informativo de una película.
        '''
        cadena: str = f'{self.director:<25} | '
        cadena += f'{self.titulo:^40} | '
        cadena += f'{self.anho_estreno:^6} | '
        cadena += f'{self.puntuacion_media:^4}'
        
        return cadena
    
    def __eq__(self, pelicula:'Pelicula') -> bool:
        '''
        Implementación del método mágico "==".
        
        Parameters
        ----------
        pelicula : Pelicula
         Película sobre la que se quiere comprobar la igualdad.
        
        Returns
        -------
        bool
        '''
        if self.director == pelicula.director and \
           self.anho_estreno == pelicula.anho_estreno and \
           self.titulo == pelicula.titulo:
            return True
        
        return False
    
    def __gt__(self, pelicula:'Pelicula') -> bool:
        '''
        Implementación del método mágico ">".
        
        Parameters
        ----------
        pelicula : Pelicula
         Película sobre la que se quiere comprobar la desigualdad.
        
        Returns
        -------
        bool
        '''
        if self.director != pelicula.director:
            return self.director > pelicula.director
        
        elif self.anho_estreno != pelicula.anho_estreno:
            return self.anho_estreno > pelicula.anho_estreno
        
        elif self.titulo != pelicula.titulo:
            return self.titulo > pelicula.titulo
        
        return False

    def __lt__(self, pelicula:'Pelicula') -> bool:
        '''
        Implementación del método mágico "<".
        
        Parameters
        ----------
        pelicula : Pelicula
         Película sobre la que se quiere comprobar la desigualdad.
        
        Returns
        -------
        bool
        '''
        if self.director != pelicula.director:
            return self.director < pelicula.director
        
        elif self.anho_estreno != pelicula.anho_estreno:
            return self.anho_estreno < pelicula.anho_estreno
        
        elif self.titulo != pelicula.titulo:
            return self.titulo < pelicula.titulo
        
        return False
    
    def __ge__(self, pelicula:'Pelicula') -> bool:
        '''
        Implementación del método mágico ">=".
        
        Parameters
        ----------
        pelicula : Pelicula
         Película sobre la que se quiere comprobar la (des)igualdad.
        
        Returns
        -------
        bool
        '''
        return (self == pelicula or self > pelicula)
    
    @property
    def director(self) -> str:
        return self._director
    
    @property
    def titulo(self) -> str:
        return self._titulo
    
    @property
    def anho_estreno(self) -> int:
        return self._anho_estreno
    
    @property
    def puntuacion_media(self) -> int:
        return self._puntuacion_media