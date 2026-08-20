PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS galaxies (
	id TEXT PRIMARY KEY,

	idx INTEGER NOT NULL,
	prev TEXT
);

CREATE TABLE IF NOT EXISTS players (
	galaxy_id TEXT NOT NULL,
	FOREIGNKEY galaxy_id REFERENCES galaxies(id)
);
