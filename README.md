# 📚 Home Library Manager 📚
A simple Python package to manage personal book collections. Track books, check them out to friends, and manage due dates.

##  Features
- 📌 **Add books** to your library
- ✅ **Check out books** to friends
- 🔄 **Return books** and track due dates
- 💸 **Automatically calculate fines**
- 🖥️ **Command-line interface for easy usage**

## 📦 Installation

```sh
git clone https://github.com/YOUR-USERNAME/home_library.git
cd home_library

pip install -r requirements.txt

pip install -e .
```

## Usage
Add a new book 
```
home-library add-book --title "1984" --author "George Orwell" --genre "Dystopian"
```
List all books
```
home-library list-books
```
Check out a book
```
home-library checkout --book_id 1 --user_id 2
```
Return a book
```
home-library return-book --book_id 1
```
Pay a fine
```
home-library pay-fine --user_id 2 --amount 5
```