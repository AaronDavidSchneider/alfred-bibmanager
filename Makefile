PROJECT_NAME := "alfred-bibmanager"
PKG := "github.com/AaronDavidSchneider/$(PROJECT_NAME)"

package-alfred:
	@ zip -r alfred-bibmanager-workflow.alfredworkflow ./*
