#build stage
FROM golang:1.19.1-bullseye AS builder

WORKDIR /go/src/app
COPY . .
RUN go get -d -v ./...
RUN mkdir /go/bin/app
RUN go build -o /go/bin/app -v ./...
RUN go test ./...

#final stage
FROM golang:1.19.1-alpine
RUN apk --no-cache add ca-certificates
COPY --from=builder /go/bin/app /app
ENTRYPOINT /app
LABEL Name=backend Version=0.0.1
EXPOSE 8080
