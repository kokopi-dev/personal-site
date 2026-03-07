package constants

type LayoutParams struct {
	Title string
	NavTitle string
}

func NewLayoutParams(title string) *LayoutParams {
	return &LayoutParams{
		Title: title,
		NavTitle: "derrickgee.dev",
	}
}
