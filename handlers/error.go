package handlers

import (
	"net/http"
	"personal-site/pages"

	"github.com/gin-gonic/gin"
)

func NotFoundHandler(c *gin.Context) {
    c.Status(http.StatusNotFound)
    pages.ErrorPage().Render(c.Request.Context(), c.Writer)
}
