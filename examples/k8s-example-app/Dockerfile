# Use the official Golang image to build the application
FROM golang:1.20 as builder

# Set the working directory inside the container
WORKDIR /app

# Copy go mod and sum files
COPY go.mod go.sum ./

# Download dependencies
RUN go mod download

# Copy the source code
COPY . .

# Build the Go application
RUN go build -o main .

# Use a minimal image for the final application
FROM alpine:latest

# Copy the Go binary from the builder stage
COPY --from=builder /app/main /app/main

# Expose the port on which the app will run
EXPOSE 8080

# Start the Go application
ENTRYPOINT ["/app/main"]
