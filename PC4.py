# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta 
# o abrimos el folder desde visual Studio Code 


# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# streamlit run your_script.py
# python -m streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Generamos 3 páginas en la aplicación web de Streamlit.
# Generamos una página principal, otra donde contaran su experiencia aprendiendo a programar y una tercera donde presentarán sus gráficos.

# Creamos la lista de páginas
paginas = ['Inicio', 'Experiencia', 'Gráficos']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona una página', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Inicio':

    # La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>Futura publicista vs Python</h1>", unsafe_allow_html=True)

    # <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
    # La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
    # el atributo style se utiliza para agregar estilos CSS. 
    # En este caso, el texto está alineado al centro (text-align: center;). 
    # Pueden agregar emojis en el texto de Markdown utilizando códigos de emoji, por ejemplo:
    # <h1 style='text-align: center;'>Aquí escribe un nombre creativo para tu blog 📝</h1>
    # También pueden personalizar el color del texto utilizando el atributo style, por ejemplo:
    # <h1 style='text-align: center; color: blue;'>Nombre de tu blog</h1>
    # El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

    # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)

    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen de perfil
    col1.image("abc.png", caption='Mi primer ciclo en facultad', width=300)

    # col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar. 
    # En este caso, la imagen es "ellie.png". 
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen, 
    # en este caso "Aquí puedes escribir una etiqueta debajo de la imagen". 
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

    # En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
    # Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
    # ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

    texto = """
    Hola! Soy Nathaly Chávez, estudiante de quinto ciclo de Publicidad y entusiasta de todo lo que combina creatividad, cultura y tecnología. Vengo de Lima, Perú, y me apasionan los temas que conectan el branding personal con la diversidad cultural y la forma en que nos comunicamos en entornos cada vez más digitales.
    El ciclo pasado desarrollé una monografía donde analizo la serie Emily en París desde una mirada crítica y creativa: ¿cómo influyen la imagen personal y los estereotipos culturales en la percepción de las marcas? Ese tipo de preguntas son las que me motivan a seguir explorando el poder simbólico de la publicidad.
    Además, este semestre me enfrenté por primera vez al mundo de la programación con Python. Al principio fue intimidante, pero luego, entre Google Colab, gráficos interactivos y Visual Studio, descubrí que programar también puede ser una herramienta creativa para visualizar datos, entender patrones y narrar ideas desde otro ángulo. Fue como descubrir otro lenguaje, uno que también comunica.
    En el futuro me gustaría especializarme en diseño visual, branding estratégico y producción digital, combinando lo conceptual con lo técnico. Sueño con desarrollar campañas que no solo impacten, sino que también representen contextos reales y diversas formas de ser.
    Y cuando no estoy creando, analizando o programando, me encanta caminar con mi perrita, jugar con apps de edición, armar playlists que reflejan estados de ánimo y, de vez en cuando, soñar despierta con tener mi propio estudio creativo ✨
    """

    # Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
    
    # Mostramos el texto
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
    # La etiqueta <div> se utiliza para agrupar contenido en HTML. 
    # En este caso, el texto está justificado (text-align: justify;). 
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto} se reemplaza por el valor de la variable texto.

