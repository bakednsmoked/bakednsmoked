package db

import (
	"database/sql"
	"log"

	_ "github.com/mattn/go-sqlite3"
)

const DB_PATH = "db.sqlite"
const TEST_DB_PATH = "test_db.sqlite"

func InitDB(testing bool) {
	var db_path string
	if testing == false {
		db_path = DB_PATH
	} else {
		db_path = TEST_DB_PATH
	}
	conn, err := sql.Open("sqlite3", db_path)
	if err != nil {
		log.Fatal(err)
	}

	qry := `
		CREATE TABLE stockroom (
			id TEXT UNIQUE NOT NULL,
			name TEXT UNIQUE NOT NULL,
			description TEXT NOT NULL,
			PRIMARY KEY (id)
		);
	`
	res, err := conn.Exec(qry)
	if err != nil {
		log.Fatal(err)
	}

	log.Println(res.RowsAffected())

	err = conn.Close()
	if err != nil {
		log.Fatal(err)
	}

}
