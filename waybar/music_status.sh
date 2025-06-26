#!/bin/bash

status=$(playerctl status 2>/dev/null)
icon=""

info=$(playerctl metadata --format '{{artist}} - {{title}}' 2>/dev/null)

if [ -z "$info" ]; then
    info="No Music"
fi

if [ "$status" = "Playing" ]; then
    echo "{\"text\": \"$icon $info\", \"class\": \"playing\"}"
elif [ "$status" = "Paused" ]; then
    echo "{\"text\": \"$icon $info\", \"class\": \"paused\"}"
else
    echo "{\"text\": \"No Music\", \"class\": \"stopped\"}"
fi
