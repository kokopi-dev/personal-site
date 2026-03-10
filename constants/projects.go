package constants

type Project struct {
	Url         string
	Name        string
	Description string
	TechTags    []string
	LinkGitea   string
	LinkGithub  string
	HostedOn    string
	IsWIP       bool
}

var AllProjects = []Project{
	{
		Url:         "https://derrickgee.dev/projects/support-ticket-demo",
		Name:        "Support Ticket System",
		Description: "A sample of a robust support ticket system with the option to OAuth for database access. Authenticated users will be able to see other user created tickets. Guest mode will store tickets locally in your browser.",
		HostedOn:    "Home Server",
		LinkGitea:   "https://git.kokopi.dev/kokopi/personal-support-ticket-system",
		LinkGithub:  "https://github.com/kokopi-dev/personal-support-ticket-system",
		TechTags:    []string{"typescript", "react", "fastify", "tailwindcss", "sqlite", "vite", "bun"},
		IsWIP:       false,
	},
	{
		Url:         "/projects/dotfiles",
		Name:        "Linux Dotfiles",
		Description: "Dotfile configurations for specific linux applications.",
		HostedOn:    "",
		LinkGitea:   "https://git.kokopi.dev/kokopi/dotfiles",
		LinkGithub:  "https://github.com/kokopi-dev/dotfiles",
		TechTags:    []string{"linux", "lua", "bash", "python"},
		IsWIP:       false,
	},
	{
		Url:         "/projects/dotfiles",
		Name:        "Koko-chan",
		Description: "Paid discord bot service for handling schedules.",
		HostedOn:    "",
		LinkGitea:   "",
		LinkGithub:  "",
		TechTags:    []string{"golang", "templ", "tailwindcss"},
		IsWIP:       true,
	},
}
