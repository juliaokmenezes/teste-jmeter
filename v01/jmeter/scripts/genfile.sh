#!/bin/bash

sizes=(128 256 512 1024)

for s in "${sizes[@]}"; do
    dd if=/dev/zero of="$s"MB.txt bs="$s"M count=1
done
