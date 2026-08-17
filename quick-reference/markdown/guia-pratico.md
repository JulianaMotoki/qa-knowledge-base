# Markdown para GitHub

Este guia reúne as principais formatações do Markdown utilizadas no GitHub, com foco na criação de documentações técnicas.

<br>

# 1. Títulos

## Sintaxe

```md
# Título 1

## Título 2

### Título 3

#### Título 4

##### Título 5

###### Título 6
```

## Resultado

# Título 1

## Título 2

### Título 3

#### Título 4

##### Título 5

###### Título 6

<br>

# 2. Parágrafos e quebra de linha

## Novo parágrafo

```md
Primeiro parágrafo.

Segundo parágrafo.
```

Resultado:

Primeiro parágrafo.

Segundo parágrafo.

<br>

## Quebra de linha

Utilize `<br>`.

```md
Primeira linha.<br>
Segunda linha.
```

Resultado:

Primeira linha.<br>
Segunda linha.

<br>

# 3. Ênfase

## Sintaxe

```md
**Negrito**

*Itálico*

***Negrito e itálico***

~~Texto riscado~~

`Código`
```

## Resultado

**Negrito**

*Itálico*

***Negrito e itálico***

~~Texto riscado~~

`Código`

<br>

# 4. Listas

## Lista não ordenada

### Sintaxe

```md
- Item 1
- Item 2
  - Subitem
- Item 3
```

### Resultado

- Item 1
- Item 2
  - Subitem
- Item 3

<br>

## Lista ordenada

### Sintaxe

```md
1. Primeiro
2. Segundo
3. Terceiro
```

### Resultado

1. Primeiro
2. Segundo
3. Terceiro

<br>

## Checklist

### Sintaxe

```md
- [x] Concluído
- [ ] Pendente
```

### Resultado

- [x] Concluído
- [ ] Pendente

<br>

# 5. Links

## Sintaxe

```md
[GitHub](https://github.com)
```

## Resultado

[GitHub](https://github.com)

<br>

# 6. Imagens

## Imagem local

```md
![Logo](imagens/logo.png)
```

## Imagem externa

```md
![Logo](https://exemplo.com/logo.png)
```

<br>

# 7. Citações

## Sintaxe

```md
> Este é um texto em destaque.
```

## Resultado

> Este é um texto em destaque.

<br>

# 8. Alertas (Callouts)

Os alertas são suportados pelo GitHub e servem para destacar informações importantes.

## NOTE

### Sintaxe

```md
> [!NOTE]
> Informação importante.
```

### Resultado

> [!NOTE]
> Informação importante.

<br>

## TIP

### Sintaxe

```md
> [!TIP]
> Utilize Regex para agilizar alterações em massa.
```

### Resultado

> [!TIP]
> Utilize Regex para agilizar alterações em massa.

<br>

## IMPORTANT

### Sintaxe

```md
> [!IMPORTANT]
> Este procedimento deve ser seguido antes do deploy.
```

### Resultado

> [!IMPORTANT]
> Este procedimento deve ser seguido antes do deploy.

<br>

## WARNING

### Sintaxe

```md
> [!WARNING]
> Esta operação pode alterar diversos arquivos.
```

### Resultado

> [!WARNING]
> Esta operação pode alterar diversos arquivos.

<br>

## CAUTION

### Sintaxes

```md
> [!CAUTION]
> Esta ação não pode ser desfeita.
```

### Resultado

> [!CAUTION]
> Esta ação não pode ser desfeita.

<br>

# 9. Código

## Código em linha

### Sintaxe

```md
Use o comando `git status`.
```

### Resultado

Use o comando `git status`.

<br>

## Bloco de código

### Sintaxe

```md
```bash
git status
git add .
git commit -m "Atualização"
```
```

### Resultado

```bash
git status
git add .
git commit -m "Atualização"
```

<br>

# 10. Destaque de sintaxe

É possível informar a linguagem utilizada após as três crases para que o GitHub aplique o **syntax highlighting**.

## Bash

### Sintaxe

```md
```bash
git pull
```
```

### Resultado

```bash
git pull
```

<br>

## SQL

### Sintaxe

```md
```sql
SELECT * FROM usuarios;
```
```

### Resultado

```sql
SELECT * FROM usuarios;
```

<br>

## JSON

### Sintaxe

```md
```json
{
  "nome": "Juliana"
}
```
```

### Resultado

```json
{
  "nome": "Juliana"
}
```

<br>

## YAML

### Sintaxe

```md
```yaml
name: CI

on:
  push:
    branches:
      - main
```
```

### Resultado

```yaml
name: CI

on:
  push:
    branches:
      - main
```

<br>

## Python

### Sintaxe

```md
```python
print("Olá Mundo")
```
```

### Resultado

```python
print("Olá Mundo")
```

<br>

## Regex

### Sintaxe

```md
```regex
^\d+$
```
```

### Resultado

```regex
^\d+$
```

<br>

# 11. Tabelas

## Sintaxe

```md
| Ferramenta | Finalidade |
|------------|------------|
| Robot Framework | Automação |
| Postman | Testes de API |
| JMeter | Performance |
```

## Resultado

| Ferramenta | Finalidade |
|------------|------------|
| Robot Framework | Automação |
| Postman | Testes de API |
| JMeter | Performance |

<br>

# 12. Linha horizontal

## Sintaxe

```md
<br>
```

## Resultado

<br>

# 13. Comentários

Os comentários não aparecem após a renderização do Markdown.

## Sintaxe

```md
<!-- Este comentário não será exibido -->
```

<br>

# 14. Emojis

## Sintaxe

```md
✅ Concluído

❌ Erro

⚠️ Atenção

ℹ️ Informação

💡 Dica

🚀 Deploy realizado
```

## Resultado

✅ Concluído

❌ Erro

⚠️ Atenção

ℹ️ Informação

💡 Dica

🚀 Deploy realizado

<br>

# 15. Escapar caracteres especiais

Quando quiser exibir um caractere que possui significado especial no Markdown, utilize `\` antes dele.

## Sintaxe

```md
\*

\#

\`

\[
```

## Resultado

\*

\#

\`

\[

<br>

# 16. Misturando recursos

É possível combinar diferentes recursos do Markdown no mesmo conteúdo.

## Sintaxe

```md
> [!TIP]
> Utilize o comando `git status` antes de realizar um commit.
>
> Consulte também:
>
> - Fluxo de Git
> - Pull Request
> - GitHub Actions
```

## Resultado

> [!TIP]
> Utilize o comando `git status` antes de realizar um commit.
>
> Consulte também:
>
> - Fluxo de Git
> - Pull Request
> - GitHub Actions