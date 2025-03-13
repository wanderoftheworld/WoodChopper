#!/bin/bash

: '
A very neat comment.
bla dee.
'
# Check if a file is provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <header_file.h>"
    exit 1
fi

header_file="$1"

# Check if the file exists
if [ ! -f "$header_file" ]; then
    echo "Error: File $header_file not found."
    exit 1
fi

# Extract enum members from the header file
enum_members=($(grep -o '(?<=enum\s+\w+\s*\{).*?(?=\})' "$header_file" | tr -d '\n' | tr -s ' '))

# Check if any enum members were found
if [ ${#enum_members[@]} -eq 0 ]; then
    echo "Error: No enum members found in $header_file."
    exit 1
fi

# Print formatted enum members
echo "Formatted enum members:"
for member in "${enum_members[@]}"; do
    formatted_member="[${member}] = \"${member}\""
    echo "$formatted_member"
done

exit 0
