#!/bin/bash

transc=$(cut -d$'\t' -f2 $1)
dirname=$(cut -d$'\t' -f1 $1 | rev | cut -d'/' -f2 - | rev | cut -d'-' -f2 - )
filename=$(cut -d$'\t' -f1 $1 | rev | cut -d'/' -f1 - | rev | cut -d'.' -f1 - | cut -d'_' -f2 -)

# converts to lowercase
transc=${transc,,} 

# delete punctuations
transc=$(echo "$transc" | tr -d '[:punct:]') 

id=$(paste <(echo "$dirname") <(echo "$filename") --delimiters '-' )

# Hypothesis File as per Kaldi's required format 
paste <(echo "$id") <(echo "$transc") | awk -F'\t' '$2!=""' -
