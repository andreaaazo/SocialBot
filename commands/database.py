import sqlite3
from tokenize import String

from traitlets import Int


class Database:
    def __init__(self) -> None:
        self.conn = sqlite3.connect("accounts.db")
        self.c = self.conn.cursor()

    def create_database(self):
        # It creates a table for Instagram accounts
        self.c.execute(
            """CREATE TABLE instagram_accounts (
		account_num integer,
    e_mail text,
    password text
		)"""
        )
        self.conn.commit()

        # It creates a table for TikTok accounts
        self.c.execute(
            """CREATE TABLE tiktok_accounts (
		account_num integer,
    e_mail text,
    password text
		)"""
        )
        self.conn.commit()

        # It creates a table for Instagram posts
        self.c.execute(
            """CREATE TABLE instagram_posts(
    account_num integer,
    post_caption text,
    post_path text,
    post_hashtags text
    )"""
        )
        self.conn.commit()

        # It creates a table for TikTok posts
        self.c.execute(
            """CREATE TABLE tiktok_posts(
      account_num int,
      post_caption text,
      post_path text,
      post_hashtags text
    )"""
        )
        self.conn.commit()

    def send_instagram_credentials(
        self, account_num: Int, e_mail: String, password: String
    ):
        self.c.execute(
            "SELECT * FROM instagram_accounts WHERE account_num = :account_num",
            {"account_num": account_num},
        )  # Takes all the values from account_num
        self.conn.commit()

        if (
            len(self.c.fetchall()) != 0
        ):  # Checking if credentials are already saved. If TRUE replace the old values.
            self.c.execute(
                "UPDATE instagram_accounts SET e_mail = :e_mail, password = :password WHERE account_num = :account_num",
                {"account_num": account_num, "e_mail": e_mail, "password": password},
            )  # Update old credentials with new credentials
            self.conn.commit()
            return "Instagram credentials updated"  # Return a string
        else:
            self.c.execute(
                "INSERT INTO instagram_accounts VALUES (?, ?, ?)",
                (account_num, e_mail, password),
            )  # Insert new credentials
            self.conn.commit()
            return "Instagram credentials added"  # Return a string

    def send_tiktok_credentials(
        self, account_num: Int, e_mail: String, password: String
    ):
        self.c.execute(
            "SELECT * FROM tiktok_accounts WHERE account_num = :account_num",
            {"account_num": account_num},
        )  # It receives all the values from account_num
        self.conn.commit()

        if (
            len(self.c.fetchall()) != 0
        ):  # Checking if credentials are already saved. If TRUE replace the old values.
            self.c.execute(
                "UPDATE tiktok_accounts SET e_mail = :e_mail, password = :password WHERE account_num = :account_num",
                {"account_num": account_num, "e_mail": e_mail, "password": password},
            )  # Update old credentials with new credentials
            self.conn.commit()
            return "TikTok credentials updated"  # Return a string
        else:
            self.c.execute(
                "INSERT INTO tiktok_accounts VALUES (?, ?, ?)",
                (account_num, e_mail, password),
            )  # Insert new credentials
            self.conn.commit()
            return "TikTok credentials added"  # Return a string

    def send_instagram_post(
        self,
        account_num: Int,
        post_caption: String,
        post_path: String,
        post_hashtags: String,
    ):
        self.c.execute(
            "SELECT * FROM instagram_posts WHERE account_num = :account_num",
            {"account_num": account_num},
        )  # Fetch post data
        self.conn.commit()

        if (
            len(self.c.fetchall()) != 0
        ):  # Check if post credentials are already saved. If TRUE update old values
            self.c.execute(
                "UPDATE instagram_posts SET post_caption = :post_caption, post_path = :post_path, post_hashtags = :post_hashtags WHERE account_num = :account_num",
                {
                    "account_num": account_num,
                    "post_caption": post_caption,
                    "post_path": post_path,
                    "post_hashtags": post_hashtags,
                },
            )
            self.conn.commit()
            return "Instagram post updated"  # Return a string
        else:
            self.c.execute(
                "INSERT INTO instagram_posts VALUES (?, ?, ?, ?)",
                (account_num, post_caption, post_path, post_hashtags),
            )  # Insert new credentials
            self.conn.commit()
            return "Instagram post added"  # Return a string

    def send_tiktok_post(
        self,
        account_num: Int,
        post_caption: String,
        post_path: String,
        post_hashtags: String,
    ):
        self.c.execute(
            "SELECT * FROM tiktok_posts WHERE account_num = :account_num",
            {"account_num": account_num},
        )  # Fetch post data
        self.conn.commit()

        if (
            len(self.c.fetchall()) != 0
        ):  # Check if post credentials are already saved. If TRUE update old values
            self.c.execute(
                "UPDATE tiktok_posts SET post_caption = :post_caption, post_path = :post_path, post_hashtags = :posthashtags WHERE account_num = :account_num",
                {
                    "account_num": account_num,
                    "post_caption": post_caption,
                    "post_path": post_path,
                    "post_hashtags": post_hashtags,
                },
            )  # Update old values with new values
            self.conn.commit()
            return "Instagram post updated"  # Return a string
        else:
            self.c.execute(
                "INSERT INTO tiktok_posts VALUES (?, ?, ?, ?)",
                (account_num, post_caption, post_path, post_hashtags),
            )  # Insert new credentials
            self.conn.commit()
            return "Instagram post added"  # Return a string

    def instagram_active_informations(self, account_num: Int):
        self.temp_string = ""
        self.final_string = ""
        self.data = []
        self.invalid_characters = ["(", ")", "'"]
        self.c.execute(
            "SELECT e_mail FROM instagram_accounts WHERE account_num = :account_num",
            {"account_num": account_num},
        )  # Getting e-mail
        self.data.append(self.c.fetchone())
        self.c.execute(
            "SELECT post_caption FROM instagram_posts WHERE account_num = :account_num",
            {"account_num": account_num},
        )  # Getting caption
        self.data.append(self.c.fetchone())
        self.c.execute(
            "SELECT post_hashtags FROM instagram_posts WHERE account_num = :account_num",
            {"account_num": account_num},
        )  # Getting hashtags
        self.data.append(self.c.fetchone())
        for i in self.data:  # Save array values in a temporary string
            self.temp_string += str(i)

        for (
            i
        ) in (
            self.temp_string
        ):  # Delete invalid characters from the temporary string and save it in a final string
            if i in self.invalid_characters:
                pass
            else:
                self.final_string += i

        return self.final_string  # Returns a string

    def tiktok_active_informations(self, account_num: Int):
        self.temp_string = ""
        self.final_string = ""
        self.data = []
        self.invalid_characters = ["(", ")", "'"]
        self.c.execute(
            "SELECT e_mail FROM tiktok_accounts WHERE account_num = :account_num",
            {"account_num": account_num},
        )  # Getting e-mail
        self.data.append(self.c.fetchone())
        self.c.execute(
            "SELECT post_caption FROM tiktok_posts WHERE account_num = :account_num",
            {"account_num": account_num},
        )  # Getting caption
        self.data.append(self.c.fetchone())
        self.c.execute(
            "SELECT post_hashtags FROM tiktok_posts WHERE account_num = :account_num",
            {"account_num": account_num},
        )  # Getting hashtags
        self.data.append(self.c.fetchone())
        for i in self.data:  # Save array values in a temporary string
            self.temp_string += str(i)

        for (
            i
        ) in (
            self.temp_string
        ):  # Delete invalid characters from the temporary string and save it in a final string
            if i in self.invalid_characters:
                pass
            else:
                self.final_string += i

        return self.final_string  # Returns a string

    def delete_instagram_path(self, account_num: Int):
        self.c.execute(
            "UPDATE instagram_posts SET post_path = 'None' WHERE account_num = :account_num",
            {"account_num": account_num},
        )  # Replace path with None
        self.conn.commit()
        return "Path successfully deleted"

    def delete_tiktok_path(self, account_num: Int):
        self.c.execute(
            "UPDATE tiktok_posts SET post_path = 'None' WHERE account_num = :account_num",
            {"account_num": account_num},
        )  # Replace path with None
        self.conn.commit()
        return "Path successfully deleted"
