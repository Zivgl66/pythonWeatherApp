#!/bin/bash

term=$(xsel -ob)
echo "Searching for : $term"
    open "http://www.google.com/search?q=$term"
