UPDATE country_vaccination_stats
SET daily_vaccinations = (SELECT daily_vaccinations, PERCENTILE_CONT(0.5) FROM country_vaccinations_stats)
WHERE daily_vaccinations = NULL;

UPDATE country_vaccination_stats
SET daily_vaccinations = 0
WHERE daily_vaccinations = NULL;