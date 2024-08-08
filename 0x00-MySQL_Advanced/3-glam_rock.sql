-- Lists all bands with 'Glam rock' style ranked by their longevity
-- (their splitting year (or 2022 if not split) - their formation year)

SELECT band_name, IFNULL(split, 2022) - formed AS lifespan
FROM metal_bands WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
