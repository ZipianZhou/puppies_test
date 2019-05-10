To build: 
        docker build -t puppies:latest .
To run: 
        docker run -p 8000:8000 -v $(pwd):/usr/app puppies:latest
