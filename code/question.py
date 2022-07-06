from flask import Flask
import sqlalchemy

#Model (data object)
#https://docs.sqlalchemy.org/en/14/orm/tutorial.html
class question():
    """
	PRIMARY KEY("id" AUTOINCREMENT)
    "id"	INTEGER NOT NULL UNIQUE,
	"text"	TEXT NOT NULL,
	"translation_text"	TEXT,
	"picture_ID"	INTEGER,
	"tags"	TEXT,
	"grades"	TEXT,
	"chapter"	INTEGER,                               
"""
    pass