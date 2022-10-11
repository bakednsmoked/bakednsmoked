package db

import (
	"backend/db"
	"os"
	"testing"
)

func TestInsertDB(t *testing.T) {
	_, err := os.Stat(db.TEST_DB_PATH)
	if err != nil {
		db.InitDB(true)
	}
	d := db.NewDatabase(true)
	err = d.Insert("test_name", "a test description")
	if err != nil {
		t.Log(err)
		t.FailNow()
	}
	d.Delete("test_name")
	t.Log("Passed")
}
