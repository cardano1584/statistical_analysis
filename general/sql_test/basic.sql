DECLARE @DateKey AS INT = 22101;  -- Example date key (January 1, 2022)

-- Extract the year and day parts
DECLARE @YearPart AS INT = 2000 + @DateKey / 1000;  -- Add 2000 to get full year
DECLARE @DayPart AS INT = @DateKey % 1000;  -- Extract day of the year

-- Construct a standard date string and convert to DATE
SELECT DATEADD(DAY, @DayPart - 1, CONVERT(DATE, CAST(@YearPart AS VARCHAR) + '-01-01')) AS ResultingDate;
