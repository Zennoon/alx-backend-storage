-- Creates index for the names table with the name column

CREATE INDEX idx_name_first ON names (name(1));
