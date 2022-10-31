#!/bin/bash

clear
coverage run --branch -m pytest
coverage html
