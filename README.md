# Proyecto de Sistema de Usuarios y Portafolios
Este proyecto constituye una solución integral que aborda la gestión de usuarios y portafolios, empleando Flask como el framework principal para el desarrollo web y SQLite como la base de datos subyacente. Además, incorpora técnicas de web scraping dirigidas a una página financiera específica, facilitando la descarga de los históricos de cierre del mes. Esta funcionalidad es crucial para proporcionar a los usuarios una visión detallada y actualizada de sus inversiones.

## Características Clave
### Gestión de Usuarios y Portafolios
El sistema ofrece una interfaz intuitiva que permite a los usuarios registrarse, ingresar al sistema de manera segura y gestionar sus portafolios de inversión de manera eficiente. Cada usuario puede personalizar su experiencia, ingresando la cantidad deseada de acciones y los correspondientes tickers, ya sea en mayúsculas o minúsculas.

### Web Scraping para Datos Financieros
La capacidad de realizar web scraping sobre una página financiera específica garantiza la obtención precisa de los históricos de cierre del mes. Esto proporciona a los usuarios información crucial para tomar decisiones informadas sobre sus inversiones y evaluar el rendimiento de sus portafolios.

### Optimización de Carteras
El sistema va más allá de la simple gestión de portafolios al incorporar herramientas avanzadas de optimización. Los usuarios pueden aprovechar algoritmos especializados para optimizar la distribución de sus activos, maximizando el rendimiento y gestionando eficazmente el riesgo.

### Visualización de Gráficos Financieros
La visualización desempeña un papel fundamental en la comprensión de los datos financieros. El proyecto incluye capacidades robustas de visualización, generando gráficos claros y perspicaces que permiten a los usuarios analizar y comparar fácilmente el rendimiento de sus inversiones a lo largo del tiempo.

## Requisitos
Para ejecutar este proyecto, es necesario tener instaladas las siguientes bibliotecas de Python. Se recomienda utilizar un entorno virtual para evitar conflictos con otras dependencias del sistema.
```bash
pip install -r requirements.txt
```
#Ejecución
## Ejecución General (base de datos y aplicación web)

1. Ejecuta el script **base.py** para inicializar y crear la base de datos.
> *   Solo se debe ejecutar una vez
2. Luego, ejecuta el script **app.py** para poner en marcha la web app y habilitar la funcionalidad web.

## Ejecución página web
1. **Registrarse**
> * LLenar el formulario de registro

> [![registro.png](https://i.postimg.cc/kgjFHScF/registro.png)](https://postimg.cc/K1MMkRCR)

2. **Ingresar al sistema**
> * Acceder con tu cuenta existente

>[![logeo.png](https://i.postimg.cc/YqH3LM0g/logeo.png)](https://postimg.cc/PNSZBGmr)

3.**Configurar tu portafolio**
> * Indica la cantidad deseada de acciones en tu portafolio.

>[![portafolio.png](https://i.postimg.cc/zfVSYf2m/portafolio.png)](https://postimg.cc/yJCSF7zn)

4. **Ingresar los Tickers de Acciones**
> * Introduce los tickers de las acciones, ya sea en mayúsculas o minúsculas.
> * **Los tickers solo pueden ser del mercado de estados unidos**
>> https://www.marketwatch.com/tools/markets/stocks/country/united-states

> [![tickers.png](https://i.postimg.cc/3NHgGF87/tickers.png)](https://postimg.cc/7GmG87JQ)

5. **Crear Portafolio**
> * Haz clic en el botón **crear portafolio** para registrarlo.

>[![pcreado.png](https://i.postimg.cc/zXFkn6HQ/pcreado.png)](https://postimg.cc/4mntG85v)

6. **Cerrar Sesión**
> Finaliza tu sesión para proteger tu información.

### Comentarios
* El botón de restablecer restablece el número de acciones a ingresar a su valor inicial.
* Se pueden crear tantos usuarios como se deseen, siempre y cuando el correo y el nombre de usuario sean únicos.
* Si decides volver a abrir sesión, se mostrarán todos los portafolios que hayas creado previamente.
> [![portafolioscreados.png](https://i.postimg.cc/XvmKj0tr/portafolioscreados.png)](https://postimg.cc/xkGN5BfQ)
* Puedes verificar el correcto ingreso de usuarios y portafolios en la base de datos.
> [![Picture15.png](https://i.postimg.cc/rpHLccx0/Picture15.png)](https://postimg.cc/67CPLkHt)

## Ejecución del Optimizador de Portafolios
1. Ejecuta el script **resultados.py**
2. Al ejecutarse, se solicitará tu usuario y contraseña con los que te registraste en la página web.
> [![ejecuci-n-de-ana-lis.png](https://i.postimg.cc/prNBZtBw/ejecuci-n-de-ana-lis.png)](https://postimg.cc/Hc25YRRz)
3. El sistema generará tablas detalladas en la terminal y presentará gráficos que ilustran el rendimiento de todos tus portafolios creados en una nueva ventana.
> * **Tablas**
>> [![resultados2.png](https://i.postimg.cc/fyjYfSyd/resultados2.png)](https://postimg.cc/H8nJpxQW)
> * **Graficos**
>> [![g1.png](https://i.postimg.cc/qq8xDZbz/g1.png)](https://postimg.cc/bSwnsLjh)
>> [![g2.png](https://i.postimg.cc/tRPkgYqp/g2.png)](https://postimg.cc/yW1cQ63b)
>> [![g3.png](https://i.postimg.cc/9M9dznjJ/g3.png)](https://postimg.cc/CBFBQJ5q)

### Comentarios
* Si tienes más de un portafolio creado tambien se mostrará es información
* Puedes identificar tu portafolio a través del ID, por ejemplo: ID 1 equivale a Portafolio 1


