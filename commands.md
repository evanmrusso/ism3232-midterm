## 1. Building the project

```bash
cd
pwd
mkdir ism3232_midterm
cd ~/ism3232_midterm
pwd
code .
python3 -m venv .venv
source .venv/bin/activate
which python3
pip install pytest
pip install ruff
pip freeze > requirements.txt
echo '.venv' > .gitgnore
echo '__pycache__/' >> .gitignore
echo '*.pyc' >> .gitignore
touch business_rules.py main.py commands.md README.md
mkdir -p tests && touch tests/__init__.py tests/test_business_rules.py
git init
git commit -m 'Midterm setup'
git branch -M main
git remote add origin https://github.com/evanmrusso/ism3232-midterm.git
git push -u origin main
git add .
git commit -m 'Midterm setup'
git push -u origin main
git push -u origin main
git check-ignore .venv/ __pycache__/
git add .
git commit -m "Fix gitignore and remove misspelled file"
git push
printf ".venv/\n__pycache__/\n*.pyc\n" > .gitignore
rm -i .gitgnore
git check-ignore .venv/ __pycache__/
git add .
git commit -m "Fix gitignore and remove misspelled file"
git push
git status
```

## 2. The virtual environment

```bash
which python3
```

```text
/home/evanm/ism3232_midterm/.venv/bin/python3
```

The `.venv/bin/python3` portion of the output shows that Python is running from my project’s virtual environment.

## 3. The project structure

```bash
tree -L 2
```

```text
.
├── README.md
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    └── test_business_rules.py

2 directories, 7 files
```

The `.venv` folder exists on my computer but is not in my GitHub repository because `.gitignore` excludes it from Git tracking.