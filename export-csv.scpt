set districtsInFile to POSIX file "districts.numbers"
set districtsOutFile to POSIX path of ("districts.csv")

tell application "Numbers"
    open districtsInFile
    tell front document
        export to file districtsOutFile as CSV
    end tell
    close front document
end tell


set markersInFile to POSIX file "markers.numbers"
set markersOutFile to POSIX path of ("markers.csv")

tell application "Numbers"
    open markersInFile
    tell front document
        export to file markersOutFile as CSV
    end tell
    close front document
end tell