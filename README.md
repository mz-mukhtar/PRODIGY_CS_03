# Password complexity Checker

This project is part of my Prodigy interniship program, which is building a simple python-based command-line tool to check the strength of passwords

## Fetures


- Input is hidden while typing (for security)
- Evaluates password based on:
  - Length (minimum 8 characters)
  - Presence of lowercase letters
  - Presence of uppercase letters
  - Inclusion of numbers
  - Use of special characters
- Provides:
  - A score (out of 5)
  - A strength label: **Weak**, **Moderate**, or **Strong**
  - Personalized improvement suggestions

## Future Enhancemets
- Check against common password dictionary
- Random strong password generator (--generate flag)


## Installation

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/mz-mukhtar/PRODIGY_CS_03.git
cd PRODIGY_CS_03
```
- Make sure you have python 3.x installed. you can check that by using the following comand
```bash
python --version
```
or, if you are on linux, it might refer python to python 2. So use

```bash
python3 --version
```
## How to use
```bash 
python checker.py
```
or, if you are using python 3specifically: 

```bash
python3 checker.py
```
## Example Output
Welcome to the Password Complexity Checker!

Enter your password: ********

Analyzing password...

		Length is 8+ characters

		Missing lowercase letter

		Contains uppercase letter

		Contains digit

		Missing special character

	Score: 3/5

	Strength: Moderate

 Suggestions to improve:
- Add some lowercase letters (a–z)
- Use special characters (!@#$ etc.)

