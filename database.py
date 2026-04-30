import snowflake.connector
import streamlit as st

def get_snowflake_connection():
    """Gerencia a conexão com o Snowflake usando segredos do Streamlit."""
    try:
        return snowflake.connector.connect(
            user=st.secrets["snowflake"]["user"],
            password=st.secrets["snowflake"]["password"],
            account=st.secrets["snowflake"]["account"],
            warehouse=st.secrets["snowflake"]["warehouse"],
            database=st.secrets["snowflake"]["database"],
            schema=st.secrets["snowflake"]["schema"]
        )
    except Exception as e:
        st.error(f"Erro ao conectar ao Snowflake: {e}")
        return None

def fetch_material_type(material_id):
    """Executa a query e retorna o tipo do material."""
    conn = get_snowflake_connection()
    if not conn:
        return None
    
    try:
        with conn.cursor() as cur:
            query = "SELECT TIPO_MATERIAL FROM SUA_TABELA WHERE CODIGO_MATERIAL = %s"
            cur.execute(query, (material_id,))
            result = cur.fetchone()
            return result[0] if result else None
    finally:
        conn.close()
