package db

import (
	"backend/db"
	"testing"
)

func TestDelete(t *testing.T) {

	d := db.NewDatabase(true)
	err := d.Insert("test_delete", "For testing the delete function")
	if err != nil {
		t.Logf("Problem inserting data for test: %s", err)
		t.FailNow()
	}

	err = d.Delete("test_delete")
	if err != nil {
		t.Logf("Problem deleting test db item: %s", err)
		t.FailNow()
	}
	t.Log("Passed")
}
