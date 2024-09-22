# sensosoft_ai
# Sensosoft AI - Sistema de Evaluación Sensorial de Cervezas Artesanales

**Sensosoft AI** es una aplicación web diseñada para la cervecería de la Universidad Santiago de Cali (USC), que permite realizar un análisis sensorial detallado de cervezas artesanales. El sistema está dirigido a operarios de producción, coordinadores de calidad y administradores, proporcionando herramientas para capturar, gestionar y analizar datos relacionados con el aroma, sabor, color y textura de las cervezas, con el objetivo de mejorar la calidad del producto y optimizar el proceso de producción.

## Características principales

- **Captura de datos sensoriales**: Los operarios de producción pueden ingresar información sobre las características sensoriales de las cervezas mediante un formulario intuitivo.
- **Análisis de datos**: Los coordinadores de calidad pueden visualizar y exportar reportes detallados de los resultados sensoriales para tomar decisiones informadas.
- **Gestión de usuarios y roles**: Los administradores tienen la capacidad de gestionar los perfiles de usuario, asignar roles y controlar el acceso a diferentes funcionalidades del sistema.
- **Validaciones personalizadas**: El sistema incluye validaciones para garantizar que los datos capturados cumplan con ciertos criterios de calidad, como los colores válidos para las cervezas.
  
## Estructura del proyecto

El proyecto sigue la arquitectura **Model-Template-View (MTV)** de Django, que facilita el desarrollo y la organización del código:
- **Models**: Definición de las tablas de la base de datos (como la clase `Cerveza`), que representan los datos sensoriales capturados.
- **Templates**: Plantillas HTML para la interfaz de usuario, renderizadas con los datos proporcionados por las vistas.
- **Views**: Lógica de negocio que controla la captura y presentación de los datos sensoriales.

Este proyecto utiliza **Django** como framework principal y está pensado para crecer con la incorporación de nuevas funcionalidades, como análisis avanzados basados en IA y generación de reportes automáticos.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/usuario/sensosoft_ai.git
   cd sensosoft_ai
