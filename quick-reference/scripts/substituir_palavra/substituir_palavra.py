# Código desenvolvido junto com IA
# A ideia inicial para a criaçao do código foi garantir o formato padrão do Gherkin,
# porém pode ser adaptado a inúmeras situações.

import re
from pathlib import Path

pasta_entrada = Path(input("Informe o caminho da pasta: "))
pasta_saida = pasta_entrada / "saida"

pasta_saida.mkdir(exist_ok=True)

substituicoes = {
    "Dado": "DADO",
    "Quando": "QUANDO",
    "Então": "ENTÃO",
    "E": "E",
    "Mas": "MAS"
}

for arquivo in pasta_entrada.glob("*.txt"):

    texto = arquivo.read_text(encoding="utf-8")

    for palavra, substituicao in substituicoes.items():
        # ^ = início da linha
        # \s* = permite espaços antes da palavra
        # \b = garante que é uma palavra inteira
        padrao = rf"^(\s*){re.escape(palavra)}\b"

        texto = re.sub(
            padrao,
            rf"\1{substituicao}",
            texto,
            flags=re.MULTILINE
        )

    arquivo_saida = pasta_saida / arquivo.name
    arquivo_saida.write_text(texto, encoding="utf-8")

    print(f"Processado: {arquivo.name}")

print("Concluído!")