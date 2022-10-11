package routes

import (
	"backend/db"
	"io"
	"log"
	"net/http"
	"os"

	_ "github.com/mattn/go-sqlite3"
)

func HandleStock(w http.ResponseWriter, req *http.Request) {
	log.Println("Got request for stock")
	if req.Method == http.MethodGet {
		io.WriteString(w, "Hello\n")
	}

	var testing bool
	db_path := os.Getenv("DB_PATH")
	if db_path == db.TEST_DB_PATH {
		testing = true
	} else {
		testing = false
	}

	db := db.NewDatabase(testing)
	if req.Body != nil {

		var buff []byte
		_, err := req.Body.Read(buff)
		if err != nil {
			log.Printf("Problem reading request: %s", err)
		}
		log.Printf("Req from client: %s", buff)

		row, err := db.Get(string(buff))
		if err != nil {
			log.Printf("Problem getting data from db: %s", err)
		}

		io.WriteString(w, string(row))
	}

}
