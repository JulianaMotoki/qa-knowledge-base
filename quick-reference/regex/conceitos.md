# Conceitos Intermediários de Regex

## 1. Grupos de captura

São partes da expressão colocadas entre parênteses `()`.

Eles "guardam" um trecho encontrado para que ele possa ser reutilizado depois, normalmente em uma substituição.

**Exemplo**

```regex
(\d{3})(\d{2})
```

Texto:

```text
12345
```

Grupos capturados:

- Grupo 1 → `123`
- Grupo 2 → `45`

---

## 2. Lookahead

O Lookahead verifica o que vem **depois** do texto encontrado, mas essa parte **não é incluída** no resultado.

Pense como:

> "Encontre isto, somente se depois existir aquilo."

**Exemplo**

```regex
arquivo(?=\.txt)
```

Encontra:

```text
arquivo
```

em:

```text
arquivo.txt
```

---

## 3. Lookbehind

O Lookbehind verifica o que vem **antes** do texto encontrado, mas essa parte **não é incluída** no resultado.

Pense como:

> "Encontre isto, somente se antes existir aquilo."

**Exemplo**

```regex
(?<=R\$ )\d+
```

Encontra:

```text
100
```

em:

```text
R$ 100
```

---

## 4. Funções de substituição

São recursos usados para montar um novo texto utilizando os grupos capturados.

A sintaxe varia conforme a ferramenta (`$1`, `\1`, etc.).

**Exemplo**

Regex:

```regex
(\d{3})(\d{3})(\d{3})(\d{2})
```

Substituição:

```text
$1.$2.$3-$4
```

Resultado:

```text
123.456.789-01
```