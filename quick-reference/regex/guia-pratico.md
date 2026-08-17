# Guia Prático de Regex

Este documento reúne expressões regulares úteis para localizar, validar, formatar e manipular textos.

As expressões apresentadas seguem a sintaxe mais comum das Expressões Regulares (Regular Expressions - Regex), utilizada por diversas ferramentas, como:

- Editores de texto (VS Code, Notepad++, Sublime Text)
- Bancos de dados (PostgreSQL, Oracle, MySQL, entre outros)
- Linguagens de programação (Java, JavaScript, Python, C#, etc.)
- Ferramentas de automação
- Ferramentas de testes
- IDEs

> **Importante:** embora a sintaxe básica seja praticamente a mesma, alguns recursos podem variar entre ferramentas (como grupos de captura, lookaheads, lookbehinds e funções de substituição).

<br>

### 1. Exemplos de Regex
## 1.1 Linhas e quebras de linha

| O que faz | Regex (Localizar) | Substituir | Observação |
|-----------|-------------------|------------|------------|
| Remover linhas em branco | `^\s*$\r?\n` | Deixe vazio | Remove também linhas que possuem apenas espaços ou tabulações. |
| Identificar o ponto final da linha | `\.(?=\r?$)` | — | Encontra apenas o ponto localizado no final da linha. |
| Remover o ponto final da linha | `\.(?=\r?$)` | Deixe vazio | Remove apenas o ponto no final da linha. |
| Substituir o ponto final por vírgula | `\.(?=\r?$)` | `,` | Mantém o restante da linha. |
| Adicionar vírgula ao final da linha | `(?=\r?$)` | `,` | Adiciona uma vírgula ao final de cada linha. |
| Adicionar ponto e vírgula ao final da linha | `(?=\r?$)` | `;` | Adiciona um ponto e vírgula ao final de cada linha. |
| Adicionar vírgula apenas em linhas com conteúdo | `^(.+?)(?=\r?$)` | `$1,` | Ignora linhas vazias. |
| Remover espaços no início da linha | `^[ \t]+` | Deixe vazio | Remove espaços e tabulações no início da linha. |
| Remover espaços no final da linha | `[ \t]+(?=\r?$)` | Deixe vazio | Remove espaços e tabulações no final da linha. |

<br>

## 1.2 Documentos (CPF e CNPJ)

| O que faz | Regex (Localizar) | Substituir | Observação |
|-----------|-------------------|------------|------------|
| Formatar CPF | `\b(\d{3})(\d{3})(\d{3})(\d{2})\b` | `$1.$2.$3-$4` | Converte `12345678901` em `123.456.789-01`. |
| Remover formatação do CPF | `\b(\d{3})\.(\d{3})\.(\d{3})-(\d{2})\b` | `$1$2$3$4` | Remove pontos e hífen. |
| Identificar CPF formatado | `\b\d{3}\.\d{3}\.\d{3}-\d{2}\b` | — | Apenas identifica. |
| Identificar CPF sem formatação | `\b\d{11}\b` | — | Apenas identifica. |
| Formatar CNPJ numérico | `\b(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})\b` | `$1.$2.$3/$4-$5` | Converte `12345678000190` em `12.345.678/0001-90`. |
| Remover formatação do CNPJ numérico | `\b(\d{2})\.(\d{3})\.(\d{3})\/(\d{4})-(\d{2})\b` | `$1$2$3$4$5` | Remove pontos, barra e hífen. |
| Identificar CNPJ numérico formatado | `\b\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}\b` | — | Apenas identifica. |
| Identificar CNPJ numérico sem formatação | `\b\d{14}\b` | — | Apenas identifica. |
| Formatar CNPJ alfanumérico | `\b([A-Z0-9]{2})([A-Z0-9]{3})([A-Z0-9]{3})([A-Z0-9]{4})(\d{2})\b` | `$1.$2.$3/$4-$5` | Converte um CNPJ alfanumérico sem formatação para o padrão `XX.XXX.XXX/XXXX-00`. |
| Remover formatação do CNPJ alfanumérico | `\b([A-Z0-9]{2})\.([A-Z0-9]{3})\.([A-Z0-9]{3})\/([A-Z0-9]{4})-(\d{2})\b` | `$1$2$3$4$5` | Remove pontos, barra e hífen. |
| Identificar CNPJ alfanumérico formatado | `\b[A-Z0-9]{2}\.[A-Z0-9]{3}\.[A-Z0-9]{3}\/[A-Z0-9]{4}-\d{2}\b` | — | Apenas identifica. |
| Identificar CNPJ alfanumérico sem formatação | `\b[A-Z0-9]{12}\d{2}\b` | — | Apenas identifica. |

<br>

## 1.3 Organização de textos

| O que faz | Regex (Localizar) | Substituir | Observação |
|-----------|-------------------|------------|------------|
| Remover espaços duplicados | `[ \t]{2,}` | Um único espaço | Substitui múltiplos espaços ou tabulações por um único espaço. |
| Remover linhas que possuem apenas espaços | `^[ \t]+$\r?\n?` | Deixe vazio | Remove linhas que contêm apenas espaços ou tabulações. |
| Remover linhas duplicadas consecutivas | `^(.*)(\r?\n\1)+$` | `$1` | Mantém apenas a primeira ocorrência de linhas repetidas consecutivamente. |
| Encontrar linhas que começam com um texto | `^Erro.*` | — | Encontra linhas iniciadas com "Erro". |
| Encontrar linhas que terminam com um texto | `.*concluído\r?$` | — | Encontra linhas finalizadas com "concluído". |
| Encontrar linhas que contenham determinada palavra | `^.*\bfalha\b.*$` | — | Encontra linhas que contenham a palavra "falha". |
| Remover um prefixo | `^Item:\s*` | Deixe vazio | Remove o prefixo `Item:` do início da linha. |

<br>

## 1.4 Manipulação de listas

| O que faz | Regex (Localizar) | Substituir | Observação |
|-----------|-------------------|------------|------------|
| Colocar aspas em cada linha | `^(.+?)(?=\r?$)` | `"$1"` | Envolve cada linha com aspas duplas. |
| Colocar aspas e vírgula | `^(.+?)(?=\r?$)` | `"$1",` | Útil para criar listas em JSON ou JavaScript. |
| Transformar lista em valores SQL | `^(.+?)(?=\r?$)` | `'$1',` | Útil para montar cláusulas `IN` em SQL. |
| Remover a última vírgula de uma lista | `,(?=\s*$)` | Deixe vazio | Remove apenas a última vírgula da seleção ou do texto. |

<br>

## 1.5 Identificação de dados

| O que faz | Regex (Localizar) | Substituir | Observação |
|-----------|-------------------|------------|------------|
| Encontrar e-mails | `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b` | — | Identifica endereços de e-mail. |
| Encontrar URLs | `https?:\/\/[^\s]+` | — | Identifica URLs iniciadas por `http://` ou `https://`. |
| Encontrar números | `\d+` | — | Encontra sequências de um ou mais números. |
| Encontrar linhas compostas apenas por números | `^\d+\r?$` | — | Encontra linhas que possuem somente números. |
| Encontrar texto entre aspas | `"[^"]*"` | — | Encontra todo o conteúdo entre aspas duplas. |
| Encontrar texto entre parênteses | `\([^)]*\)` | — | Encontra todo o conteúdo entre parênteses. |

<br>

## 1.6 Logs

| O que faz | Regex (Localizar) | Substituir | Observação |
|-----------|-------------------|------------|------------|
| Encontrar linhas com ERROR | `^.*\bERROR\b.*$` | — | Encontra linhas que contenham a palavra `ERROR`. |
| Encontrar linhas com ERROR ou FAIL | `^.*\b(?:ERROR\|FAIL)\b.*$` | — | Encontra linhas que contenham `ERROR` ou `FAIL`. |
| Encontrar códigos HTTP 4xx | `\b4\d{2}\b` | — | Identifica códigos HTTP de erro do cliente (400–499). |
| Encontrar códigos HTTP 5xx | `\b5\d{2}\b` | — | Identifica códigos HTTP de erro do servidor (500–599). |
| Encontrar UUID | `\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\b` | — | Identifica UUIDs no formato padrão (versões 1 a 5). |

<br>

## 1.7 Outros
| O que faz | Regex (Localizar) | Substituir | Observação |
|-----------|-------------------|------------|------------|
| Encontrar um texto específico único em uma linha | `^---$` | `<br>` | Só vai encontrar se ele for único na linha |
| Encontrar um texto específico | `(?<!-)---(?!-)` | `xpto` | Vai diferenciar `---` de `----` ou qualquer outra variação |

<br>

## 2. Principais símbolos

| Símbolo | Significado |
|---------|-------------|
| `^` | Início da linha |
| `$` | Final da linha |
| `.` | Qualquer caractere |
| `\.` | Ponto literal |
| `\d` | Número |
| `\D` | Não número |
| `\s` | Espaço em branco |
| `\S` | Não espaço |
| `\w` | Letra, número ou `_` |
| `\W` | Qualquer caractere que não seja letra, número ou `_` |
| `\b` | Limite de palavra |
| `*` | Zero ou mais ocorrências |
| `+` | Uma ou mais ocorrências |
| `?` | Zero ou uma ocorrência |
| `{n}` | Exatamente n ocorrências |
| `{n,m}` | Entre n e m ocorrências |
| `[abc]` | Um dos caracteres informados |
| `[^abc]` | Qualquer caractere exceto os informados |
| `( )` | Grupo de captura |
| `(?: )` | Grupo sem captura |
| `\|` | Operador "ou" |
| `$1`, `$2` | Referência aos grupos capturados (a sintaxe pode variar conforme a ferramenta) |

<br>

# 3. Observações

- Regex normalmente valida apenas o **formato** de uma informação.
- A sintaxe de substituição (`$1`, `\1`, etc.) pode variar conforme a ferramenta utilizada.
- Alguns recursos, como **lookbehind**, **lookahead** e determinados metacaracteres, podem não estar disponíveis em todos os mecanismos de Regex.
- Sempre consulte a documentação da ferramenta caso uma expressão não funcione exatamente como esperado.