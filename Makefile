DC = docker compose
API_CONTAINER = backend_api_course
.PHONY: up down bash
up:
	${DC} up


down:
	${DC} down



bash:
	@echo 'run -> docker compose exec -it backend_api_course bash '
	${DC} exec -it ${API_CONTAINER} bash
