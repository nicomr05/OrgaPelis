import pandas as pd

tipo = False # Cambiar a 'False' si se quiere cambiar el tipo de lista ordenada

if tipo:
    from array_ordered_positional_list import ArrayOrderedPositionalList as ListaOrdenada
else:
    from linked_ordered_positional_list import LinkedOrderedPositionalList as ListaOrdenada

class Pandas:
    '''
    Clase que gestiona las estadísticas de las películas y las muestra por pantalla.

    Methods
    -------
    __init__(self) -> None:
        Asigna atributos al objeto.

    estad_totales(self, lista:ListaOrdenada) -> tuple:
        Recoge los valores de cada película y los añade al dataframe como diccionario.
        Luego devuelve una tupla con las estadísticas que se solicitaron.

    peliculas_por_director(self) -> None:
        Cuenta el número de películas por director/a.

    media_director(self) -> None:
        Realiza la media de la puntuación por director/a.

    media_por_anho(self) -> None:
        Realiza la media por año de estreno.
    '''
    def __init__(self) -> None:
        '''
        Método que asigna atributos al objeto.

        Returns
        -------
        None
        '''
        self._dataframe = pd.DataFrame(columns=['Director', 'Título', 'Fecha', 'Puntuación'])
    
    def estad_totales(self, lista:ListaOrdenada) -> tuple:
        '''
        Método que recoge los valores de cada película y los añade al dataframe como diccionario.
        Luego devuelve una tupla con las estadísticas que se solicitaron.

        Returns
        -------
        tuple
         Tupla con tres valores: número de películas por director, media de puntuación del
         director y la media de puntuación por año.
        '''
        for pelicula in lista:
            fila: dict = {'Director':pelicula.director, 'Título':pelicula.titulo, 'Fecha':pelicula.anho_estreno, 'Puntuación':pelicula.puntuacion_media}
            self.dataframe.loc[len(self.dataframe)] = fila # Añadimos cada diccionario al dataframe. Intentamos hacerlo con append pero daba error.
        
        return (self.peliculas_por_director(), self.media_director(), self.media_por_anho())
            
    def peliculas_por_director(self) -> None:
        '''
        Método que cuenta el número de películas por director/a.

        Returns
        -------
        None
        '''
        group_col = 'Director'
        target_col = 'Título'
        data_directores = self.dataframe.groupby(group_col).agg({target_col: ['count']})

        cad: str = 'Número de películas por director'
        n: int = 50

        print ('\n','#'*n, sep='')
        print (f'{cad:^50}')
        print ('#'*n)
        print ('\n',f'{data_directores}', sep='')
    
    def media_director(self) -> None:
        '''
        Método que realiza la media de la puntuación por director/a.

        Returns
        -------
        None
        '''
        group_col = 'Director'
        target_col = 'Puntuación'
        data_directores = self.dataframe.groupby(group_col).agg({target_col: ['mean']})
        
        cad: str = 'Puntuación media agrupada por director'
        n: int = 50

        print ('\n'*3,'#'*n, sep='')
        print (f'{cad:^50}')
        print ('#'*n)
        print ('\n',f'{data_directores}', sep='')
    
    def media_por_anho(self) -> None:
        '''
        Método que realiza la media por año de estreno.

        Returns
        -------
        None
        '''
        group_col = 'Fecha'
        target_col = 'Puntuación'
        data_directores = self.dataframe.groupby(group_col).agg({target_col: ['mean']})
        
        cad: str = 'Puntuación media agrupada por año'
        n: int = 50

        print ('\n'*3,'#'*n, sep='')
        print (f'{cad:^50}')
        print ('#'*n)
        print ('\n',f'{data_directores}', sep='')

    @property
    def dataframe(self) -> pd.DataFrame:
        return self._dataframe