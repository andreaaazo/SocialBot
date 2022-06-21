from contextlib import nullcontext
import sqlite3

class Database:
  def __init__(self) -> None:
    self.conn = sqlite3.connect('account.db')
    self.c = self.conn.cursor()
  

  def create_database(self):
    self.c.execute("""CREATE TABLE accounts (
		e_mail text,
    password text
		)""")

    # Commit our command
    self.conn.commit()

    self.c.execute("""CREATE TABLE posts (
		post_caption text,
    post_path text,
    post_hashtags text
		)""")

    # Commit commands
    self.conn.commit()


  def insertAccountInformations(self, email, password):
    self.c.execute("SELECT * FROM accounts")

    if not (email, password) in self.c.fetchall():  # Check if account is already inserted
      self.accountCommandString = "INSERT INTO accounts VALUES ('%s', '%s')" % (email, password)  # If not insert informations
      self.c.execute(self.accountCommandString)
      self.conn.commit()  # Submit

    else:
      return print("Account already stored")
    
    self.conn.commit()  # Submit


  def insertPostInformations(self, post_caption, post_path, post_hashtags):
    self.c.execute("SELECT * FROM posts")

    if not (post_caption, post_path, post_hashtags) in self.c.fetchall():  # Check if account is already inserted
      self.postCommandString = "INSERT INTO posts VALUES ('%s', '%s', '%s')" % (post_caption, post_path, post_hashtags)  # If not insert informations
      self.c.execute(self.postCommandString)
      self.conn.commit()  # Submit

    else:
      return print("Account already stored")
    
    self.conn.commit()  # Submit


if __name__ == '__main__':
  database = Database()
  database.insertAccountInformations('email@outlook.com', 'password')
  database.insertPostInformations('captionn', 'path', 'hashtags')