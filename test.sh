#!/bin/bash

curl --request POST http://localhost:5000/api/timeline_post -d 'name=Wei&email=cool@cool.com&content=Supercoolioman some filler and yes and stuff'

curl --request GET https://localhost:5000/api/timeline_post