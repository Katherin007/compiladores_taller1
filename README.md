# compiladores_taller1
# **ANÁLISIS COMPARATIVO: C++ VS. PYTHON EN RENDIMIENTO Y MANEJO DE ERRORES**

---

## **1. Rendimiento y Velocidad de Ejecución (Punto 1)** ⏱️

| Lenguaje | Tiempo de Ejecución (Reportado) |
| :---: | :---: |
| **C++** | $114,718 \text{ microsegundos}$ |
| **Python** | $102 \text{ microsegundos}$ |

Aunque en Python fue más rápido, **debería de C++ ser mucho más rápido** ya que compila a código máquina nativo y no tiene la sobrecarga del intérprete, lo que le permite ejecutar bucles y operaciones básicas en una fracción de segundo. La mayor parte del tiempo transcurrido provendría de la operación de entrada/salida (imprimir en la consola).

En este caso Python fue mucho más rápido por la razón de que en C++ **el sistema midió el tiempo de toda la ejecución del programa**, incluyendo el tiempo que tardó el sistema operativo en **cargar el archivo ejecutable** de C++ y configurar la consola para la salida.

---

## **2. Detección y Solución de Errores (Punto 2)** 🛠️

### **2.1. Consecuencias del Error**

| Lenguaje | Resultado del Error |
| :---: | :--- |
| **C++** | El programa **no se compila**. El proceso de compilación se detuvo tan pronto como el compilador encontró la línea defectuosa. **No crea el archivo ejecutable**. |
| **Python** | Al intentar ejecutar este código, Python se detuvo inmediatamente en la línea del error y **termina el programa**. |

### **2.2. Detección Temporal del Error**

| Lenguaje | Momento de Detección |
| :---: | :--- |
| **Python** | Justo **antes de la ejecución**. Intenta ejecutar línea por línea y al no encontrar la sintaxis esperada falla. |
| **C++** | El error se detecta durante el **tiempo de compilación (*compile time*)**. Es el compilador el que analiza el código antes de intentar generar el ejecutable. |

### **2.3. Mensajes de Error Generados**

| Lenguaje | Mensaje de Error (Típico) |
| :---: | :--- |
| **Python** | `SyntaxError: expected ':'` |
| **C++** | `error: lvalue required as left operand of assignment` |

### **2.4. Interpretación y Corrección de Errores**

#### **Corrección en Python:**

* **Interpretación:** El programador debe entender que en Python, todas las declaraciones de control de flujo (`if`, `for`, `while`, etc.) deben terminar con **dos puntos (`:`)**.
* **Corrección:** Agregar los dos puntos y la indentación correcta (que en Python es obligatoria).

python
# Corrección de Sintaxis: Se añade ':'
if numero % 2 == 0: 
    print("El número es par")

### Corrección en C++:

* **Interpretación:** El programador debe reconocer que el operador de **asignación** (`=`) intenta cambiar el valor de una variable, mientras que el operador de **comparación** (`==`) se usa para verificar si dos valores son iguales. Una condición `if` siempre requiere una comparación.

* **Corrección:** Reemplazar el signo de asignación con el operador de igualdad.

cpp
// Corrección de Semántica: Se cambia '=' por '=='
if (numero % 2 == 0) { 
    cout << "El numero es par" << endl; 
}
