# Fluxo básico de Git e GitHub

## 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
```

Clona o repositório para a máquina local.

---

## 2. Entrar na pasta do projeto

```bash
cd qa-knowledge-base
```

Acessa a pasta do projeto.

---

## 3. Atualizar a branch principal

```bash
git switch main
git pull origin main
```

Garante que a `main` esteja atualizada antes de iniciar uma nova alteração.

---

## 4. Criar uma nova branch

### 4.1 Opção 1
```bash
git switch -c nome-da-branch
```

Cria uma nova branch e já muda para ela.

### 4.2 Opção 2
```bash
git branch nome-da-branch
```
Cria uma nova branch

```bash
git checkout nome-da-branch
```
Muda para a branch criada



---

## 5. Fazer as alterações

Crie, edite ou exclua os arquivos necessários.

---

## 6. Verificar as alterações

```bash
git status
```

Mostra os arquivos modificados, criados ou removidos.

---

## 7. Adicionar as alterações

### 7.1 Opção 1
```bash
git add -A
```

Adiciona todas as alterações para o próximo commit.

### 7.2 Opção 2
```bash
git add README.md
```
```bash
git add docs/guia-git-github.md
```
Cada comando é para adicionar um arquivo por vez para o próximo commit. 


---

## 8. Conferir novamente

```bash
git status
```

Verifica se todos os arquivos esperados foram adicionados.

---

## 9. Criar o commit

```bash
git commit -m "Cria estrutura inicial do repositório"
```

Salva as alterações no histórico local.

---

## 10. Enviar a branch para o GitHub

```bash
git push -u origin nome-da-branch
```

Envia a branch para o GitHub.

> O parâmetro `-u` precisa ser usado apenas no primeiro `push` da branch.

Depois disso, basta utilizar:

```bash
git push
```

---

## 11. Criar o Pull Request

Pelo GitHub:

- Abra o repositório.
- Clique em **Compare & Pull Request**.
- Revise as alterações.
- Clique em **Create Pull Request**.

Ou pelo terminal:

```bash
gh pr create --web
```

---

## 12. Após o merge

Volte para a `main`:

```bash
git switch main
```

Atualize a `main`:

```bash
git pull origin main
```

Remova a branch local:

```bash
git branch -d nome-da-branch
```

---

# Comandos úteis

## Ver em qual branch está

```bash
git branch
```

ou

```bash
git status
```

---

## Trocar de branch

```bash
git switch nome-da-branch
```

Exemplo:

```bash
git switch main
```

