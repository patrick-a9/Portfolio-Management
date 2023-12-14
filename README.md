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
# Ejecución
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
>> **MATRIZ DE COVARIANZA**
>> * Un gráfico de matriz de covarianza de los rendimientos de tickers es una representación visual que muestra las relaciones de covarianza entre los rendimientos de diferentes activos financieros, representados por sus tickers o símbolos de identificación en el mercado. Este tipo de gráfico es comúnmente utilizado en el análisis de carteras y gestión de riesgos en finanzas.

>> [![g1.png](https://i.postimg.cc/qq8xDZbz/g1.png)](https://postimg.cc/bSwnsLjh)
>>> * Aquí hay algunas características clave de un gráfico de matriz de covarianza de rendimientos de tickers:
>>>> * **Eje de las etiquetas (tickers)**: En un lado de la matriz, se enumeran los tickers de los activos financieros incluidos en el análisis. Pueden ser acciones, bonos, fondos u otros instrumentos financieros.
>>>> * **Celdas de la matriz**: Cada celda de la matriz representa la covarianza entre los rendimientos de dos activos particulares. La covarianza mide cómo se mueven dos activos en relación el uno al otro. Un valor positivo indica una relación positiva (ambos activos tienden a moverse en la misma dirección), mientras que un valor negativo indica una relación negativa (los activos tienden a moverse en direcciones opuestas).
>>>> * **Coloración o sombreado**: Para facilitar la interpretación visual, las celdas de la matriz a menudo se sombrean o colorean de acuerdo con los valores de covarianza. Por ejemplo, celdas más oscuras pueden indicar una mayor covarianza (mayor correlación) entre los rendimientos, mientras que celdas más claras pueden indicar una menor covarianza.
>>>> * **Diagonal principal**: La diagonal principal de la matriz muestra la covarianza de cada activo consigo mismo, lo cual siempre es igual a la varianza del rendimiento de ese activo.

>> **GRÁFICO DE PESOS ÓPTIMOS**
>> * Un gráfico de pesos óptimos de los rendimientos de tickers representa visualmente la distribución de asignación de pesos ideales o óptimos en una cartera de activos financieros, identificados por sus tickers o símbolos en el mercado. Este tipo de gráfico es valioso en la gestión de carteras y ayuda a los inversores a entender cómo distribuir sus recursos entre diferentes activos para lograr ciertos objetivos, como maximizar el rendimiento o minimizar el riesgo.

>> [![Picture17.png](https://i.postimg.cc/VNPKB7xh/Picture17.png)](https://postimg.cc/SnVLmGNL)
>>> * Aquí hay algunas características clave de un gráfico de pesos óptimos de tickers:
>>>> * **Eje X (horizontal):** Cada tick en el eje X representa un activo financiero específico identificado por su ticker. Este eje muestra los diferentes tickers incluidos en la cartera.
>>>> * **Eje Y (vertical):**  La suma de todos los pesos en la cartera debería ser igual a 1 (o 100% si se expresa como porcentaje), ya que representa la totalidad de la asignación de activos.
>>>> * **Suma de pesos:** Para cada ticker, se representa una barra en el gráfico, ubicado en la posición correspondiente en el eje X y con una altura según la media de sus rendimientos en el eje Y.

>> **GRÁFICO DE MEDIAS**
>> * Un gráfico de medias de tickers presenta visualmente las medias (promedios) de los rendimientos de diferentes activos financieros, identificados por sus tickers o símbolos en el mercado.

>> [![g2.png](https://i.postimg.cc/tRPkgYqp/g2.png)](https://postimg.cc/yW1cQ63b)
>>> * Aquí hay algunas características clave de un gráfico de medias de tickers:
>>>> * **Eje X (horizontal):** Cada tick en el eje X representa un activo financiero específico identificado por su ticker. Este eje muestra los diferentes activos incluidos en el análisis.
>>>> * **Eje Y (vertical):** El eje Y muestra las medias de los rendimientos para cada activo. Cada punto en el eje Y corresponde a la media de los rendimientos de un activo financiero particular.

>> **GRÁFICO DE FRONTERA EFICIENTE**
>> * Un gráfico de frontera eficiente, también conocido como gráfico de frontera de cartera eficiente, es una representación visual de las combinaciones óptimas de activos financieros que ofrecen el máximo rendimiento esperado para un nivel de riesgo dado o el mínimo riesgo para un nivel dado de rendimiento. Este gráfico es una herramienta clave en la teoría moderna de carteras y es utilizado para ayudar a los inversores a tomar decisiones informadas sobre cómo asignar sus activos.

>>[![g3.png](https://i.postimg.cc/9M9dznjJ/g3.png)](https://postimg.cc/CBFBQJ5q)
>>> * Aquí hay algunas características clave de un gráfico de frontera eficiente de tickers:
>>>> * **Eje X (horizontal):** Representa el rendimiento esperado de la cartera. Cuanto más arriba en el eje Y, mayor es el rendimiento.
>>>> * **Puntos coloreados:** Cada punto en el gráfico representa una cartera específica. Estos puntos están coloreados según el ratio de Sharpe, que es una medida que relaciona el rendimiento de una cartera con su riesgo (volatilidad). Los colores indican diferentes niveles de eficiencia en términos de riesgo-rendimiento.

### Comentarios
* Si tienes más de un portafolio creado tambien se mostrará es información
* Puedes identificar tu portafolio a través del ID, por ejemplo: ID 1 equivale a Portafolio 1