elif  pagina_seleccionada == 'Experiencia':

    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h1>", unsafe_allow_html=True)

    # En esta sección debes describir y comentar tu experiencia aprendiendo a programar
    # ¿Cómo te sentiste al principio?, 
    # ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
    # ¿Qué te gustaría hacer con la programación en el futuro? 

    # Agregar un  texto para la respuesta
    texto_2 = """
    Al inicio del curso, aprender a programar me generaba mucha ansiedad porque era la primera vez que veía Python y no sabía bien por dónde empezar. Todo me sonaba muy técnico y complicado, como si fuera un lenguaje completamente ajeno a mí. Sin embargo, a medida que avanzaban las clases y comenzaba a practicar, especialmente en Google Colab, fui perdiendo miedo. Colab me pareció bastante accesible para principiantes, ya que no necesitaba instalar nada y podía ir ejecutando por bloques, lo que facilitaba mucho el proceso de prueba y error.
    Después empecé a usar Visual Studio Code, y aunque al principio fue un poco más técnico de configurar (como activar entornos virtuales o instalar paquetes), me ayudó a entender mejor cómo funciona realmente Python en mi computadora y me dio más control sobre lo que estaba haciendo. Esa transición me hizo sentir que estaba avanzando hacia un nivel más serio en la programación.
    La programación me ha enseñado a pensar de forma más lógica y ordenada, y sobre todo, a ser paciente conmigo misma cuando algo no sale a la primera. Me gusta que programar te permite crear soluciones a problemas reales, desde algo pequeño como automatizar una tarea hasta visualizar datos de forma interactiva. En el futuro me gustaría usar la programación como una herramienta complementaria a mi carrera, quizás para desarrollar proyectos interactivos, analizar datos de campañas o incluso crear visualizaciones creativas en medios digitales.
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 21px;'>{texto_2}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el texto está justificado (text-align: justify;).
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto_2.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto_2} se reemplaza por el valor de la variable texto.

    # Agregamos un subtítulo para el video
    st.markdown("<h2 style='text-align: center;'>Siempre hay una primera vez para todo, atrévete!!!</h2>", unsafe_allow_html=True)
    
    # <h2 style='text-align: center;'>Aquí escribe un nombre creativo para presentar tu video</h2>: Esta es una cadena de código HTML.
    # La etiqueta <h2> se utiliza para un encabezado de segundo nivel en una página web.
    # El texto está centrado (text-align: center;).
    # El texto dentro de las etiquetas <h2> ("Aquí escribe un nombre creativo para presentar tu video") es el contenido del encabezado.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.
    # Por ejemplo, puedes agregar un emoji de video 🎥 

    # Agregamos un video realizado en las practicas anteriores
    st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E")

    # st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E"): Esta línea está mostrando un video en la aplicación web.
    # La función video toma como primer argumento la URL del video que se desea mostrar.
    # En este caso, la URL es "https://www.youtube.com/watch?v=X_Z7d04x9-E".
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.

    # O creamos un botón para ir al enlace del video con button
    st.markdown(f"<div style='text-align: center;'><a href='https://drive.google.com/file/d/1DW2CPiUE9YyIJKcj-UX-uL6APp8wuim5/view?usp=sharing' target='_blank'><button>Mi video PC1</button></a></div>", unsafe_allow_html=True) 
    st.markdown(f"<div style='text-align: center;'><a href='https://drive.google.com/file/d/1jhA_7SI3BQrz7TRb3wIIcg272MgB6rOW/view?usp=sharing' target='_blank'><button>Mi video PC2</button></a></div>", unsafe_allow_html=True) 

    # <div style='text-align: center;'><a href='https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link' target='_blank'><button>Ver video</button></a></div>:
    # Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el contenido está centrado (text-align: center;).
    # La etiqueta <a> se utiliza para crear un enlace.
    # El atributo href especifica la URL a la que se dirige el enlace.
    # En este caso, la URL es 'https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link'.
    # El atributo target='_blank' indica que el enlace se abrirá en una nueva pestaña del navegador.
    # La etiqueta <button> se utiliza para crear un botón.
    # El texto dentro de las etiquetas <button> ("Ver video") es el contenido del botón.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.
    
else:

    # Agregamos un título para la página de gráficos
    st.markdown("<h1 style='text-align: center;'>Mis primeros gráficos de muchos</h1>", unsafe_allow_html=True)

    # Creamos una lista de gráficos
    graficos = ['Gráfico de barras verticales de cantidad de idiomas por familia lingüística', 'Gráfico circular sobre distribución de películas y series', 'Mapa interactivo de familias lingüísticas por ubicación geográfica']

    # Creamos un cuadro de selección en la página de gráficos
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # El cuadro de selección se crea con la función selectbox.
    # El primer argumento es el texto que se muestra en el cuadro de selección.
    # El segundo argumento es una lista de opciones que se pueden seleccionar.
    # En este caso, las opciones son los elementos de la lista graficos.
    # La opción seleccionada se asigna a la variable grafico_seleccionado.
    # La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
    

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Gráfico de barras verticales de cantidad de idiomas por familia lingüística':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El gráfico de barras muestra que la familia quechua es la más representada, con 12 lenguas identificadas. Le sigue la familia arawak, con 9 lenguas, y luego la categoría NK (no clasificado), con 7 lenguas. El resto de familias lingüísticas, como Zaparoan, Harakmbut, Chicham, Jíbaro, Pano-Tacanan, Sechuran y otras, presentan entre 1 y 3 lenguas cada una. Este panorama refleja una distribución desigual, donde unas pocas familias concentran la mayor parte de las lenguas identificadas, mientras muchas otras están representadas por una sola lengua.</div>", unsafe_allow_html=True)
        st.image("imagen.png", caption='Gráfico de lenguas aisladas', width=500)
        pass
    elif grafico_seleccionado == 'Gráfico circular sobre distribución de películas y series':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>La distribución de contenido revela una predominancia clara de las películas, que representan el 69.6% del total, frente al 30.4% de las series. Esta desproporción evidencia una orientación marcada hacia el formato cinematográfico, lo cual podría responder a una estrategia de producción más ágil, menor compromiso de continuidad y una mayor facilidad de distribución global. A pesar del auge de las series en la era del streaming, el formato película sigue dominando ampliamente el catálogo.", unsafe_allow_html=True)
        st.image("grafico.png", caption='Gráfico de familias lingüísticas', width=500)
        pass
    elif grafico_seleccionado == 'Mapa interactivo de familias lingüísticas por ubicación geográfica':
        st.markdown("<div style='text-align: justify; font-size: 20px;'>El mapa muestra la distribución territorial de las lenguas indígenas según su familia lingüística. Cada marcador representa una lengua ubicada en el lugar donde se habla, e indica a qué familia pertenece. Al observar el mapa, se nota que las lenguas quechuas están concentradas principalmente en la zona andina, mientras que las lenguas de la familia arawak se extienden por regiones amazónicas. Familias con menos lenguas, como Harakmbut o Zaparoan, aparecen de forma más aislada, generalmente en puntos específicos de la selva. En conjunto, el mapa permite ver que la diversidad lingüística del Perú no solo es amplia, sino también geográficamente dispersa, y que cada familia tiene una distribución particular en el territorio.</div>", unsafe_allow_html=True)
        # Si "mapa_cusco.html" es un archivo HTML (no una imagen), debes mostrarlo con st.components.v1.html
        import streamlit.components.v1 as components
        with open("mapa_linguistico.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass

    # if grafico_seleccionado == 'Gráfico de barras verticales de lenguas aisladas':
    # st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
    # st.image("aisladas_base_datos.png", caption='Gráfico de lenguas aisladas', width=500): Esta línea está mostrando una imagen en la aplicación web.
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar.
    # En este caso, la imagen es "aisladas_base_datos.png".
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen,
    # en este caso "Gráfico de lenguas aisladas".
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 500 píxeles.

    # elif grafico_seleccionado == 'mapa_cusco':
    # import streamlit.components.v1 as components
    # with open("mapa_cusco.html", "r", encoding="utf-8") as f:
    #     html_content = f.read()
    # components.html(html_content, height=500): Esta línea está mostrando un archivo HTML en la aplicación web.
    # La función components.html toma como primer argumento el contenido HTML que se desea mostrar.
    # En este caso, el contenido HTML se lee desde el archivo "mapa_cusco.html".
    # El argumento height se utiliza para especificar la altura del contenido HTML, en este caso 500 píxeles.
    
    # Si no tenemos el archivo HTML, podemos agregar el código para crear el mapa de Cusco directamente en Streamlit.
    # Primero debes crear el diccionario de coordenadas del mapa de Cusco.
    # Luego debes crear el mapa utilizando la librería folium y streamlit-folium.
    # pip install folium
    # pip install streamlit-folium
        #import folium
        #from streamlit_folium import st_folium

        # Mostrar el mapa en Streamlit
        #st_folium(mapa_cusco, width=700, height=500)
    