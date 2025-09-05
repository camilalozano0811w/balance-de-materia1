import streamlit as st

def calculate_mass_balance(pulp_initial_mass, soluble_solids_initial_fraction, soluble_solids_final_fraction):
    """
    Calcula el balance de masa para un problema de dilución de pulpa.

    Args:
        pulp_initial_mass (float): Masa inicial de la pulpa (M1).
        soluble_solids_initial_fraction (float): Fracción de sólidos solubles iniciales (X1).
        soluble_solids_final_fraction (float): Fracción de sólidos solubles finales (X3).

    Returns:
        tuple: Una tupla que contiene la masa de la pulpa final (M3) y la masa de azúcar a agregar (M2).
    """
    # M1 * X1 + M2 * X2 = M3 * X3
    # M1 + M2 = M3
    # M2 * X2 = M3 * X3 - M1 * X1
    # M2 = M3 - M1
    # (M3 - M1) * X2 = M3 * X3 - M1 * X1
    # M3 * X2 - M1 * X2 = M3 * X3 - M1 * X1
    # M1 * X1 - M1 * X2 = M3 * X3 - M3 * X2
    # M1 * (X1 - X2) = M3 * (X3 - X2)
    # M3 = M1 * (X1 - X2) / (X3 - X2)

    # La fracción de sólidos en el azúcar puro (X2) es 1.0 (o 100%)
    x2 = 1.0

    # Evitar la división por cero
    if (soluble_solids_final_fraction - x2) == 0:
        return 0, 0

    # Balance de sólidos (para hallar M3)
    m3 = pulp_initial_mass * (soluble_solids_initial_fraction - x2) / (soluble_solids_final_fraction - x2)

    # Balance general (para hallar M2)
    m2 = m3 - pulp_initial_mass

    return m3, m2

# --- Configuración de la página de Streamlit ---
st.set_page_config(page_title="Balance de Masa de Pulpa", layout="centered", initial_sidebar_state="expanded")

# --- Encabezado y descripción ---
st.title("Calculadora de Balance de Masa de Pulpa")
st.markdown("Esta aplicación resuelve el problema del Ejercicio 1. Pulpa. ")
st.markdown("""
    Ingresa los valores de la masa inicial de la pulpa (M1), la fracción inicial de sólidos disueltos (X1) y la fracción final deseada (X3) para calcular la cantidad de azúcar (sólidos disueltos) que se debe agregar.
""")

# --- Controles de entrada de usuario ---
st.header("Valores de Entrada")

m1_input = st.number_input(
    "Masa de pulpa inicial (M1 en kg):",
    min_value=0.0,
    value=50.0,
    step=0.1,
    format="%.2f",
)

x1_input = st.number_input(
    "Fracción de sólidos inicial (X1):",
    min_value=0.0,
    max_value=1.0,
    value=0.07,
    step=0.01,
    format="%.2f",
)

x3_input = st.number_input(
    "Fracción de sólidos final (X3):",
    min_value=0.0,
    max_value=1.0,
    value=0.10,
    step=0.01,
    format="%.2f",
)

# --- Botón para realizar el cálculo ---
if st.button("Calcular"):
    if m1_input <= 0 or x1_input >= x3_input:
        st.error("Por favor, revisa los valores de entrada. La masa debe ser positiva y la fracción inicial de sólidos debe ser menor que la final.")
    else:
        # Realizar el cálculo
        m3_result, m2_result = calculate_mass_balance(m1_input, x1_input, x3_input)

        # Mostrar resultados
        st.success("¡Cálculo exitoso!")
        st.subheader("Resultados")
        st.info(f"Masa de la pulpa final (M3): **{m3_result:.2f} kg**")
        st.info(f"Masa de azúcar a agregar (M2): **{m2_result:.2f} kg**")

        st.markdown("---")
        st.subheader("Detalles del Balance de Masa")
        
        # Muestra las ecuaciones y valores para el usuario
        st.markdown(f"""
        - **Balance de Sólidos:** $M1 \cdot X1 + M2 \cdot X2 = M3 \cdot X3$
        - **Balance General:** $M1 + M2 = M3$

        A partir de la combinación de ecuaciones y sabiendo que $X2$ (fracción de sólidos en el azúcar puro) es $1.0$, se obtiene:

        $M3 = M1 \cdot \frac{{X1 - X2}}{{X3 - X2}} = {m1_input:.2f} \cdot \frac{{({x1_input:.2f} - 1.0)}}{{({x3_input:.2f} - 1.0)}} = {m3_result:.2f} \text{ kg}$

        $M2 = M3 - M1 = {m3_result:.2f} - {m1_input:.2f} = {m2_result:.2f} \text{ kg}$
        """)



