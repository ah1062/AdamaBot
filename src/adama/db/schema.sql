PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS games (
	id TEXT PRIMARY KEY,
	name TEXT,
	active INTEGER NOT NULL DEFAULT 1,

	server_id INTEGER NOT NULL,
	galaxy_id TEXT NOT NULL,

	created_at TEXT DEFAULT CURRENT_TIMESTAMP,
	archived_at TEXT,

	FOREIGN KEY(galaxy_id) REFERENCES galaxies(id)
);

CREATE TABLE IF NOT EXISTS galaxies (
	id TEXT PRIMARY KEY,
	turn INTEGER NOT NULL,
	prev_id TEXT,
	next_id TEXT,

	FOREIGN KEY(prev_id) REFERENCES galaxies(id),
	FOREIGN KEY(next_id) REFERENCES galaxies(id)
);

CREATE TABLE IF NOT EXISTS ships (
	id TEXT NOT NULL,
	galaxy_id TEXT NOT NULL,

	name TEXT NOT NULL,

	location_coords TEXT NOT NULL,
	jump_coords TEXT,
	backup_jump_coords TEXT,

	PRIMARY KEY (id, galaxy_id),
	FOREIGN KEY(galaxy_id) REFERENCES galaxies(id) ON DELETE CASCADE
);	

-- CREATE TABLE IF NOT EXISTS resources ();
-- CREATE TABLE IF NOT EXISTS shuttles ();
-- CREATE TABLE IF NOT EXISTS stations ();
