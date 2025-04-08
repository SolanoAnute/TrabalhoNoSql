from conexao import get_db  

def listar_jogadores():
    db = get_db()
    jogadores_collection = db["jogadores"]

    jogadores = list(jogadores_collection.find({}, {"_id": 0}))  # Remove o _id do MongoDB para evitar erro de conversão
    
    print("Jogadores cadastrados:")
    for jogador in jogadores:
        print(jogador)
    
    return jogadores

def contar_jogadores_por_posicao():
    db = get_db()
    jogadores_collection = db["jogadores"]
    
    pipeline = [
        {
            "$group": {
                "_id": "$Posicao_Origem",
                "total": {"$sum": 1},
                "jogadores": {"$push": "$Nome"}
            }
        }
    ]
    
    resultado = list(jogadores_collection.aggregate(pipeline))
    return resultado

    
    

def contar_jogadores_veteranos():
    db = get_db()
    jogadores_collection = db["jogadores"]
    
    pipeline = [
        {
            "$match": {
                "Data_Nascimento": {"$lte": "1990-12-31"}
            }
        },
        {
            "$group": {
                "_id": None,
                "total": {"$sum": 1},
                "jogadores": {
                    "$push": {
                        "Nome": "$Nome",
                        "Vigor_Fisico_Semana": "$saude.Vigor_Fisico_Semana"
                    }
                }
            }
        }
    ]
    
    resultado = list(jogadores_collection.aggregate(pipeline))
    return resultado

def analisar_jogadores_com_queixa():
    db = get_db()
    jogadores_collection = db["jogadores"]
    
    pipeline = [
        {
            "$facet": {
                "total_jogadores_com_queixa": [
                    {"$match": {"saude.Queixa_Problemas_Semana": {"$ne": "Nenhuma"}}},
                    {"$count": "total"}
                ],
                "jogadores_com_queixa_por_posicao": [
                    {"$match": {"saude.Queixa_Problemas_Semana": {"$ne": "Nenhuma"}}},
                    {
                        "$group": {
                            "_id": "$Posicao_Origem",
                            "total": {"$sum": 1}
                        }
                    }
                ],
                "jogadores_detalhados_por_posicao": [
                    {"$match": {"saude.Queixa_Problemas_Semana": {"$ne": "Nenhuma"}}},
                    {
                        "$group": {
                            "_id": "$Posicao_Origem",
                            "jogadores": {
                                "$push": {
                                    "Nome": "$Nome",
                                    "Queixa_Problemas_Semana": "$saude.Queixa_Problemas_Semana"
                                }
                            }
                        }
                    }
                ]
            }
        }
    ]
    
    resultado = list(jogadores_collection.aggregate(pipeline))
    return resultado


def listar_indices():
    db = get_db()
    jogadores_collection = db["jogadores"]
    indices = list(jogadores_collection.list_indexes())
    return indices
