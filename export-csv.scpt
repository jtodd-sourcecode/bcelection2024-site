-- Define the root directory
set rootDir to "/Users/jtodd/GitHub/bcelection2024-site/"

-- Use the root directory to define the full input and output paths for districts
set districtsInFile to POSIX file (rootDir & "districts.numbers")
set districtsOutFile to (rootDir & "districts.csv") as POSIX file

tell application "Numbers"
    open districtsInFile
    delay 2 -- Ensure the file is fully opened
    tell front document
        -- Export as CSV
        export to districtsOutFile as CSV
    end tell
    close front document saving no
end tell

-- Use the root directory to define the full input and output paths for markers
set markersInFile to POSIX file (rootDir & "markers.numbers")
set markersOutFile to (rootDir & "markers.csv") as POSIX file

tell application "Numbers"
    open markersInFile
    delay 2 -- Ensure the file is fully opened
    tell front document
        -- Export as CSV
        export to markersOutFile as CSV
    end tell
    close front document saving no
end tell