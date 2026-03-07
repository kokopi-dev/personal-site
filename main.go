package main

import (
	"context"
	"log"
	"net/http"
	"os"
	"os/signal"
	"personal-site/pages"
	"syscall"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
)

func setupRoutesAndMiddleware() *gin.Engine {
	r := gin.Default()
	r.Static("/static", "./static")
	r.GET("/", func(c *gin.Context) {
		page := pages.Index()
		page.Render(c.Request.Context(), c.Writer)
	})
	return r
}

func init() {
	if err := godotenv.Load(); err != nil {
		log.Println("No .env file found")
	} else {
		log.Println(".env loaded successfully")
	}
}
func main() {
	router := setupRoutesAndMiddleware()

	// dev env
	router.SetTrustedProxies(nil)

	// prod env
	// router.SetTrustedProxies([]string{"127.0.0.1"})
	// router.TrustedPlatform = gin.PlatformCloudflare

	srv := &http.Server{
		Addr:    ":3500",
		Handler: router,
	}
	go func() {
		log.Println("Server starting on :3500")
		if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			log.Fatal("Failed to start server:", err)
		}
	}()
	quit := make(chan os.Signal, 1)
	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
	<-quit

	log.Println("Shutting down server...")

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	if err := srv.Shutdown(ctx); err != nil {
		log.Fatal("Server forced to shutdown:", err)
	}

	log.Println("Server exited")

}
