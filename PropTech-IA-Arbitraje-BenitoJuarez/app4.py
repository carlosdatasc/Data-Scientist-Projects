import streamlit as st
import pandas as pd
import pydeck as pdk

# 1. Configuración de la página (Premium)
st.set_page_config(page_title="Inteligencia Artificial detección de Oportunidades", layout="wide")

# Estilo CSS Combinado (Mejora visual de métricas y tablas)
st.markdown("""
    <style>
    [data-testid="stMetricLabel"] { font-size: 16px !important; font-weight: bold !important; color: #4f4f4f !important; }
    [data-testid="stMetricValue"] { font-size: 28px !important; color: #1f77b4 !important; }
    [data-testid="stMetric"] { 
        background-color: #ffffff; border: 1px solid #e0e0e0; 
        padding: 15px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); 
    }
    .stDataFrame { border-radius: 10px; overflow: hidden; }
    </style>
    """, unsafe_allow_html=True)

# 2. Carga de datos (Triple Carga con Cache)
@st.cache_data
def load_all_data():
    # Master de predios
    df = pd.read_csv('./oportunidades_bj2_sample.csv')
    df['colonia'] = df['colonia'].str.strip()
    df['pct_formateado'] = df['pct_valor'] / 100
    
    # Carga de archivos de entorno con las correcciones de Lat/Lon ya aplicadas
    movilidad = pd.read_csv('./estaciones_cercanas_sample2.csv')
    amenidades = pd.read_csv('./amenidades_cercanas_opt_sample2.csv')
        
    return df, movilidad, amenidades

df_p, df_m, df_a = load_all_data()

# 3. Sidebar: Filtros Avanzados (Versión 1 + Versión 2)
st.sidebar.header(" Búsqueda Avanzada")

lista_colonias = sorted(df_p['colonia'].unique())
colonia_sel = st.sidebar.selectbox("Selecciona Colonia:", ['Todas'] + lista_colonias)

tipo_op = st.sidebar.radio(
    "Filtrar Oportunidades:",
    ['Todos', 'Infravalorados', 'Sobrevalorados']
)

# --- Aplicación de Filtros ---
df_f = df_p.copy()
if colonia_sel != "Todas":
    df_f = df_f[df_f['colonia'] == colonia_sel]

if tipo_op == "Infravalorados":
    df_f = df_f[df_f['pct_valor'] > 0]
elif tipo_op == 'Sobrevalorados':
    df_f = df_f[df_f['pct_valor'] < 0]



# 4. Títulos y Métricas Dinámicas (Estilo Versión 1)
st.title("Localizador de Oportunidades con IA")
st.subheader("Análisis de Valor y Entorno en Benito Juárez")

c1, c2, c3 = st.columns(3)
with c1: st.metric(label="Predios en zona", value=len(df_f))
with c2: st.metric(label="Plusvalía Media", value=f"{df_f['score_plusvalia'].mean():.1f} pts")
with c3: st.metric(label="Gap Promedio", value=f"{df_f['pct_formateado'].mean():.2f}%")

# 5. Tablero de Control Dinámico (Dataframe Seleccionable)
st.write('### Tablero de Control de Objetivos')
st.info(" Haz clic en una fila para realizar la auditoría geoespacial del predio.")

evento_seleccion = st.dataframe(
    df_f[['colonia', 'valor_suelo', 'valor_modelo', 'gap_valor', 'pct_formateado', 'score_plusvalia']],
    use_container_width=True,
    hide_index=False, 
    on_select="rerun", 
    selection_mode="single-row",
    column_config={
        "pct_formateado": st.column_config.NumberColumn("Gap %", format="%.2f%%"),
        "valor_suelo": st.column_config.NumberColumn("Valor Real ($)", format="$%d"),
        "valor_modelo": st.column_config.NumberColumn("Valor IA ($)", format="$%d"),
        "gap_valor": st.column_config.NumberColumn("Diferencia ($)", format="$%d"),
        "score_plusvalia": st.column_config.ProgressColumn("Plusvalía", min_value=0, max_value=100, format="%d pts")
    }
)

