# Setup

Install `uv`:

```bash
pip install uv
```

Install `specify-cli` from `spec-kit`:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

## Windows PATH

If `uv` or `specify` is not recognized, add the `uv` tool bin folder to your user PATH:

```powershell
setx PATH "$env:PATH;$env:USERPROFILE\.local\bin"
```

Then close and reopen your terminal.
