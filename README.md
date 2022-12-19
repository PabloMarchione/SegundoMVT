# SegundoMVT
Pablo Marchione
Entrega Nº7

"primerapp"

superuser:
usuario= admin
passsword= admin

Aplicacion para crear Jugadores, Equipos y Estadios (Con sus respectivos formularios).

1. Una vez ejecutado el "runserver" agregar a la url /primerapp para acceder al Home.
2. Desde ahi con cada boton se pueden crear y guardar los objetos en la bbdd.
3. El boton "Buscar Jugador" le va a requerir un campo de solo texto que especificamente coincida con el nombre a buscar asi tambien con la primer letra de cada nombre en mayuscula, por ej "Juan Roman". Dejar el campo totalmente vacio cuenta como error, vera un mensaje de advertencia y podra volver a realizar la busqueda.
4. Una vez realizada una busqueda exitosa, se podra observar el listado de dichos jugadores con su nombre,apellido y equipo(su mejor epoca) respectivamente.
5. Por ultimo, todos los modelos estan registrados, puede ingresar como administrador, hacer y deshacer a su antojo.

notas:
1. El formulario de "estadios" esta constituido con SOLO html, se notara la diferencia a simple vista, esto se realizo a conciencia con el mero objetivo de practicar.
2. En cambio en los formularios de "jugadores" y "equipos" se concibieron usando Django, por los mismos motivos ya mencionados.
3. El "estilo" de la pagina es el mismo que en las clases por pura comodidad, todos los templates heredan del archivo "fader.html" como asi lo requiere la consigna.
4. En el formulario de busqueda de jugadores, si ingresas un nombre existente muestra al jugador, si no ingresas nada muestra el mensaje de error, pero no pude hacer un "ELIF" para comparar el get en caso de que no se cumpla ninguno de esos escenarios, me quedo esa laguna ahi mismo :(.

 

listado de Jugadores "pre-cargados":
Juan Roman Riquelme
Fernando Redondo
Johan Cruyff
