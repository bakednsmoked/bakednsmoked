package db

import (
	"log"

	"github.com/google/uuid"
)

func (db Database) Insert(
	name string,
	description string,
) error {
	uuid, err := uuid.NewRandom()
	if err != nil {
		return err
	}
	qry := `
		INSERT INTO stockroom (id, name, description)
		VALUES (?, ?, ?)
	`
	_, err = db.conn.Exec(qry, uuid, name, description)
	if err != nil {
		return err
	}

	return nil
}

func (db Database) Delete(name string) error {
	qry := `
		DELETE FROM stockroom WHERE name = ?;
	`

	_, err := db.conn.Exec(qry, name)
	if err != nil {
		log.Printf("Problem deleting data: %s", err)
		return err
	}

	return nil
}

func (db Database) Get(db_item string) (string, error) {
	qry := `
		SELECT * FROM stockroom WHERE name = '?';
	`
	s_row := db.conn.QueryRow(qry, db_item)

	var s_buff string
	s_row.Scan(s_buff)
	return s_buff, nil
}
