# Pruebas Unitarias de la API de Pokémon

**Autor:** Hansel Pérez (25-0461)

## Descripción

Este proyecto consiste en un conjunto de pruebas unitarias para la API de Pokémon, utilizando el marco de pruebas `pytest`. El objetivo de estas pruebas es verificar el correcto funcionamiento de la API en diferentes escenarios, asegurando que responde según lo esperado.

## Estructura del Proyecto

El archivo principal de pruebas es `pokemon_test.py`, donde se encuentran definidas seis funciones de prueba. Cada función está diseñada para evaluar un caso de uso específico de la API de Pokémon y está debidamente comentada para una mejor comprensión.

### Casos de Uso Implementados

Las pruebas realizadas en este proyecto cubren los siguientes casos de uso:

1. **Obtener información de un Pokémon válido**
   - Verifica que la API devuelva información correcta al solicitar un Pokémon existente (ejemplo: Pikachu).

2. **Buscar un Pokémon inexistente**
   - Confirma que la API devuelva un error 404 al buscar un Pokémon que no existe.

3. **Verificar el tipo de un Pokémon**
   - Asegura que un Pokémon tenga el tipo correcto (por ejemplo, Pikachu debe ser de tipo "electric").

4. **Verificar estadísticas base de un Pokémon**
   - Comprueba que un Pokémon tenga sus estadísticas base correctamente cargadas.

5. **Probar la velocidad de respuesta de la API**
   - Verifica que la API responda en un tiempo razonable (menos de 2 segundos).

6. **Obtener la lista de movimientos de un Pokémon**
   - Asegura que un Pokémon tenga al menos un movimiento disponible.

## Instalación

Para ejecutar las pruebas, necesitarás tener Python y `pytest` instalados en tu sistema. Puedes seguir los siguientes pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Hanzo02/Casos-de-uso.git
