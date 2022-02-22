#!/bin/sh
cd ..
clear
echo ------------------------------------------
echo JobBoard FastAPI Course
echo ------------------------------------------
uvicorn backend.main:app --reload 