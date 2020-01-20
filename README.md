# manage_minyan
Auto generate weekly emails for Sabbath Prayer group

## Setup Repo with asdf and poetry
- Install asdf

```bash
brew install asdf
```

- Install `poetry`

```bash
curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
```

Add the following lines to `~/.bashrc`:

```bash
# poetry
source $HOME/.poetry/env
```

Add the following lines to `~/.bash_profile`:

```bash
# asdf
. $HOME/.asdf/asdf.sh
. $HOME/.asdf/completions/asdf.bash

# poetry
source $HOME/.poetry/env
export PATH="$HOME/.poetry/bin:$PATH"
```

- Add python asdf plugin and install python 3.7.4
```bash
asdf plugin-add python
asdf install python 3.7.4
```

Restart your terminal.
