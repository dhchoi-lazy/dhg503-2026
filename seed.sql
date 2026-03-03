CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    major TEXT NOT NULL,
    year INT NOT NULL
);

INSERT INTO students (name, major, year) VALUES
    ('Alice Kim', 'Digital Humanities', 1),
    ('Bob Chen', 'History', 2),
    ('Charlie Park', 'Computer Science', 3),
    ('Diana Lee', 'Cultural Studies', 1),
    ('Edward Wong', 'Philosophy', 2)
ON CONFLICT DO NOTHING;
