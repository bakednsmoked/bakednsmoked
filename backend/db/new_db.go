package db

import (
	"database/sql"
	"log"
	"os"
)

type Row struct {
	name        string
	description string
}
type Database struct {
	conn sql.DB
}

func NewDatabase(testing bool) *Database {

	var db_path string
	if testing == false {
		err := os.Setenv("DB_PATH", DB_PATH)
		if err != nil {
			log.Fatalf("Problem getting env variable: %s", err)
		}
		db_path = DB_PATH
	} else {
		err := os.Setenv("DB_PATH", TEST_DB_PATH)
		if err != nil {
			log.Fatalf("Problem getting env variable: %s", err)
		}
		db_path = TEST_DB_PATH
	}

	_, er := os.Stat(db_path)
	if er != nil {
		InitDB(testing)
	}
	conn, err := sql.Open("sqlite3", db_path)
	if err != nil {
		log.Fatalf("Problem opening database: %s", err)
	}
	db := Database{
		conn: *conn,
	}
	return &db
}
