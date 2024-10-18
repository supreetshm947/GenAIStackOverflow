CREATE TABLE IF NOT EXISTS stackoverflow_posts (
    question_id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    answer_count INT,
    last_edit_date TIMESTAMP,
    creation_date TIMESTAMP,
    tags TEXT[],
    link TEXT,
    is_answered BOOLEAN,
    closed_date TIMESTAMP,
    score INT,
    answer TEXT
);
