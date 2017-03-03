NAME = thiagofalcao/python2.7
VERSION = latest

.PHONY: all build run test

all: build

pull:
	docker pull $(NAME)

build:
	docker build -t $(NAME):$(VERSION) .

run:
	docker run -it $(NAME)

test:
	docker run -v ${CURDIR}:/app -w /app $(NAME) /bin/sh test.sh
