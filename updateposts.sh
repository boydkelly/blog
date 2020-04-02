#!/bin/bash
echo `date -Is` >> content/update.log
git add content/post/*
git commit -a -m "push by script"
git push origin master
