NAME = thiagofalcao/python2.7
VERSION = 0.1.0

.PHONY: all build run test

all: build

build:
	docker build -t $(NAME):$(VERSION) .

run:
	docker run -it $(NAME)

test:
	docker run -v $PWD:/app -w /app $(NAME) /bin/sh /app/test.sh
