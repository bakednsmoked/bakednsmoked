package main

import (
	"log"
	"net/http"
	"os"

	"backend/db"
	"backend/routes"
)

func main() {

	_, err := os.Stat(db.DB_PATH)
	if err != nil {

		db.InitDB(false)
	}
	http.HandleFunc("/stock", routes.HandleStock)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
