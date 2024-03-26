from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

import src.config as config
import mysql.connector


def create_connection() -> PooledMySQLConnection | MySQLConnectionAbstract:
    return mysql.connector.connect(
      host=config.host,
      user=config.user,
      password=config.password,
      database=config.database_name
    )
