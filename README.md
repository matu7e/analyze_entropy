# Analyze Entropy

Este script permite analizar la entropía de los tokens JWT para verificar el cumplimiento de la especificación **ASVS V3.2.2**, que requiere una entropía mínima de 64 bits en los tokens de sesión. Se calcula la entropía de cada parte del token (header, payload y signature) y se proporciona un análisis detallado.

---

## Características

- Calcula la entropía de cada sección de un token JWT (header, payload y signature).
- Proporciona un cálculo de entropía total.
- Diseñado para validar el cumplimiento de estándares de seguridad.

---

## Requisitos

### Lenguaje
- **Python 3.6+**

### Librerías necesarias
El script utiliza las librerías estándar de Python. No es necesario instalar librerías externas.

---

## Instalación

1. Clona el repositorio o descarga el archivo `analyze_entropy.py`:
   ```bash
   git clone https://github.com/matu7e/analyze_entropy.git
   cd analyze_entropy
   ```

2. Asegúrate de tener Python instalado en tu sistema:
   ```bash
   python --version
   ```
   Si no lo tienes, puedes instalarlo desde [Python.org](https://www.python.org/downloads/).

3. Opcional: Activa un entorno virtual para aislar las dependencias del proyecto.
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Linux/Mac
   venv\Scripts\activate      # En Windows
   ```

---

## Uso

1. Abre el archivo `analyze_entropy.py` y edita la lista de tokens en el script:
   ```python
   tokens = [
       "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3Mzc0MDc3NTAsInN1YiI6I.........IiwiYXBlbGxpZG8iOiJHYWxhbnRpIiwiaW50cmFuZXQiOmZhbHNlfQ.vHITuLe93s9HWT84QPowlI1bjyANMwJXoRcnkIPPScQO........._F4nGg",
       # Agrega más tokens aquí...
   ]
   ```

2. Ejecuta el script en tu terminal:
   ```bash
   python analyze_entropy.py
   ```

3. Verás un análisis detallado en la consola con la entropía de cada sección del token, como este ejemplo:
   ```plaintext
   Token 1:
       Header Entropy: 3.85
       Payload Entropy: 4.22
       Signature Entropy: 5.67
       Total Entropy: 13.74
   ```

---

## Ejemplo de salida

Al ejecutar el script, se genera una salida como esta:

```plaintext
Token 1:
    Header Entropy: 3.85
    Payload Entropy: 4.22
    Signature Entropy: 5.67
    Total Entropy: 13.74

Token 2:
    Header Entropy: 3.72
    Payload Entropy: 4.11
    Signature Entropy: 5.80
    Total Entropy: 13.63

Error en el Token 3: list index out of range
```

---

## Notas importantes

1. **Validación de tokens**: El script no verifica la validez del token JWT ni decodifica datos cifrados. Solo analiza la entropía de los datos base64 codificados.
2. **Límite de entropía**: Un valor total de entropía inferior a 64 bits puede indicar un token inseguro.
3. **Manejo de errores**: Si un token no es válido, el script generará un mensaje de error indicando el problema.

---


