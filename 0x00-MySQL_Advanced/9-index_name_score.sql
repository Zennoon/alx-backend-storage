-- Creates an index on the names table with the first character of the
-- name column, and the score column as keys

CREATE INDEX idx_name_first_score ON names (name(1), score);
