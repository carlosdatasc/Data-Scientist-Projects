# PropTech-IA: Arbitraje de Suelo e Inteligencia Inmobiliaria

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

##Visión General
Este proyecto es una herramienta de **Auditoría de Suelo y Arbitraje Inmobiliario** diseñada para detectar ineficiencias de mercado. Utiliza Ciencia de Datos para identificar el "Gap de Valor" entre el precio de mercado de un predio y su potencial real basado en infraestructura, movilidad y servicios.

**Área de Implementación actual:** CDMX (Escalando a Guanajuato).

##Características Técnicas
* **Procesamiento Masivo:** Pipeline de datos que integra +3M de registros del DENUE (INEGI) y capas de movilidad urbana.
* **Análisis Espacial:** Algoritmos de proximidad para calcular el impacto de servicios y transporte en la plusvalía.
* **Dashboard Interactivo:** Visualización geoespacial de alto rendimiento con PyDeck y Streamlit.
* **Auditoría UX:** Tooltips dinámicos en HTML para inspección de predios en tiempo real.

##Stack Tecnológico
* **Lenguaje:** Python
* **Data Stack:** Pandas, GeoPandas, Numpy
* **Visualización:** PyDeck, Streamlit, HTML/CSS
* **Optimización:** Manejo de datos mediante muestras representativas para despliegue eficiente.

##Valor de Negocio
A diferencia de los portales inmobiliarios tradicionales, este sistema permite:
1. **Detección de Arbitraje:** Localizar predios infravalorados por debajo de su valor algorítmico.
2. **Mitigación de Riesgo:** Validación del micro-entorno (amenidades y transporte) antes de la inversión.
3. **Optimización de Desarrollo:** Cruce de normatividad urbana con demanda de servicios cercana.

---
> **Nota técnica:** Esta versión pública utiliza un dataset de muestra para fines demostrativos. El motor de análisis real opera con bases de datos privadas de alta precisión para consultoría en desarrollo inmobiliario.

---
##Notas de Implementación y Confidencialidad

Este repositorio representa la arquitectura lógica y la interfaz de usuario del sistema. Por razones técnicas y estratégicas, se han aplicado los siguientes criterios:

1. **Gestión de Datos Masivos:** Los archivos fuente originales (Shapefiles de catastro y CSVs del DENUE con +500MB) superan los límites de almacenamiento de GitHub y han sido omitidos. El motor de producción local está optimizado para procesar estos volúmenes mediante técnicas de indexación espacial.
2. **Propiedad Intelectual:** La base de datos enriquecida y procesada es el activo principal de nuestra consultoría inmobiliaria. En la carpeta `/data` se incluye únicamente un **dataset de muestra (Dummy Data)** que permite validar la funcionalidad de los filtros, la reactividad del dashboard y la lógica de cruce de variables.
3. **Validación de Resultados:** La precisión del "Gap de Valor" y los mapas térmicos de plusvalía son totalmente operativos en el entorno de producción privado. 

**¿Deseas ver una demostración con datos reales de una zona específica?** Estaré compartiendo videos de funcionamiento real con el dataset completo en mis redes sociales, o puedes contactarme directamente para una sesión técnica.

*Desarrollado como una herramienta estratégica para consultoría privada y desarrollo inmobiliario.*