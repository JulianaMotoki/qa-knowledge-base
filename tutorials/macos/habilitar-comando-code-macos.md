# Como habilitar o comando `code` no macOS

Este tutorial mostra como habilitar o comando `code` no Terminal para abrir projetos diretamente no Visual Studio Code.

> **Importante:** Antes de configurar o comando, verifique se o Visual Studio Code está instalado na pasta **Aplicativos** (`/Applications`). Caso contrário, mova o aplicativo para essa pasta antes de continuar.

---

## 1. Verifique se o Visual Studio Code está na pasta Aplicativos

1. Feche completamente o Visual Studio Code.
2. Abra o **Finder**.
3. Clique em **Aplicativos** no menu lateral.
4. Verifique se o **Visual Studio Code.app** está listado.

### Caso o Visual Studio Code não esteja em Aplicativos

1. No Finder, clique em **Downloads** (ou na pasta onde o aplicativo estiver).
2. Localize o **Visual Studio Code.app**.
3. Arraste o aplicativo para **Aplicativos** no menu lateral.

Se estiver utilizando o instalador (`.dmg`), basta arrastar o ícone do **Visual Studio Code** para o ícone **Applications**, conforme exibido na janela de instalação.

Depois, abra o Visual Studio Code diretamente pela pasta **Aplicativos** para confirmar que a instalação está correta.

---

## 2. Remova um atalho antigo (caso exista)

Abra o Terminal e execute:

```bash
sudo rm /usr/local/bin/code
```

> Será solicitada a senha do usuário administrador. Durante a digitação, nenhum caractere será exibido na tela. Esse é o comportamento esperado do Terminal.

Se o arquivo não existir, o Terminal poderá exibir uma mensagem informando que ele não foi encontrado. Nesse caso, prossiga normalmente para o próximo passo.

---

## 3. Crie o atalho para o comando `code`

Execute:

```bash
sudo ln -s "/Applications/Visual Studio Code.app/Contents/Resources/app/bin/code" /usr/local/bin/code
```

---

## 4. Atualize o cache de comandos do Terminal

```bash
hash -r
```

---

## 5. Teste a configuração

Verifique se o comando foi instalado corretamente:

```bash
code --version
```

Em seguida, navegue até qualquer pasta e execute:

```bash
code .
```

O ponto (`.`) representa a pasta atual do Terminal. Se tudo estiver configurado corretamente, o Visual Studio Code será aberto com essa pasta carregada.

---

## Solução alternativa

Caso prefira utilizar a configuração oficial do próprio Visual Studio Code:

1. Abra o Visual Studio Code.
2. Pressione **⌘ Command + Shift + P**.
3. Procure por **Shell Command: Install 'code' command in PATH**.
4. Execute a opção.
5. Feche e abra o Terminal novamente.
6. Teste o comando:

```bash
code .
```