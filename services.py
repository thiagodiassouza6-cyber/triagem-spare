def validar_fluxo_material(tipo_mat):
    """
    Define o destino e a mensagem com base no tipo de material.
    Retorna um dicionário com as configurações da interface.
    """
    fluxos = {
        "NLAG": {
            "status": "warning",
            "msg": "Materiais NLAG devem ser tratados via Nesflow (Governança Global).",
            "label": "Ir para Nesflow",
            "url": "https://link-do-seu-nesflow.com"
        },
        "ERSA": {  # Atualizado de ESA para ERSA
            "status": "success",
            "msg": "Código validado para a plataforma Sparetech.",
            "label": "Acessar Sparetech",
            "url": "https://link-da-sua-sparetech.com"
        },
        "UNBW": {  # Atualizado de NBW para UNBW
            "status": "success",
            "msg": "Código validado para a plataforma Sparetech.",
            "label": "Acessar Sparetech",
            "url": "https://link-da-sua-sparetech.com"
        }
    }
    return fluxos.get(tipo_mat, None)
