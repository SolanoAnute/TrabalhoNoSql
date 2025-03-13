from pydantic import BaseModel
from typing import List, Optional

class Saude(BaseModel):
    Vigor_Fisico_Semana: str
    Queixa_Problemas_Semana: Optional[str] = None
    Condicao_Jogo_Semana: str
    Capacidade_Jogo: str
    Status_Tratamento_Lesao: Optional[str] = None

class Jogador(BaseModel):
    ID: int
    Nome: str
    Data_Nascimento: str
    Posicao_Origem: str
    Posicoes_Complementares: List[str]
    Tempo_Jogado_Semana: int
    saude: Saude
