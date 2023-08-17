#!/bin/bash

file_directory="/jmeter/tests/files"

# Get a list of files sorted by size in ascending order
files=$(du -k "$file_directory"/* | sort -n | awk '{print $2}')

versions=("S3" "Presigned URL")
tags=("S3" "PU")
ports=(8081 8080)
indexes=(0 1)

for idx in ${indexes[@]}; do
    for file in ${files[@]}; do
        size_in_bytes=$(stat -c "%s" "$file")
        size_in_mb=$(bc <<< "scale=0; $size_in_bytes / (1024*1024)")

        echo ===============================================================
        echo Starting test for ${size_in_mb}MB on version ${versions[$idx]}
        echo ===============================================================
        jmeter -n -t /jmeter/tests/S05/FileSizeTest.jmx -Jversion=${versions[$idx]} -Jport=${ports[$idx]} -Jsize=$size_in_mb -Jfile_path=$file -l /jmeter/results/${tags[$idx]}"_$size_in_mb"MB.csv
        echo ===============================================================
        echo Ending test for ${size_in_mb}MB on version ${versions[$idx]}
        echo ===============================================================
        echo \#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#
        echo \#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#
        echo \#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#
        sleep 10s
    done
    sleep 30s
done

