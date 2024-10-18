FROM postgres:17
FROM postgres:latest

# Install pgvector extension
RUN apt-get update && apt-get install -y postgresql-17-pgvector

# Start the server and create the database
CMD ["postgres"]