# 6. Lógica de Auditoría Detallada (Mapa Pro con Capas Combinadas)
if len(evento_seleccion.selection.rows) > 0:
    idx_seleccionado = evento_seleccion.selection.rows[0]
    id_real = df_f.index[idx_seleccionado]
    p = df_f.loc[id_real]
    
    st.divider()
    st.write(f"### Auditoría Geoespacial: Entorno del Predio ID {id_real}")
    
    entorno_m = df_m[df_m['id_predio'] == id_real]
    entorno_a = df_a[df_a['id_predio'] == id_real]

    # 1. Para Movilidad (Evita el error de concatenación)
    entorno_m = entorno_m.copy()
    entorno_m['label_principal'] = entorno_m['nombre_estacion'] # Mapeamos nombre_estacion a label_principal
    entorno_m['label_detalle'] = entorno_m.apply(
        lambda x: f"Sistema: {x['sistema']} | Línea: {x['linea']}".replace('nan', 'N/A'), axis=1
    )

    # 2. Para Amenidades
    entorno_a = entorno_a.copy()
    entorno_a['label_principal'] = entorno_a['nombre'] # Mapeamos nombre a label_principal
    entorno_a['label_detalle'] = entorno_a.apply(
        lambda x: f"Cat: {x['tipo_amenidad']} | Clase: {x['categoria']}".replace('nan', 'N/A'), axis=1
    )

    # 3. Para el Predio
    df_p_mapa = pd.DataFrame([p]).copy()
    df_p_mapa['label_principal'] = f"Predio ID: {id_real}" # Nombre específico para el predio
    df_p_mapa['label_detalle'] = f"Gap: {p['pct_valor']:.2f}% | Plusvalía: {int(p['score_plusvalia'])} pts"

    # --- Capas del Mapa ---
    
    # 1. El Objetivo (Rojo si sobrevalorado, Verde si infravalorado)
    color_predio = [255, 75, 75, 230] if p['pct_valor'] < 0 else [30, 200, 0, 230]
    layer_predio = pdk.Layer(
        "ScatterplotLayer",
        df_p_mapa,
        get_position=['longitud', 'latitud'],
        get_radius=40,
        get_fill_color=color_predio,
        pickable=True
    )

    # 2. Capa de Transporte (Cian Eléctrico)
    layer_movilidad = pdk.Layer(
        "ScatterplotLayer",
        entorno_m,
        get_position=['lon_estacion', 'lat_estacion'],
        get_radius=15,
        get_fill_color=[0, 255, 255, 255],
        pickable=True
    )

    # 3. Capa de Amenidades (Verde Esmeralda)
    layer_amenidades = pdk.Layer(
        "ScatterplotLayer",
        entorno_a,
        get_position=['Longitud', 'Latitud'],
        get_radius=15,
        get_fill_color=[34, 193, 114, 180],
        pickable=True
    )

    # Configuración de cámara centrada en el predio (Zoom Alto)
    view_state = pdk.ViewState(
        latitude=p['latitud'], 
        longitude=p['longitud'], 
        zoom=16.5, 
        pitch=45
    )

    st.pydeck_chart(pdk.Deck(
        layers=[layer_predio, layer_amenidades, layer_movilidad],
        initial_view_state=view_state,
        tooltip={
        "html": """
            <div style="font-family: sans-serif; font-size: 13px; color: white; padding: 5px;">
                <b style="font-size: 15px; color: #00ffcc;">{label_principal}</b><br/>
                <hr style="margin: 5px 0; border: 0.5px solid #666;">
                {label_detalle}
            </div>
        """,
        "style": {"backgroundColor": "#1e1e26", "color": "white", "border-radius": "8px"}
        }
    ))
    
    # Resumen de Auditoría en Columnas
    m1, m2 = st.columns(2)
    m1.success(f"Transporte Cercano: {len(entorno_m)} estaciones.")
    m2.success(f"Amenidades Proximidad: {len(entorno_a)} locales clave.")

else:
    # Vista General (Mapa tipo Versión 1)
    st.warning("Selecciona una propiedad en la tabla para auditar el entorno detallado.")
    
    view_general = pdk.ViewState(
        latitude=df_f['latitud'].mean() if not df_f.empty else 19.38,
        longitude=df_f['longitud'].mean() if not df_f.empty else -99.17,
        zoom=12.5,
        pitch=0
    )
    
    capa_general = pdk.Layer(
        "ScatterplotLayer",
        df_f,
        get_position=['longitud', 'latitud'],
        get_radius=20,
        get_fill_color='[30, 200, 0, 160]' if tipo_op != 'Sobrevalorados' else '[200, 30, 0, 160]',
        pickable=True,
        tooltip={
            "text": "Valor Real: ${valor_suelo}\nValor modelo: ${valor_modelo}\nDiferencia: ${gap_valor}\nGap: {pct_valor}"
        }
    )
    
    st.pydeck_chart(pdk.Deck(layers=[capa_general], initial_view_state=view_general))

st.caption("AI Hunter BJ v2.0 - Análisis de Valor de Suelo y Equipamiento Urbano.")