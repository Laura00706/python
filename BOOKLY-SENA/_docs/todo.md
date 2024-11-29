```
py -m venv .venv

.venv\scripts\activate

where.exe python

py -m pip install --upgrade pip

git init

```

- crear .gitignore -> burcar github .gitignore for fastapi (incluir .venv)

```
pip install "fastapi[standard]"

```

- crear requirements.txt

```
pip freeze > requirements.txt

pip install -r requirements.txt

```

- lista

 /books - get
 /books - post
 /book /[book_id] - patch
 /book/[book_id] -delete