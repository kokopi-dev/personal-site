# css build
FROM oven/bun:latest AS css

WORKDIR /app

RUN bun add tailwindcss @tailwindcss/cli

COPY tailwind.css ./tailwind.css

RUN bunx @tailwindcss/cli \
      -i ./tailwind.css \
      -o ./static/css/app.css \
      --minify


# go build
FROM golang:1.23-alpine AS builder

WORKDIR /app

RUN go install github.com/a-h/templ/cmd/templ@latest

COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN templ generate
RUN go build -o server .


# final image
FROM alpine:latest

WORKDIR /app

COPY --from=builder /app/server .
COPY --from=css /app/static/css/app.css ./static/css/app.css

EXPOSE 3500
CMD ["./server"]
