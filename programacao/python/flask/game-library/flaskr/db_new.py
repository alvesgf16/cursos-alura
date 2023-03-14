from os import environ as env

import click
import mysql.connector
from mysql.connector import errorcode

GAMES = "games"
GAMES_TABLE_CREATION_QUERY = """
CREATE TABLE `games` (
    `id` int(11) NOT NULL AUTO_INCREMENT
    `name` varchar(50) NOT NULL,
    `genre` varchar(40) NOT NULL,
    `platform` varchar(20) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
"""
USERS = "users"
USERS_TABLE_CREATION_QUERY = """
CREATE TABLE `users` (
    `name` varchar(20) NOT NULL,
    `username` varchar(10) NOT NULL,
    `password` varchar(100) NOT NULL,
    PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
"""


class Table:
    def __init__(self, a_name: str, a_creation_query: str) -> None:
        self.name = (a_name,)
        self.creation_query = a_creation_query


tables = [
    Table(USERS, USERS_TABLE_CREATION_QUERY),
    Table(GAMES, GAMES_TABLE_CREATION_QUERY)
]


def db_create() -> None:
    print("Connecting...")
    try:
        with mysql.connector.connect(
            host="localhost",
            user=env.get("MYSQL_USER"),
            password=env.get("MYSQL_PASSWORD"),
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute("DROP DATABASE IF EXISTS `game_library`;")
                cursor.execute("CREATE DATABASE `game_library`;")
                cursor.execute("USE `game_library`;")
                for table in tables:
                    print(f"Creating table {table.name}:", end=" ")
                    cursor.execute(table.creation_query)
                    print("OK")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("There is something wrong with the username or password")
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists")
        else:
            print(err)


@click.command("db-create")
def db_create_command() -> None:
    db_create()
    click.echo("Initialized the database.")
