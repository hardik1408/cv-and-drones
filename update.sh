#!/bin/bash

git status
git add .
read name
git commit -m\"$name\"
git push origin main
