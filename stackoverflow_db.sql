CREATE TABLE stackoverflow_posts (
    post_id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    tags TEXT[],
    url TEXT
);
